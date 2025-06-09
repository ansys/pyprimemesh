# Copyright (C) 2024 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Module for LS-DYNA export utilities."""

########################### [TODO] ##################################
# [TODO] code quality of this file is not up to PyPrimeMesh standards,
# please move the code to cpp or improve the code quality
########################### [TODO] ##################################

import ansys.meshing.prime as prime

__all__ = ['MaterialProcessor', 'DatabaseProcessor']

# class _TractionProperties:
#     DAMAGE_EVOLUTION_ENERGY = 1000
#     NOM_STRESS_1 = 1e10
#     NOM_STRESS_2 = 1e10
#     NOM_STRESS_3 = 1e10


class _FormatDynaCards:
    __slots__ = ('_card_format', '_format_map')

    def __init__(self, card_format):
        self._card_format = card_format
        self._format_map = {"SHORT": 10, "LONG": 20}

    def field_int(self, num):
        field_len = self._format_map[self._card_format]
        if len(str(num)) <= field_len:
            blank_space = field_len - len(str(num))
            field = ' ' * blank_space + str(num)
        else:
            field = self.field_exp(num)
        return field

    def field_exp(self, f):
        field_len = self._format_map[self._card_format]
        if field_len < 7:
            field_len = 7
        s = "%.*e" % (field_len - 7, f)
        mantissa, exp = s.split('e')
        sign = ' '
        if f < 0:
            sign = ''
        # add 1 to digits as 1 is taken by sign +/-
        return sign + "%se%+0*d" % (mantissa, 2 + 1, int(exp))

    def field_float(self, num):
        field_len = self._format_map[self._card_format]
        if len(str(num)) <= field_len:
            blank_space = field_len - len(str(num))
            field = ' ' * blank_space + str(num)
        else:
            if abs(float(num)) < 1e-3:
                field = self.field_exp(num)
            elif abs(float(num)) > 1e-3 and len(str(int(float(num)))) < 7:
                field = str(num)[:field_len]
            else:
                field = self.field_exp(num)
        # else:
        # if abs(float(num)) < 1000:
        # field = str(num)[:field_len]
        # elif len(str(int(float(num)))) < 7:
        # field = str(num)[:field_len]
        # else:
        # field = self.field_exp(num)

        # below lines are not to be added in any case
        # if len(str(round(float(num), 2))) <= field_len:
        # blank_space = field_len - len(str(num))
        # field = ' ' * blank_space + str(num)[:field_len]
        # else:
        # field = self.field_exp(num)
        return field

    def field_str(self, string):
        field_len = self._format_map[self._card_format]
        if len(string) <= field_len:
            blank_space = field_len - len(string)
            field = ' ' * blank_space + str(string)
        else:
            field = string[0:field_len]
        return field

    def field_less_1_str(self, string):
        field_len = self._format_map[self._card_format]
        if len(string) <= field_len - 1:
            blank_space = field_len - 1 - len(string)
            field = ' ' * blank_space + str(string)
        else:
            field = string[0 : field_len - 1]
        return field


class _MatGlass:
    __slots__ = (
        '_card_format',
        '_formatter',
        '_format_map',
        '_header_title',
        '_header',
        '_data_line',
        '_model',
        '_logger',
    )

    def __init__(self, model: prime.Model, card_format="SHORT"):
        self._card_format = card_format
        self._formatter = _FormatDynaCards(self._card_format)
        self._format_map = {"SHORT": 10, "LONG": 20}
        self._header_title = ["mid", "ro", "e", "pr", "-", "-", "imod", "ilaw"]
        self._header = [1, 1.000e-09, 0.0, 0.0]
        self._data_line = {
            "D1_TITLE": ["fmod", "ft", "fc", "at", "bt", "ac", "bc", 'ftscl'],
            "D1_DATA": ['', 0.0, 0.0, '', '', '', '', 1],
            "D2_TITLE": ["sfsti", "sfstr", "crin", "ecrcl", "ncycr", "nipf"],
            "D2_DATA": [0.0001, 0.01, 1, 0.002, 5.0, 5],
            "D3_TITLE": ["epscr", "engcrt", "radcrt", "raten1", "rfiltf"],
            "D3_DATA": [-0.16],
        }
        self._model = model
        self._logger = model.python_logger

    def get_britle_glass_commands(self, mat_id, mat_name, all_mat_props, e, pr, density):
        mat_props = all_mat_props["BRITTLE CRACKING"]
        mat_fields = mat_props["Data"]
        params = mat_props["Parameters"]
        if "TYPE" in params and params["TYPE"] != "STRAIN":
            self._logger.warning(
                f"Warning: Material {mat_name} (id={mat_id}) is not processed. "
                f"it has BRITTLE CRACKING"
            )
            return ""
        stress = 0.0
        if "Remaining direct stress after cracking" in mat_fields:
            stress = float(mat_fields["Remaining direct stress after cracking"][0])
        else:
            self._logger.warning(
                f"Warning: Material {mat_name} (id={mat_id}) is not processed. "
                f"it has BRITTLE CRACKING"
            )
            return ""
        mat_string = ""
        translated = False
        header_data = self._header
        header_data[0] = mat_id
        header_data[1] = density
        header_data[2] = e
        header_data[3] = pr
        self._data_line["D1_DATA"][1] = stress
        self._data_line["D1_DATA"][2] = 20 * stress
        mat_string += "*MAT_GLASS_TITLE\n"
        mat_string += f"{mat_name}\n"
        mat_string += "$#" + "".join([self._formatter.field_str(i) for i in self._header_title])[2:]
        mat_string += "\n"
        mat_string += self._formatter.field_int(header_data[0])
        mat_string += "".join([self._formatter.field_float(i) for i in header_data[1:]])
        mat_string += "\n"
        mat_string += (
            "$#"
            + "".join([self._formatter.field_str(i) for i in self._data_line["D1_TITLE"]])[2:]
            + "\n"
        )
        mat_string += self._formatter.field_str(self._data_line["D1_DATA"][0])
        mat_string += self._formatter.field_float(self._data_line["D1_DATA"][1])
        mat_string += self._formatter.field_float(self._data_line["D1_DATA"][2])
        mat_string += self._formatter.field_str(self._data_line["D1_DATA"][3])
        mat_string += self._formatter.field_str(self._data_line["D1_DATA"][4])
        mat_string += self._formatter.field_str(self._data_line["D1_DATA"][5])
        mat_string += self._formatter.field_str(self._data_line["D1_DATA"][6])
        mat_string += self._formatter.field_int(self._data_line["D1_DATA"][7])
        mat_string += "\n"
        mat_string += (
            "$#"
            + "".join([self._formatter.field_str(i) for i in self._data_line["D2_TITLE"]])[2:]
            + "\n"
        )
        mat_string += self._formatter.field_float(self._data_line["D2_DATA"][0])
        mat_string += self._formatter.field_float(self._data_line["D2_DATA"][1])
        mat_string += self._formatter.field_int(self._data_line["D2_DATA"][2])
        mat_string += self._formatter.field_float(self._data_line["D2_DATA"][3])
        mat_string += self._formatter.field_float(self._data_line["D2_DATA"][4])
        mat_string += self._formatter.field_int(self._data_line["D2_DATA"][5])
        mat_string += "\n"
        mat_string += (
            "$#"
            + "".join([self._formatter.field_str(i) for i in self._data_line["D3_TITLE"]])[2:]
            + "\n"
        )
        mat_string += self._formatter.field_float(self._data_line["D3_DATA"][0])
        mat_string += "\n"
        return mat_string


class _MatHyperelasticYeoh:
    __slots__ = (
        '_card_format',
        '_formatter',
        '_format_map',
        '_header_title',
        '_header',
        '_data_line',
        '_model',
        '_logger',
    )

    def __init__(self, model: prime.Model, card_format="SHORT"):
        self._card_format = card_format
        self._formatter = _FormatDynaCards(self._card_format)
        self._format_map = {"SHORT": 10, "LONG": 20}
        self._header_title = ["mid", "ro", "pr", "n", "nv", "g", "sgif", "ref"]
        self._header = [1, 1.000e-09, 0.0, 0, 0, 2500.0, 5.0]
        self._data_line = {
            "D1_TITLE": ["C10", "C01", "C11", "C20", "C02", "C30", "THERMAL"],
            "D1_DATA": [0.0, " ", " ", 0.0, " ", 0.0],
        }
        self._model = model
        self._logger = model.python_logger


class _MatOgdenRubber:
    __slots__ = (
        '_card_format',
        '_formatter',
        '_format_map',
        '_header_title',
        '_header',
        '_data_line',
        '_model',
        '_logger',
    )

    def __init__(self, model: prime.Model, card_format="SHORT"):
        self._card_format = card_format
        self._formatter = _FormatDynaCards(self._card_format)
        self._format_map = {"SHORT": 10, "LONG": 20}
        self._header_title = ["mid", "ro", "pr", "n", "nv", "g", "sgif", "ref"]
        self._header = [1, 1.000e-09, 0.0, 0, 0, 2500.0, 5.0]
        self._data_line = {
            "D1_TITLE": ["MU1", "MU2", "MU3", "MU4", "MU5", "MU6", "MU7", "MU8"],
            "D1_DATA": ["", "", "", "", "", "", "", ""],
            "D2_TITLE": [
                "ALPHA1",
                "ALPHA2",
                "ALPHA3",
                "ALPHA4",
                "ALPHA5",
                "ALPHA6",
                "ALPHA7",
                "ALPHA8",
            ],
            "D2_DATA": ["", "", "", "", "", "", "", ""],
        }
        self._model = model
        self._logger = model.python_logger


class _MatHyperelastic:
    __slots__ = ('_card_format', '_formatter', '_format_map', '_model', '_logger')

    def __init__(self, model: prime.Model, card_format="SHORT"):
        self._card_format = card_format
        self._formatter = _FormatDynaCards(self._card_format)
        self._format_map = {"SHORT": 10, "LONG": 20}
        # self._header_title = ["mid", "ro", "pr", "n", "nv", "g", "sgif", "ref"]
        # self._header = [1, 1.000E-09, 0.0, 0, 0, 2500.0, 5.0]
        # self._data_line = {
        # "D1_TITLE": ["C10", "C01", "C11", "C20", "C02", "C30", "THERMAL"],
        # "D1_DATA": [0.0, " "," ", 0.0, " ", 0.0]
        # }
        self._model = model
        self._logger = model.python_logger

    def define_hyper_elastic(
        self, mat_id, mat_name, all_mat_props, weight=1, density=1e-9, poisson_ratio=0.497
    ):
        # self._logger.info("hyper elastic")
        mat_props = all_mat_props["HYPERELASTIC"]
        mat_fields = mat_props["Data"]
        mat_string = ""
        translated = False
        if mat_props["Parameters"] and "YEOH" in mat_props["Parameters"]:
            if "TEST DATA INPUT" not in mat_props["Parameters"]:
                mat_yeoh = _MatHyperelasticYeoh(self._model, card_format=self._card_format)
                C10 = "" if "C10" not in mat_fields else mat_fields["C10"][0]
                C20 = "" if "C20" not in mat_fields else mat_fields["C20"][0]
                C30 = "" if "C30" not in mat_fields else mat_fields["C30"][0]
                D1 = "" if "D1" not in mat_fields else mat_fields["D1"][0]
                D2 = "" if "D2" not in mat_fields else mat_fields["D2"][0]
                D3 = "" if "D3" not in mat_fields else mat_fields["D3"][0]
                temperature = "" if "Temperature" not in mat_fields else mat_fields["Temperature"]
                if len(temperature) > 1:
                    self._logger.warning(
                        f"Multiple temperatures for material "
                        f"{mat_name} (ID {mat_id}) are not preocessed"
                    )
                order = 3
                if str(C30).strip() == "":
                    order = 2
                if str(C20).strip() == "":
                    order = 1
                header_data = mat_yeoh._header
                header_data[0] = mat_id
                header_data[1] = density
                header_data[2] = poisson_ratio
                if C10:
                    mat_yeoh._data_line["D1_DATA"][0] = weight * float(C10)
                if C20:
                    mat_yeoh._data_line["D1_DATA"][3] = weight * float(C20)
                if C30:
                    mat_yeoh._data_line["D1_DATA"][5] = weight * float(C30)

                header_data[5] = 2 * float(C10) * weight
                header_data[6] = 2 * float(C10) * weight / 500

                mat_string += "*MAT_HYPERELASTIC_RUBBER_TITLE\n"
                mat_string += f"{mat_name}\n"
                mat_string += (
                    "$#"
                    + "".join([self._formatter.field_str(i) for i in mat_yeoh._header_title])[2:]
                )
                mat_string += "\n"
                mat_string += self._formatter.field_int(header_data[0])
                mat_string += self._formatter.field_exp(header_data[1])
                mat_string += self._formatter.field_float(header_data[2])
                mat_string += self._formatter.field_int(header_data[3])
                mat_string += self._formatter.field_int(header_data[4])
                mat_string += self._formatter.field_float(header_data[5])
                mat_string += self._formatter.field_float(header_data[6])
                mat_string += "\n"
                mat_string += (
                    "$#"
                    + "".join(
                        [self._formatter.field_str(i) for i in mat_yeoh._data_line["D1_TITLE"]]
                    )[2:]
                    + "\n"
                )
                mat_string += self._formatter.field_float(mat_yeoh._data_line["D1_DATA"][0])
                mat_string += self._formatter.field_str(mat_yeoh._data_line["D1_DATA"][1])
                mat_string += self._formatter.field_str(mat_yeoh._data_line["D1_DATA"][2])
                mat_string += self._formatter.field_float(mat_yeoh._data_line["D1_DATA"][3])
                mat_string += self._formatter.field_str(mat_yeoh._data_line["D1_DATA"][4])
                mat_string += self._formatter.field_float(mat_yeoh._data_line["D1_DATA"][5])
                mat_string += "\n"
                # *MAT_HYPERELASTIC_RUBBER_TITLE
                # New_44_MAT_OS_BUMPER_YEOH_H60_VISCO
                # 44              1.5E-9               0.496         0
                # 0                  0.                                      0.
                # 0.7212886543097898
                # -0.27228646700194564                     0.16228994721970272
                translated = True
            else:
                self._logger.warning(
                    f"Test data for Material {mat_name} (ID {mat_id}) "
                    f"with hyperelastic property is not translated "
                )
        # self._logger.info(mat_string)
        elif mat_props["Parameters"] and "OGDEN" in mat_props["Parameters"]:
            if "TEST DATA INPUT" not in mat_props["Parameters"]:
                N = 1
                if "N" in mat_props["Parameters"]:
                    N = int(mat_props["Parameters"]['N'])
                temperature = "" if "Temperature" not in mat_fields else mat_fields["Temperature"]
                if len(temperature) > 1:
                    self._logger.warning(
                        f"Multiple temperatures for material {mat_name} (ID {mat_id}) "
                        f"are not preocessed"
                    )
                D = []
                u = []
                alpha = []
                for i in range(1, N + 1):
                    # self._logger.info(f"D{i} = {mat_fields[f'D{i}'][0]}")
                    # self._logger.info(f"u{i} = {mat_fields[f'u{i}'][0]}")
                    # self._logger.info(f"a{i} = {mat_fields[f'a{i}'][0]}")
                    D.append("" if f"D{i}" not in mat_fields else mat_fields[f"D{i}"][0])
                    u.append("" if f"u{i}" not in mat_fields else mat_fields[f"u{i}"][0])
                    alpha.append("" if f"a{i}" not in mat_fields else mat_fields[f"a{i}"][0])
                U0 = 0
                MU = []
                for i in range(N):
                    MU.append(2 * float(u[i]) / float(alpha[i]))
                    U0 += float(u[i])
                K0 = None
                if D[0]:
                    K0 = 2 / float(D[0])
                else:
                    self._logger.warning(
                        f"D1 parameter is zero or not available in "
                        f"hyperelastic ogden material (ID: {mat_id} Name: {mat_name}"
                    )
                if K0 is not None:
                    pr = ((3 * K0 / U0) - 2) / ((6 * K0 / U0) + 2)
                else:
                    pr = 0.075
                    self._logger.warning(
                        f"The poisson's ratio have been hardcoded to 0.075 in "
                        f"hyperelastic ogden material (ID: {mat_id} Name: {mat_name}"
                    )
                mat_ogden = _MatOgdenRubber(self._model, card_format=self._card_format)
                header_data = mat_ogden._header
                header_data[0] = mat_id
                header_data[1] = density
                header_data[2] = poisson_ratio
                mat_string += "*MAT_OGDEN_RUBBER_TITLE\n"
                mat_string += f"{mat_name}\n"
                mat_string += (
                    "$#"
                    + "".join([self._formatter.field_str(i) for i in mat_ogden._header_title])[2:]
                )
                mat_string += "\n"
                mat_string += self._formatter.field_int(header_data[0])
                mat_string += self._formatter.field_exp(header_data[1])
                mat_string += self._formatter.field_float(header_data[2])
                mat_string += self._formatter.field_int(header_data[3])
                mat_string += self._formatter.field_int(header_data[4])
                mat_string += self._formatter.field_float(header_data[5])
                mat_string += self._formatter.field_float(header_data[6])
                mat_string += "\n"
                mat_string += (
                    "$#"
                    + "".join(
                        [self._formatter.field_str(i) for i in mat_ogden._data_line["D1_TITLE"]]
                    )[2:]
                    + "\n"
                )
                for j in range(len(MU)):
                    mat_ogden._data_line["D1_DATA"][j] = MU[j]
                    mat_string += self._formatter.field_float(mat_ogden._data_line["D1_DATA"][j])
                mat_string += (
                    "".join(
                        [
                            self._formatter.field_str(i)
                            for i in mat_ogden._data_line["D1_DATA"][len(MU) :]
                        ]
                    )
                    + "\n"
                )
                mat_string += (
                    "$#"
                    + "".join(
                        [self._formatter.field_str(i) for i in mat_ogden._data_line["D1_TITLE"]]
                    )[2:]
                    + "\n"
                )
                for j in range(len(alpha)):
                    # self._logger.info(f"alpha[{j}] = {alpha[j]}")
                    mat_ogden._data_line["D2_DATA"][j] = alpha[j]
                    mat_string += self._formatter.field_float(mat_ogden._data_line["D2_DATA"][j])
                mat_string += (
                    "".join(
                        [
                            self._formatter.field_str(i)
                            for i in mat_ogden._data_line["D2_DATA"][len(MU) :]
                        ]
                    )
                    + "\n"
                )
                mat_string += "\n"
                translated = True
            else:
                self._logger.warning(
                    f"Test data for Material {mat_name} (ID {mat_id}) "
                    f"with hyperelastic property is not translated "
                )
        else:
            self._logger.warning(
                f"Material {mat_name} (ID {mat_id}) "
                f"with hyperelastic property is not translated "
            )
            translated = True
        if not translated:
            self._logger.warning(
                f"Material {mat_name} (ID {mat_id}) "
                f"with hyperelastic property is not translated "
            )
            # mat_string += "! UnTranslated Hyper Elastic Part
            # of the material MAT ID {0}".format(abq_mat._id)
        return mat_string


class _DefineCurve:
    __slots__ = (
        '_card_format',
        '_formatter',
        '_format_map',
        '_header_title',
        '_header',
        '_model',
        '_logger',
    )
    _curve_id_list = []

    def __init__(self, model: prime.Model, card_format="SHORT"):
        self._card_format = card_format
        self._formatter = _FormatDynaCards(self._card_format)
        self._format_map = {"SHORT": 10, "LONG": 20}
        self._header_title = ["lcid", "sidr", "sfa", "sfo", "offa", "offo", "dattyp", "lcint"]
        self._header = [1, 0, 1.0, 1.0, 0.0, 0.0, 0, 0]
        self._model = model
        self._logger = model.python_logger

    def get_valid_curve_id(self, mat_id, _id_init=100):
        init = _id_init
        if int(str(_id_init) + str(mat_id)) in _DefineCurve._curve_id_list:
            _id = self.get_valid_curve_id(mat_id, _id_init=init + 100)
        else:
            _id = int(str(_id_init) + str(mat_id))
        return _id

    def write_uniaxial_data_curve_card(self, mat_id, mat_name, curve_data):
        self._formatter._card_format = 'SHORT'
        mat_string = ""
        mat_string += "*DEFINE_CURVE_TITLE\n"
        mat_string += f"UNIAXIAL TEST DATA: {mat_name}\n"
        mat_string += "$#" + "".join([self._formatter.field_str(i) for i in self._header_title])[2:]
        mat_string += "\n"
        curve_id = self.get_valid_curve_id(mat_id)
        header_data = self._header
        header_data[0] = curve_id
        mat_string += self._formatter.field_int(header_data[0])
        mat_string += self._formatter.field_int(header_data[1])
        # mat_string += "".join([self._formatter.field_float(i) for i in header_data[1:5]])
        # mat_string += "".join([self._formatter.field_int(i) for i in header_data[5:]])
        mat_string += "\n"
        self._formatter._card_format = 'LONG'
        mat_string += (
            "$#" + "".join([self._formatter.field_str('a1'), self._formatter.field_str('o1')])[2:]
        )
        mat_string += "\n"
        if 'Data' in curve_data and curve_data['Data'] is not None:
            stress = reversed(curve_data['Data']['Nominal stress'])
            strain = reversed(curve_data['Data']['Nominal strain'])
            nominal_lat_strain = curve_data['Data'][
                f"Nominal lateral strain, . Default is zero. "
                f"Not needed if the POISSON parameter is specified on the *HYPERFOAM option"
            ]
            for e, s in zip(strain, stress):
                mat_string += ''.join(
                    [self._formatter.field_float(float(e)), self._formatter.field_float(float(s))]
                )
                mat_string += "\n"
        _DefineCurve._curve_id_list.append(curve_id)
        return curve_id, mat_string

    def write_uniaxial_data_curve_card_for_low_density_foam(self, mat_id, mat_name, curve_data):
        self._formatter._card_format = 'SHORT'
        mat_string = ""
        mat_string += "*DEFINE_CURVE_TITLE\n"
        mat_string += f"UNIAXIAL TEST DATA: {mat_name}\n"
        mat_string += "$#" + "".join([self._formatter.field_str(i) for i in self._header_title])[2:]
        mat_string += "\n"
        curve_id = self.get_valid_curve_id(mat_id)
        header_data = self._header
        header_data[0] = curve_id
        mat_string += self._formatter.field_int(header_data[0])
        mat_string += self._formatter.field_int(header_data[1])
        # mat_string += "".join([self._formatter.field_float(i) for i in header_data[1:5]])
        # mat_string += "".join([self._formatter.field_int(i) for i in header_data[5:]])
        mat_string += "\n"
        self._formatter._card_format = 'LONG'
        mat_string += (
            "$#" + "".join([self._formatter.field_str('a1'), self._formatter.field_str('o1')])[2:]
        )
        mat_string += "\n"
        if 'Data' in curve_data and curve_data['Data'] is not None:
            stress = curve_data['Data']['Nominal stress']
            strain = curve_data['Data']['Nominal strain']
            nominal_lat_strain = curve_data['Data'][
                "Nominal lateral strain, . Default is zero. "
                f"Not needed if the POISSON parameter is specified on the *HYPERFOAM option"
            ]
            for e, s in zip(strain, stress):
                if float(e) != 0.0 or float(s) != 0.0:
                    mat_string += ''.join(
                        [
                            self._formatter.field_float(-1 * float(e)),
                            self._formatter.field_float(-1 * float(s)),
                        ]
                    )
                else:
                    mat_string += ''.join(
                        [
                            self._formatter.field_float(float(e)),
                            self._formatter.field_float(float(s)),
                        ]
                    )
                mat_string += "\n"
        _DefineCurve._curve_id_list.append(curve_id)
        return curve_id, mat_string

    def write_plastic_curve_card(self, mat_id, mat_name, curve_data):
        self._formatter._card_format = 'SHORT'
        mat_string = ""
        mat_string += "*DEFINE_CURVE_TITLE\n"
        mat_string += f"PLASTIC CURVE: {mat_name}\n"
        mat_string += "$#" + "".join([self._formatter.field_str(i) for i in self._header_title])[2:]
        mat_string += "\n"
        curve_id = self.get_valid_curve_id(mat_id)
        header_data = self._header
        header_data[0] = curve_id
        mat_string += self._formatter.field_int(header_data[0])
        mat_string += self._formatter.field_int(header_data[1])
        # mat_string += "".join([self._formatter.field_float(i) for i in header_data[1:5]])
        # mat_string += "".join([self._formatter.field_int(i) for i in header_data[5:]])
        mat_string += "\n"
        self._formatter._card_format = 'LONG'
        mat_string += (
            "$#" + "".join([self._formatter.field_str('a1'), self._formatter.field_str('o1')])[2:]
        )
        mat_string += "\n"
        if 'Data' in curve_data and curve_data['Data'] is not None:
            stress = []
            strain = []
            stress = curve_data['Data']['Yield stress']
            strain = curve_data['Data']['Plastic strain']
            sigy = float(stress[0])
            temperature = []
            if "Temperature" in curve_data['Data']:
                temperature = curve_data['Data']['Temperature']
            if temperature:
                t_old = None
                for e, s, t in zip(strain, stress, temperature):
                    if t_old is None:
                        t_old = float(t)
                    if t_old == float(t):
                        mat_string += ''.join(
                            [
                                self._formatter.field_float(float(e)),
                                self._formatter.field_float(float(s)),
                            ]
                        )
                        mat_string += "\n"
                    else:
                        self._logger.warning(
                            f"Warning: Plastic data on {mat_name} has multiple temperature data."
                            f"It is not processed."
                        )
                        break
            else:
                for e, s in zip(strain, stress):
                    mat_string += ''.join(
                        [
                            self._formatter.field_float(float(e)),
                            self._formatter.field_float(float(s)),
                        ]
                    )
                    mat_string += "\n"
        _DefineCurve._curve_id_list.append(curve_id)
        return curve_id, mat_string, sigy

    def write_damage_curve(self, mat_id, mat_name, curve_data):
        self._formatter._card_format = 'SHORT'
        mat_string = ""
        mat_string += "*DEFINE_CURVE_TITLE\n"
        mat_string += f"DAMAGE CURVE: {mat_name}\n"
        mat_string += "$#" + "".join([self._formatter.field_str(i) for i in self._header_title])[2:]
        mat_string += "\n"
        curve_id = self.get_valid_curve_id(mat_id)
        header_data = self._header
        header_data[0] = curve_id
        mat_string += self._formatter.field_int(header_data[0])
        mat_string += self._formatter.field_int(header_data[1])
        # mat_string += "".join([self._formatter.field_float(i) for i in header_data[1:5]])
        # mat_string += "".join([self._formatter.field_int(i) for i in header_data[5:]])
        mat_string += "\n"
        self._formatter._card_format = 'LONG'
        mat_string += (
            "$#" + "".join([self._formatter.field_str('a1'), self._formatter.field_str('o1')])[2:]
        )
        mat_string += "\n"
        # self._logger.info(curve_data)
        mat_string += (
            ''.join(
                [
                    self._formatter.field_float(float(curve_data[0])),
                    self._formatter.field_float(float(curve_data[1])),
                ]
            )
            + "\n"
        )
        mat_string += (
            ''.join(
                [
                    self._formatter.field_float(-1 * float(curve_data[0])),
                    self._formatter.field_float(float(curve_data[1])),
                ]
            )
            + "\n"
        )
        _DefineCurve._curve_id_list.append(curve_id)
        return curve_id, mat_string

    def create_damage_curve_for_cohesive_mixed_mode(self, mat_id, mat_name, thickness, gic):
        self._formatter._card_format = 'SHORT'
        mat_string = ""
        mat_string += "*DEFINE_CURVE_TITLE\n"
        mat_string += f"THICK vs {mat_name}\n"
        mat_string += "$#" + "".join([self._formatter.field_str(i) for i in self._header_title])[2:]
        mat_string += "\n"
        curve_id = self.get_valid_curve_id(mat_id)
        header_data = self._header
        header_data[0] = curve_id
        mat_string += self._formatter.field_int(header_data[0])
        mat_string += self._formatter.field_int(header_data[1])
        # mat_string += "".join([self._formatter.field_float(i) for i in header_data[1:5]])
        # mat_string += "".join([self._formatter.field_int(i) for i in header_data[5:]])
        mat_string += "\n"
        self._formatter._card_format = 'LONG'
        mat_string += (
            "$#" + "".join([self._formatter.field_str('a1'), self._formatter.field_str('o1')])[2:]
        )
        mat_string += "\n"
        # self._logger.info(curve_data)
        mat_string += (
            ''.join(
                [
                    self._formatter.field_float(float(0.1 * thickness)),
                    self._formatter.field_float(float(0.1 * gic)),
                ]
            )
            + "\n"
        )
        mat_string += (
            ''.join(
                [
                    self._formatter.field_float(float(thickness)),
                    self._formatter.field_float(float(gic)),
                ]
            )
            + "\n"
        )
        mat_string += (
            ''.join(
                [
                    self._formatter.field_float(float(10 * thickness)),
                    self._formatter.field_float(float(10 * gic)),
                ]
            )
            + "\n"
        )
        _DefineCurve._curve_id_list.append(curve_id)
        return curve_id, mat_string

    def create_damage_curve_for_traction(self, mat_id, mat_name, k, e, fe, thickness):
        self._formatter._card_format = 'SHORT'
        t = k * e
        u_tot = e * thickness + 2 * fe / t
        peak = e * thickness / u_tot
        curve = [[0, 0], [peak, 1], [1, 0]]
        mat_string = ""
        mat_string += "*DEFINE_CURVE_TITLE\n"
        mat_string += f"TRACTION DAMAGE CURVE: {mat_name}\n"
        mat_string += "$#" + "".join([self._formatter.field_str(i) for i in self._header_title])[2:]
        mat_string += "\n"
        curve_id = self.get_valid_curve_id(mat_id)
        header_data = self._header
        header_data[0] = curve_id
        mat_string += self._formatter.field_int(header_data[0])
        mat_string += self._formatter.field_int(header_data[1])
        # mat_string += "".join([self._formatter.field_float(i) for i in header_data[1:5]])
        # mat_string += "".join([self._formatter.field_int(i) for i in header_data[5:]])
        mat_string += "\n"
        self._formatter._card_format = 'LONG'
        mat_string += (
            "$#" + "".join([self._formatter.field_str('a1'), self._formatter.field_str('o1')])[2:]
        )
        mat_string += "\n"
        # self._logger.info(curve_data)
        mat_string += (
            ''.join(
                [
                    self._formatter.field_float(float(curve[0][0])),
                    self._formatter.field_float(float(curve[0][1])),
                ]
            )
            + "\n"
        )
        mat_string += (
            ''.join(
                [
                    self._formatter.field_float(float(curve[1][0])),
                    self._formatter.field_float(float(curve[1][1])),
                ]
            )
            + "\n"
        )
        mat_string += (
            ''.join(
                [
                    self._formatter.field_float(float(curve[2][0])),
                    self._formatter.field_float(float(curve[2][1])),
                ]
            )
            + "\n"
        )
        _DefineCurve._curve_id_list.append(curve_id)
        return curve_id, mat_string

    def create_damage_normalized_curve(
        self, mat_id, mat_name, young, damage_len, curve_data, thickness
    ):
        # mat = ((0.0, 1e20), (1.0, 1e20))
        self._formatter._card_format = 'SHORT'
        curve = []
        T_tract = 0.0
        if 'Data' in curve_data and curve_data['Data'] is not None:
            stress = []
            strain = []
            stress = curve_data['Data']['Yield stress']
            strain = curve_data['Data']['Plastic strain']
            sigy = float(stress[0])
            temperature = []
            if "Temperature" in curve_data['Data']:
                temperature = curve_data['Data']['Temperature']
            if temperature:
                t_old = None
                for e, s, t in zip(strain, stress, temperature):
                    if t_old is None:
                        t_old = float(t)
                    if t_old == float(t):
                        curve.append([float(s), float(e)])
                    else:
                        self._logger.warning(
                            f"Warning: Plastic data on {mat_name} has multiple temperature data."
                            f"It is not processed."
                        )
                        break
            else:
                for e, s in zip(strain, stress):
                    curve.append([float(s), float(e)])
        T_tract = curve[-1][0]
        updated_curve = [[0, 0]]
        for item in curve:
            updated_curve.append(
                [(float(item[1]) + float(item[0]) / float(young)) * thickness, item[0]]
            )

        norm_strain = updated_curve[-1][0] + damage_len
        norm_stress = updated_curve[-1][1]

        updated_curve.append([updated_curve[-1][0] + damage_len, 0])

        area = 0
        for i in range(len(updated_curve) - 1):
            e1 = updated_curve[i][0]
            s1 = updated_curve[i][1]
            e2 = updated_curve[i + 1][0]
            s2 = updated_curve[i + 1][1]

            de = e2 - e1
            ds = s2 - s1
            area += de * s1 + 0.5 * de * ds

        updated_curve_2 = []
        for item in updated_curve:
            updated_curve_2.append([item[0] / norm_strain, item[1] / norm_stress])

        mat_string = ""
        mat_string += "*DEFINE_CURVE_TITLE\n"
        mat_string += f"COHESIVE DAMAGE CURVE: {mat_name}\n"
        mat_string += "$#" + "".join([self._formatter.field_str(i) for i in self._header_title])[2:]
        mat_string += "\n"
        curve_id = self.get_valid_curve_id(mat_id)
        header_data = self._header
        header_data[0] = curve_id
        mat_string += self._formatter.field_int(header_data[0])
        mat_string += self._formatter.field_int(header_data[1])
        # mat_string += "".join([self._formatter.field_float(i) for i in header_data[1:5]])
        # mat_string += "".join([self._formatter.field_int(i) for i in header_data[5:]])
        mat_string += "\n"
        self._formatter._card_format = 'LONG'
        mat_string += (
            "$#" + "".join([self._formatter.field_str('a1'), self._formatter.field_str('o1')])[2:]
        )
        mat_string += "\n"
        # self._logger.info(curve_data)
        for a, b in updated_curve_2:
            mat_string += (
                ''.join(
                    [self._formatter.field_float(float(a)), self._formatter.field_float(float(b))]
                )
                + "\n"
            )
        _DefineCurve._curve_id_list.append(curve_id)
        return curve_id, mat_string, area, T_tract


class _MatSimplifiedRubberFoam:
    __slots__ = (
        '_card_format',
        '_formatter',
        '_format_map',
        '_header_title',
        '_header',
        '_data_line',
        '_model',
        '_logger',
    )

    def __init__(self, model: prime.Model, card_format="SHORT"):
        self._card_format = card_format
        self._formatter = _FormatDynaCards(self._card_format)
        self._format_map = {"SHORT": 10, "LONG": 20}
        self._header_title = ["mid", "ro", "km", "mu", "g", "sigf", "ref", "prten"]
        self._header = [1, 1.000e-09, 0.0, 0.1, 0.0, 0.0, 0.0, 0.0]
        self._data_line = {
            "D1_TITLE": ["sg1", "sw", "st", "lc/tbid", "tension", "rtype", "avgopt", "pr/beta"],
            "D1_DATA": [1.0, 1.0, 1.0, 1, 1.0, 0.0, 0.0, 0.01],
            "D2_TITLE": ["lcunld", "hu", "shape", "stol", "visco", "hisout"],
            "D2_DATA": [0, 1.0, 0.0, 0, 0.0, 0.0],
        }
        self._model = model
        self._logger = model.python_logger

    def write_simplified_rubber_foam(self, mat_id, mat_name, all_mat_props, density=1e-9):
        mat_string = ""
        mat_string += "*MAT_SIMPLIFIED_RUBBER/FOAM_TITLE\n"
        mat_string += f"{mat_name}\n"
        mat_string += "$#" + "".join([self._formatter.field_str(i) for i in self._header_title])[2:]
        mat_string += "\n"
        header_data = self._header
        header_data[0] = mat_id
        header_data[1] = density
        mat_string += self._formatter.field_int(header_data[0])
        mat_string += "".join([self._formatter.field_float(i) for i in header_data[1:]])
        mat_string += "\n"
        curve_obj = _DefineCurve(self._model, self._card_format)
        curve_id, curve_card = curve_obj.write_uniaxial_data_curve_card(
            mat_id, mat_name, all_mat_props['UNIAXIAL TEST DATA']
        )
        self._data_line['D1_DATA'][3] = curve_id
        mat_string += (
            "$#" + "".join([self._formatter.field_str(i) for i in self._data_line['D1_TITLE']])[2:]
        )
        mat_string += "\n"
        mat_string += "".join(
            [self._formatter.field_float(i) for i in self._data_line['D1_DATA'][:3]]
        )
        mat_string += self._formatter.field_int(self._data_line['D1_DATA'][3])
        mat_string += "".join(
            [self._formatter.field_float(i) for i in self._data_line['D1_DATA'][4:]]
        )
        mat_string += "\n"
        mat_string += (
            "$#" + "".join([self._formatter.field_str(i) for i in self._data_line['D2_TITLE']])[2:]
        )
        mat_string += "\n"
        mat_string += self._formatter.field_int(self._data_line['D2_DATA'][0])
        mat_string += "".join(
            [self._formatter.field_float(i) for i in self._data_line['D2_DATA'][1:3]]
        )
        mat_string += self._formatter.field_int(self._data_line['D2_DATA'][3])
        mat_string += "".join(
            [self._formatter.field_float(i) for i in self._data_line['D2_DATA'][4:]]
        )
        mat_string += "\n"
        mat_string += curve_card
        return mat_string


class _MatLowDensityFoam:
    __slots__ = (
        '_card_format',
        '_formatter',
        '_format_map',
        '_header_title',
        '_header',
        '_data_line',
        '_model',
        '_logger',
    )

    def __init__(self, model: prime.Model, card_format="SHORT"):
        self._card_format = card_format
        self._formatter = _FormatDynaCards(self._card_format)
        self._format_map = {"SHORT": 10, "LONG": 20}
        self._header_title = ["mid", "ro", "e", "lcid", "tc", "hu", "beta", "damp"]
        self._header = [1, 1.000e-09, 2.0, 0, 0.2, 1.0, 0.0, 0.1]
        self._data_line = {
            "D1_TITLE": ["shape", "fail", "bvflag", "ed", "beta1", "kcon", "ref"],
            "D1_DATA": [1.0, 0.0, 0.0, 0.0, 0.0, 1000.0, 0.0],
        }
        self._model = model
        self._logger = model.python_logger

    def write_low_density_foam(self, mat_id, mat_name, all_mat_props, density=1e-9):
        mat_string = ""
        mat_string += "*MAT_LOW_DENSITY_FOAM_TITLE\n"
        mat_string += f"{mat_name}\n"
        mat_string += "$#" + "".join([self._formatter.field_str(i) for i in self._header_title])[2:]
        mat_string += "\n"
        curve_obj = _DefineCurve(self._model, self._card_format)
        curve_id, curve_card = curve_obj.write_uniaxial_data_curve_card_for_low_density_foam(
            mat_id, mat_name, all_mat_props['UNIAXIAL TEST DATA']
        )
        header_data = self._header
        header_data[0] = mat_id
        header_data[1] = density
        header_data[3] = curve_id
        mat_string += self._formatter.field_int(header_data[0])
        mat_string += self._formatter.field_float(header_data[1])
        mat_string += self._formatter.field_float(header_data[2])
        mat_string += self._formatter.field_int(header_data[3])
        mat_string += "".join([self._formatter.field_float(i) for i in header_data[4:]])
        mat_string += "\n"
        mat_string += (
            "$#" + "".join([self._formatter.field_str(i) for i in self._data_line['D1_TITLE']])[2:]
        )
        mat_string += "\n"
        mat_string += "".join([self._formatter.field_float(i) for i in self._data_line['D1_DATA']])
        mat_string += "\n"
        mat_string += curve_card
        return mat_string


class _MatViscoelasticHillFoam:
    __slots__ = (
        '_card_format',
        '_formatter',
        '_format_map',
        '_header_title',
        '_header',
        '_data_line',
        '_model',
        '_logger',
    )

    def __init__(self, model: prime.Model, card_format="SHORT"):
        self._card_format = card_format
        self._formatter = _FormatDynaCards(self._card_format)
        self._format_map = {"SHORT": 10, "LONG": 20}
        self._header_title = ["mid", "ro", "k", "n", "nu", "lcid", "fittype", "lcsr"]
        self._header = [1, 1.000e-09, 0.0, 0.0, 0.0, 0, 1, 0]
        self._data_line = {
            "D1_TITLE": ["lcve", "nt", "gstart"],
            "D1_DATA": [0, 6.0, 1.0],
            "D2_TITLE": ["c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8"],
            "D2_DATA": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            "D3_TITLE": ["b1", "b2", "b3", "b4", "b5", "b6", "b7", "b8"],
            "D3_DATA": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        }
        self._model = model
        self._logger = model.python_logger

    # def get_formatted_string(self, data_list):
    # length = self._format_map[self._card_format]
    # temp_str = ""
    # for data in data_list:
    # data_str = f"{data}"
    # temp_str += " " * (length - len(data_str)) + data_str
    # temp_str += "\n"
    # return temp_str

    def define_visco_hill_foam(
        self, mat_id, mat_name, all_mat_props, density=1e-9, weight=1, write_low_density_foam=True
    ):
        mat_props = all_mat_props['HYPERFOAM']
        mat_string = ""
        para_dict = {}
        DYNA_COEFFICIENT = {}
        mu_value = 0
        number_of_coeff = 1
        moduli = "LONG TERM"
        if mat_props["Parameters"]:
            if "MODULI" in mat_props["Parameters"]:
                moduli = mat_props["Parameters"]["MODULI"]
            if "N" in mat_props["Parameters"]:
                number_of_coeff = mat_props["Parameters"]["N"]
            # if "TEST DATA INPUT" in mat_props["Parameters"]:
            # self._logger.warning( f'"TEST DATA INPUT" argument for material "
            # f""{mat_name}" (ID: {mat_id}) is not processed.')
            # return mat_string
        # self._logger.info(f"weight {weight}")
        if "TEST DATA INPUT" not in mat_props["Parameters"]:
            mat_fields = mat_props["Data"]
            if mat_fields:
                for i in range(0, int(number_of_coeff)):
                    # para_list.append(mat_fields[f'f{i}'])
                    DYNA_COEFFICIENT[f"c{i + 1}"] = (
                        weight
                        * 2
                        * float(mat_fields[f"u{i + 1}"][0])
                        / float(mat_fields[f"a{i + 1}"][0])
                    )
                    DYNA_COEFFICIENT[f"b{i + 1}"] = float(mat_fields[f"a{i + 1}"][0])
                    # DYNA_COEFFICIENT[f"D{i + 1}"] = mat_fields[f"n{i + 1}"]
                    mu_value += DYNA_COEFFICIENT[f"c{i + 1}"] * DYNA_COEFFICIENT[f"b{i + 1}"]
                mu_value = 0.5 * mu_value
                k = 2 * mu_value / 3.0
                mat_string += "*MAT_VISCOELASTIC_HILL_FOAM\n"
                mat_string += (
                    "$#" + "".join([self._formatter.field_str(i) for i in self._header_title])[2:]
                )
                mat_string += "\n"
                header_data = self._header
                header_data[0] = mat_id
                header_data[1] = density
                header_data[2] = round(k, 8)
                header_data[3] = 0
                header_data[4] = 0.1
                mat_string += self._formatter.field_int(header_data[0])
                mat_string += self._formatter.field_exp(header_data[1])
                mat_string += self._formatter.field_float(header_data[2])
                mat_string += self._formatter.field_int(header_data[3])
                mat_string += self._formatter.field_float(header_data[4])
                mat_string += "\n"
                current_data_line = self._data_line
                for i in range(1, int(number_of_coeff) + 1):
                    current_data_line["D2_DATA"][i - 1] = (
                        round(DYNA_COEFFICIENT[f"c{i}"], self._format_map[self._card_format])
                        if DYNA_COEFFICIENT[f"c{i}"] is not None
                        else 0.0
                    )
                    current_data_line["D3_DATA"][i - 1] = (
                        round(DYNA_COEFFICIENT[f"b{i}"], self._format_map[self._card_format])
                        if DYNA_COEFFICIENT[f"b{i}"] is not None
                        else 0.0
                    )
                # self._logger.info(current_data_line["D1_DATA"])
                # self._logger.info(current_data_line["D2_DATA"])
                # self._logger.info(current_data_line["D3_DATA"])
                mat_string += (
                    "$#"
                    + "".join(
                        [self._formatter.field_str(i) for i in current_data_line["D1_TITLE"]]
                    )[2:]
                    + "\n"
                )
                mat_string += (
                    "".join([self._formatter.field_float(i) for i in current_data_line["D1_DATA"]])
                    + "\n"
                )
                mat_string += (
                    "$#"
                    + "".join(
                        [self._formatter.field_str(i) for i in current_data_line["D2_TITLE"]]
                    )[2:]
                    + "\n"
                )
                mat_string += (
                    "".join([self._formatter.field_float(i) for i in current_data_line["D2_DATA"]])
                    + "\n"
                )
                mat_string += (
                    "$#"
                    + "".join(
                        [self._formatter.field_str(i) for i in current_data_line["D3_TITLE"]]
                    )[2:]
                    + "\n"
                )
                mat_string += (
                    "".join([self._formatter.field_float(i) for i in current_data_line["D3_DATA"]])
                    + "\n"
                )
        else:
            if write_low_density_foam:
                simplified_foam = _MatLowDensityFoam(self._model, self._card_format)
                mat_string += simplified_foam.write_low_density_foam(
                    mat_id, mat_name, all_mat_props, density=density
                )
            else:
                simplified_foam = _MatSimplifiedRubberFoam(self._model, self._card_format)
                mat_string += simplified_foam.write_simplified_rubber_foam(
                    mat_id, mat_name, all_mat_props, density=density
                )
        return mat_string


class _MatPiecewiseLinearPlasticity:
    __slots__ = (
        '_card_format',
        '_data_dict',
        '_formatter',
        '_format_map',
        '_header_title',
        '_header',
        '_data_line',
        '_model',
        '_logger',
    )

    def __init__(self, model: prime.Model, card_format="SHORT"):
        self._card_format = card_format
        self._data_dict = {}
        self._formatter = _FormatDynaCards(self._card_format)
        self._format_map = {"SHORT": 10, "LONG": 20}
        self._header_title = ["mid", "ro", "e", "pr", "sigy", "etan", "-", "-"]
        self._header = [1, 1.000e-09, 0.0, 0.0, 0.0, 0.0, 1.0e20, 0.0]
        self._data_line = {
            "D1_TITLE": [],
            "D1_DATA": [0.0, 0.0, 0, " ", 1.0],
            "D2_TITLE": [],
            "D2_DATA": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            "D3_TITLE": [],
            "D3_DATA": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        }
        self._model = model
        self._logger = model.python_logger

    def write_piecewise_linear_plasticity(
        self,
        all_mat_props,
        mat_name,
        mat_id,
        e,
        pr,
        sigy,
        etan,
        density,
        material_used_with_shell=False,
        max_id=0,
    ):
        mat_string = ""
        mat_string += "*MAT_PIECEWISE_LINEAR_PLASTICITY_TITLE\n"
        mat_string += f"{mat_name}\n"
        mat_string += "$#" + "".join([self._formatter.field_str(i) for i in self._header_title])[2:]
        mat_string += "\n"
        curve_obj = _DefineCurve(self._model, self._card_format)
        curve_id, curve_card, sigy = curve_obj.write_plastic_curve_card(
            mat_id, mat_name, all_mat_props['PLASTIC']
        )
        header_data = self._header
        header_data[0] = mat_id
        header_data[1] = density
        header_data[2] = e
        header_data[3] = pr
        header_data[4] = sigy
        header_data[5] = etan
        mat_string += self._formatter.field_int(header_data[0])
        mat_string += "".join([self._formatter.field_float(i) for i in header_data[1:]])
        mat_string += "\n"
        self._data_line['D1_DATA'][2] = curve_id
        mat_string += (
            "$#" + "".join([self._formatter.field_str(i) for i in self._data_line['D1_TITLE']])[2:]
        )
        mat_string += "\n"
        mat_string += "".join(
            [self._formatter.field_float(i) for i in self._data_line['D1_DATA'][:2]]
        )
        mat_string += self._formatter.field_int(self._data_line['D1_DATA'][2])
        mat_string += self._formatter.field_str(self._data_line['D1_DATA'][3])
        mat_string += "".join(
            [self._formatter.field_float(i) for i in self._data_line['D1_DATA'][4:]]
        )
        mat_string += "\n"
        mat_string += (
            "$#"
            + "".join([self._formatter.field_str(i) for i in self._data_line["D2_TITLE"]])[2:]
            + "\n"
        )
        mat_string += (
            "".join([self._formatter.field_float(i) for i in self._data_line["D2_DATA"]]) + "\n"
        )
        mat_string += (
            "$#"
            + "".join([self._formatter.field_str(i) for i in self._data_line["D3_TITLE"]])[2:]
            + "\n"
        )
        mat_string += (
            "".join([self._formatter.field_float(i) for i in self._data_line["D3_DATA"]]) + "\n"
        )
        str_2d = ''
        if material_used_with_shell:
            str_2d = mat_string.replace(
                "*MAT_PIECEWISE_LINEAR_PLASTICITY_TITLE",
                "*MAT_PIECEWISE_LINEAR_PLASTICITY_2D_TITLE",
            ).replace(
                self._formatter.field_int(mat_id), self._formatter.field_int(max_id * 3 + mat_id)
            )
        mat_string += curve_card
        return mat_string + str_2d


class _MatFabric:
    __slots__ = (
        '_card_format',
        '_data_dict',
        '_formatter',
        '_format_map',
        '_header_title',
        '_header',
        '_data_line',
        '_model',
        '_logger',
    )

    def __init__(self, model: prime.Model, card_format="SHORT"):
        self._card_format = card_format
        self._data_dict = {}
        self._formatter = _FormatDynaCards(self._card_format)
        self._format_map = {"SHORT": 10, "LONG": 20}
        self._header_title = ["mid", "ro", "ea", "eb", "-", "prba", "prab", "-"]
        self._header = [1, 1.000e-09, 210000.0, 0.0, " ", 0.29, 0.0, " "]
        self._data_line = {
            "D1_TITLE": ["gab", "-", "-", "cse", "el", "prl", "lratio", "damp"],
            "D1_DATA": [0.0, " ", " ", 0.0, 0.0, 0.0, 0.0, 0.05],
            "D2_TITLE": ["aopt", "flc", "fac", "ela", "inrc", "form", "fvopt", "tsrfac"],
            "D2_DATA": [0.0, 0.0, 0.0, 0.0, 0.0, -14, 0, 0.0],
            "D3_TITLE": ["unused", "rgbrth", "a0ref", "a1", "a2", "a3", "x0", "x1"],
            "D3_DATA": [" ", 0.0, 0, 0.0, 0.0, 0.0, 0.0, 0.0],
            "D4_TITLE": ["v1", "v2", "v3", "-", "-", "-", "beta", "isrefg"],
            "D4_DATA": [0.0, 0.0, 0.0, " ", " ", " ", 0.0, 0],
            "D5_TITLE": ["lca", "lcb", "lcab", "lcua", "lcub", "lcuab", "rl"],
            "D5_DATA": [0, 0, 0, 0, 0, 0, 0.0],
            "D6_TITLE": ["lcaa", "lcbb", "h", "dt", "-", "ecoat", "scoat", "tcoat"],
            "D6_DATA": [0, 0, 0.0, 0, 0, 2000, 10.0, -0.07],
        }
        self._model = model
        self._logger = model.python_logger

    def write_mat_fabric(
        self,
        mat_name,
        mat_id,
        nu,
        density,
        max_id=0,
    ):
        mat_string = ""
        mat_string += "*MAT_FABRIC_TITLE\n"
        mat_string += f"{mat_name}_FABRIC\n"
        mat_string += "$#" + "".join([self._formatter.field_str(i) for i in self._header_title])[2:]
        mat_string += "\n"

        header_data = self._header
        header_data[0] = max_id * 3 + mat_id
        header_data[1] = density
        header_data[5] = nu
        mat_string += self._formatter.field_int(header_data[0])
        mat_string += "".join([self._formatter.field_float(i) for i in header_data[1:]])
        mat_string += "\n"
        mat_string += (
            "$#"
            + "".join([self._formatter.field_str(i) for i in self._data_line['D1_TITLE']])[2:]
            + "\n"
        )
        mat_string += (
            "".join([self._formatter.field_str(str(i)) for i in self._data_line["D1_DATA"]]) + "\n"
        )
        mat_string += (
            "$#"
            + "".join([self._formatter.field_str(i) for i in self._data_line["D2_TITLE"]])[2:]
            + "\n"
        )
        mat_string += (
            "".join([self._formatter.field_str(str(i)) for i in self._data_line["D2_DATA"]]) + "\n"
        )
        mat_string += (
            "$#"
            + "".join([self._formatter.field_str(i) for i in self._data_line["D3_TITLE"]])[2:]
            + "\n"
        )
        mat_string += (
            "".join([self._formatter.field_str(str(i)) for i in self._data_line["D3_DATA"]]) + "\n"
        )
        mat_string += (
            "$#"
            + "".join([self._formatter.field_str(i) for i in self._data_line['D4_TITLE']])[2:]
            + "\n"
        )
        mat_string += (
            "".join([self._formatter.field_str(str(i)) for i in self._data_line["D4_DATA"]]) + "\n"
        )
        mat_string += (
            "$#"
            + "".join([self._formatter.field_str(i) for i in self._data_line["D5_TITLE"]])[2:]
            + "\n"
        )
        mat_string += (
            "".join([self._formatter.field_str(str(i)) for i in self._data_line["D5_DATA"]]) + "\n"
        )
        mat_string += (
            "$#"
            + "".join([self._formatter.field_str(i) for i in self._data_line["D6_TITLE"]])[2:]
            + "\n"
        )
        mat_string += (
            "".join([self._formatter.field_str(str(i)) for i in self._data_line["D6_DATA"]]) + "\n"
        )

        return mat_string


class _CohesiveMaterialMapper:
    __slots__ = (
        '_card_format',
        '_data_dict',
        '_formatter',
        '_format_map',
        '_damage_length',
        '_fracture_energy',
        '_curve_id',
        '_strain_at_dmg_ini',
        '_strs_tria',
        '_strn_rate',
        '_dyna_commands',
        '_en',
        '_es1',
        '_es2',
        '_d_type',
        '_model',
        '_logger',
    )

    def __init__(self, model: prime.Model, card_format="SHORT"):
        self._card_format = card_format
        self._data_dict = {}
        self._formatter = _FormatDynaCards(self._card_format)
        self._format_map = {"SHORT": 10, "LONG": 20}
        self._damage_length = 0.0
        self._fracture_energy = 0.0
        self._curve_id = 0
        self._strain_at_dmg_ini = 0.0
        self._strs_tria = 0.0
        self._strn_rate = 0.0
        self._dyna_commands = ""
        self._en = 0.0
        self._es1 = 0.0
        self._es2 = 0.0
        self._d_type = "DISPLACEMENT"
        self._model = model
        self._logger = model.python_logger

    def damage_evolution(self, mat_id, mat_name, all_mat_props):
        dmg_evol_props = all_mat_props["DAMAGE EVOLUTION"]
        params = dmg_evol_props['Parameters']
        degrade = "MAXIMUM"
        softening = "LINEAR"
        d_type = "DISPLACEMENT"
        if "SOFTENING" in params:
            softening = params["SOFTENING"]
        if "DEGRADATION" in params:
            degrade = params["DEGRADATION"]
        if "TYPE" in params:
            d_type = params["TYPE"]
        self._d_type = d_type
        if degrade == "MAXIMUM" and softening == "LINEAR" and d_type == "DISPLACEMENT":
            if "Data" in dmg_evol_props and dmg_evol_props["Data"] is not None:
                str = (
                    f"Effective total or plastic displacement at failure, "
                    f"measured from the time of damage initiation"
                )
                if str in dmg_evol_props["Data"]:
                    self._damage_length = float(dmg_evol_props["Data"][str][0])
        elif degrade == "MAXIMUM" and softening == "LINEAR" and d_type == "ENERGY":
            if "Data" in dmg_evol_props and dmg_evol_props["Data"] is not None:
                if "Fracture energy" in dmg_evol_props["Data"]:
                    self._fracture_energy = float(dmg_evol_props["Data"]["Fracture energy"][0])
        else:
            self._logger.warning(
                f"Warning: Parameter on Damage Evolution (MAT:{mat_name} ID: {mat_id}) "
                f"is not processed. check the material definition"
            )

    def damage_initiation(self, mat_id, mat_name, all_mat_props):
        dmg_ini_props = all_mat_props["DAMAGE INITIATION"]
        params = dmg_ini_props['Parameters']
        criterion = "DUCTILE"
        if "CRITERION" in params:
            criterion = params["CRITERION"]
        if criterion == "DUCTILE":
            if "Data" in dmg_ini_props and dmg_ini_props["Data"] is not None:
                if "Equivalent fracture strain at damage initiation" in dmg_ini_props["Data"]:
                    self._strain_at_dmg_ini = float(
                        dmg_ini_props["Data"]["Equivalent fracture strain at damage initiation"][0]
                    )
                if "Stress triaxiality" in dmg_ini_props["Data"]:
                    self._strs_tria = float(dmg_ini_props["Data"]["Stress triaxiality"][0])
                if "Strain rate" in dmg_ini_props["Data"]:
                    self._strn_rate = float(dmg_ini_props["Data"]["Strain rate"][0])
        elif criterion == "MAXE":
            if "Data" in dmg_ini_props and dmg_ini_props["Data"] is not None:
                str1 = "Nominal strain at damage initiation in a normal-only mode"
                if str1 in dmg_ini_props["Data"]:
                    self._en = float(dmg_ini_props["Data"][str1][0])
                    str2 = (
                        f"Nominal strain at damage initiation in a shear-only mode "
                        f"that involves separation only along the first shear direction"
                    )
                if str2 in dmg_ini_props["Data"]:
                    self._es1 = float(dmg_ini_props["Data"][str2][0])
                str3 = (
                    f"Nominal strain at damage initiation in a shear-only mode "
                    f"that involves separation only along the second shear direction"
                )
                if str3 in dmg_ini_props["Data"]:
                    self._es2 = float(dmg_ini_props["Data"][str3][0])
        else:
            self._logger.warning(
                f"Warning: Parameter on Damage Initiation (MAT:{mat_name} ID: {mat_id}) "
                f"is not processed. check the material definition"
            )

    def get_all_commands(
        self,
        mat_id,
        mat_name,
        all_mat_props,
        e,
        pr,
        sigy,
        etan,
        elastic_type,
        density,
        thickness,
        mat_cohesive_general,
    ):
        mat_string = ""
        if mat_cohesive_general:
            mat_obj = _MatCohesiveGeneral(self._model, self._card_format)
            mat_obj._damage_length = self._damage_length
            mat_obj._fracture_energy = self._fracture_energy
            mat_obj._curve_id = self._curve_id
            mat_obj._strain_at_dmg_ini = self._strain_at_dmg_ini
            mat_obj._strs_tria = self._strs_tria
            mat_obj._strn_rate = self._strn_rate
            mat_obj._dyna_commands = self._dyna_commands
            mat_obj._en = self._en
            mat_obj._es1 = self._es1
            mat_obj._es2 = self._es2
            mat_obj._d_type = self._d_type
            mat_string = mat_obj.get_all_commands(
                mat_id, mat_name, all_mat_props, e, pr, sigy, etan, elastic_type, density, thickness
            )
        else:
            if elastic_type == "ISOTROPIC":
                mat_obj = _MatPlasticityWithDamage(self._model, self._card_format)
                mat_obj._damage_length = self._damage_length
                mat_obj._fracture_energy = self._fracture_energy
                mat_obj._curve_id = self._curve_id
                mat_obj._strain_at_dmg_ini = self._strain_at_dmg_ini
                mat_obj._strs_tria = self._strs_tria
                mat_obj._strn_rate = self._strn_rate
                mat_obj._dyna_commands = self._dyna_commands
                mat_obj._en = self._en
                mat_obj._es1 = self._es1
                mat_obj._es2 = self._es2
                mat_obj._d_type = self._d_type
                mat_string = mat_obj.get_all_commands(
                    mat_id,
                    mat_name,
                    all_mat_props,
                    e,
                    pr,
                    sigy,
                    etan,
                    elastic_type,
                    density,
                    thickness,
                )
            if elastic_type == "TRACTION":
                mat_obj = _MatCohesiveMixedModeElastoplasticRate(self._model, self._card_format)
                mat_obj._damage_length = self._damage_length
                mat_obj._fracture_energy = self._fracture_energy
                mat_obj._curve_id = self._curve_id
                mat_obj._strain_at_dmg_ini = self._strain_at_dmg_ini
                mat_obj._strs_tria = self._strs_tria
                mat_obj._strn_rate = self._strn_rate
                mat_obj._dyna_commands = self._dyna_commands
                mat_obj._en = self._en
                mat_obj._es1 = self._es1
                mat_obj._es2 = self._es2
                mat_obj._d_type = self._d_type
                mat_string = mat_obj.get_all_commands(
                    mat_id,
                    mat_name,
                    all_mat_props,
                    e,
                    pr,
                    sigy,
                    etan,
                    elastic_type,
                    density,
                    thickness,
                )

        return mat_string


class _MatPlasticityWithDamage:
    __slots__ = (
        '_section_thickness',
        '_card_format',
        '_data_dict',
        '_formatter',
        '_format_map',
        '_header_title',
        '_header',
        '_data_line',
        '_damage_length',
        '_fracture_energy',
        '_curve_id',
        '_strain_at_dmg_ini',
        '_strs_tria',
        '_strn_rate',
        '_dyna_commands',
        '_en',
        '_es1',
        '_es2',
        '_d_type',
        '_model',
        '_logger',
    )

    def __init__(self, model: prime.Model, card_format="SHORT"):
        self._section_thickness = 0.1
        self._card_format = card_format
        self._data_dict = {}
        self._formatter = _FormatDynaCards(self._card_format)
        self._format_map = {"SHORT": 10, "LONG": 20}
        self._header_title = ["mid", "ro", "e", "pr", "sigy", "etan", "eppf", "tdel"]
        self._header = [1, 1e-9, 0.0, 0.0, 0.0, 0, 0.0, 0.0]
        self._data_line = {
            "D1_TITLE": ["c", "p", "lcss", "lcsr", "eppfr", "vp", "lcdm", "numint"],
            "D1_DATA": [0.0, 0.0, 0, 0, 0.0, 0.0, 0.0, 0.0],
            "D2_TITLE": ["eps1", "eps2", "eps3", "eps4", "eps5", "eps6", "eps7", "eps8"],
            "D2_DATA": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            "D3_TITLE": ["es1", "es2", "es3", "es4", "es5", "es6", "es7", "es8"],
            "D3_DATA": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        }
        self._damage_length = 0.0
        self._fracture_energy = 0.0
        self._curve_id = 0
        self._strain_at_dmg_ini = 0.0
        self._strs_tria = 0.0
        self._strn_rate = 0.0
        self._dyna_commands = ""
        self._en = 0.0
        self._es1 = 0.0
        self._es2 = 0.0
        self._d_type = "DISPLACEMENT"
        self._model = model
        self._logger = model.python_logger

    def get_all_commands(
        self, mat_id, mat_name, all_mat_props, e, pr, sigy, etan, elastic_type, density, thickness
    ):
        self._section_thickness = thickness
        mat_string = ""
        mat_string += "*MAT_PLASTICITY_WITH_DAMAGE_TITLE\n"
        mat_string += f"{mat_name}\n"
        mat_string += "$#" + "".join([self._formatter.field_str(i) for i in self._header_title])[2:]
        mat_string += "\n"
        curve_obj = _DefineCurve(self._model, self._card_format)
        curve_id = 0
        curve_card = ""
        if "PLASTIC" in all_mat_props:
            curve_id, curve_card, sigy = curve_obj.write_plastic_curve_card(
                mat_id, mat_name, all_mat_props['PLASTIC']
            )
        gic = 0.0
        giic = 0.0
        curve_id_1 = 0
        t = 0.0
        eppf = self._strain_at_dmg_ini
        eppfr = self._damage_length + self._strain_at_dmg_ini
        header_data = self._header
        header_data[0] = mat_id
        header_data[1] = density
        header_data[2] = e
        header_data[3] = pr
        header_data[5] = etan
        header_data[6] = eppf
        self._data_line['D1_DATA'][2] = curve_id
        self._data_line['D1_DATA'][4] = eppfr
        mat_string += self._formatter.field_int(header_data[0])
        mat_string += "".join([self._formatter.field_float(i) for i in header_data[1:]])
        mat_string += "\n"
        mat_string += (
            "$#" + "".join([self._formatter.field_str(i) for i in self._data_line['D1_TITLE']])[2:]
        )
        mat_string += "\n"
        mat_string += self._formatter.field_float(self._data_line['D1_DATA'][0])
        mat_string += self._formatter.field_float(self._data_line['D1_DATA'][1])
        mat_string += self._formatter.field_int(self._data_line['D1_DATA'][2])
        mat_string += self._formatter.field_int(self._data_line['D1_DATA'][3])
        mat_string += "".join(
            [self._formatter.field_float(i) for i in self._data_line['D1_DATA'][4:]]
        )
        mat_string += "\n"
        mat_string += (
            "$#" + "".join([self._formatter.field_str(i) for i in self._data_line['D2_TITLE']])[2:]
        )
        mat_string += "\n"
        mat_string += "".join([self._formatter.field_float(i) for i in self._data_line['D2_DATA']])
        mat_string += "\n"
        mat_string += (
            "$#" + "".join([self._formatter.field_str(i) for i in self._data_line['D3_TITLE']])[2:]
        )
        mat_string += "\n"
        mat_string += "".join([self._formatter.field_float(i) for i in self._data_line['D3_DATA']])
        mat_string += "\n"
        mat_string += curve_card
        return mat_string


class _MatCohesiveMixedModeElastoplasticRate:
    __slots__ = (
        '_section_thickness',
        '_card_format',
        '_data_dict',
        '_formatter',
        '_format_map',
        '_header_title',
        '_header',
        '_data_line',
        '_damage_length',
        '_fracture_energy',
        '_curve_id',
        '_strain_at_dmg_ini',
        '_strs_tria',
        '_strn_rate',
        '_dyna_commands',
        '_en',
        '_es1',
        '_es2',
        '_d_type',
        '_model',
        '_logger',
    )

    def __init__(self, model: prime.Model, card_format="SHORT"):
        self._section_thickness = 0.1
        self._card_format = card_format
        self._data_dict = {}
        self._formatter = _FormatDynaCards(self._card_format)
        self._format_map = {"SHORT": 10, "LONG": 20}
        self._header_title = ["mid", "ro", "-", "-", "-", "-", "-", "-"]
        self._header = [1, 1e-9, 0.0, 4.0, 0.0, 0.0, 0.0, 1.0]
        self._data_line = {
            "D1_TITLE": ["-", "-", "-", "-", "-", "-", "-", "-"],
            "D1_DATA": [0.0, 0.0, 0, 0, 0.0, 0.0, 0.0, 0],
            "D2_TITLE": ["-", "-", "-", "-", "-", "-", "-", "-"],
            "D2_DATA": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0],
        }
        self._damage_length = 0.0
        self._fracture_energy = 0.0
        self._curve_id = 0
        self._strain_at_dmg_ini = 0.0
        self._strs_tria = 0.0
        self._strn_rate = 0.0
        self._dyna_commands = ""
        self._en = 0.0
        self._es1 = 0.0
        self._es2 = 0.0
        self._d_type = "DISPLACEMENT"
        self._model = model
        self._logger = model.python_logger

    def get_all_commands(
        self, mat_id, mat_name, all_mat_props, kn, ks1, ks2, etan, elastic_type, density, thickness
    ):
        self._section_thickness = thickness
        mat_string = ""
        curve_card_1 = ""
        curve_card_2 = ""
        mat_string += "*MAT_COHESIVE_MIXED_MODE_ELASTOPLASTIC_RATE_TITLE\n"
        mat_string += f"{mat_name}\n"
        mat_string += "$#" + "".join([self._formatter.field_str(i) for i in self._header_title])[2:]
        mat_string += "\n"
        curve_obj = _DefineCurve(self._model, self._card_format)
        gic = 0.0
        giic = 0.0

        gic = (
            kn * self._en * self._en / 2 + self._fracture_energy * 0.1
        )  # this factor is as per the suggestion
        giic = ks1 * self._es1 * self._es1 / 2 + self._fracture_energy
        t = kn * self._en
        s = ks1 * self._es1

        curve_id_1, curve_card_1 = curve_obj.create_damage_curve_for_cohesive_mixed_mode(
            mat_id, "GIC " + mat_name, self._section_thickness, gic
        )
        curve_id_2, curve_card_2 = curve_obj.create_damage_curve_for_cohesive_mixed_mode(
            mat_id, "GIIC " + mat_name, self._section_thickness, giic
        )

        header_data = self._header
        header_data[0] = mat_id
        header_data[1] = density
        header_data[4] = kn
        header_data[5] = ks1
        header_data[6] = self._section_thickness

        mat_string += self._formatter.field_int(header_data[0])
        mat_string += "".join([self._formatter.field_float(i) for i in header_data[1:]])
        mat_string += "\n"

        self._data_line['D1_DATA'][0] = gic
        self._data_line['D1_DATA'][3] = t
        self._data_line['D1_DATA'][7] = curve_id_1
        mat_string += (
            "$#" + "".join([self._formatter.field_str(i) for i in self._data_line['D1_TITLE']])[2:]
        )
        mat_string += "\n"
        mat_string += "".join(
            [self._formatter.field_float(i) for i in self._data_line['D1_DATA'][:7]]
        )
        mat_string += self._formatter.field_int(self._data_line['D1_DATA'][7])
        mat_string += "\n"
        self._data_line['D2_DATA'][0] = giic
        self._data_line['D2_DATA'][3] = s
        self._data_line['D2_DATA'][7] = curve_id_2
        mat_string += (
            "$#" + "".join([self._formatter.field_str(i) for i in self._data_line['D2_TITLE']])[2:]
        )
        mat_string += "\n"
        mat_string += "".join(
            [self._formatter.field_float(i) for i in self._data_line['D2_DATA'][:7]]
        )
        mat_string += self._formatter.field_int(self._data_line['D2_DATA'][7])
        mat_string += "\n"
        mat_string += curve_card_1
        mat_string += curve_card_2

        return mat_string


class _MatCohesiveGeneral:
    __slots__ = (
        '_section_thickness',
        '_card_format',
        '_data_dict',
        '_formatter',
        '_format_map',
        '_header_title',
        '_header',
        '_data_line',
        '_damage_length',
        '_fracture_energy',
        '_curve_id',
        '_strain_at_dmg_ini',
        '_strs_tria',
        '_strn_rate',
        '_dyna_commands',
        '_en',
        '_es1',
        '_es2',
        '_d_type',
        '_model',
        '_logger',
    )

    def __init__(self, model: prime.Model, card_format="SHORT"):
        self._section_thickness = 0.1
        self._card_format = card_format
        self._data_dict = {}
        self._formatter = _FormatDynaCards(self._card_format)
        self._format_map = {"SHORT": 10, "LONG": 20}
        self._header_title = ["mid", "ro", "roflg", "intfail", "tes", "tslc", "gic", "giic"]
        self._header = [1, 1e-9, 0.0, 0.0, 0.0, 0, 0.0, 0.0]
        self._data_line = {
            "D1_TITLE": ['xmu', 't', 's', 'stfsf', 'tslc2'],
            "D1_DATA": [1.0, 0.0, 0.0, 0.0, 0],
        }
        self._damage_length = 0.0
        self._fracture_energy = 0.0
        self._curve_id = 0
        self._strain_at_dmg_ini = 0.0
        self._strs_tria = 0.0
        self._strn_rate = 0.0
        self._dyna_commands = ""
        self._en = 0.0
        self._es1 = 0.0
        self._es2 = 0.0
        self._d_type = "DISPLACEMENT"
        self._model = model
        self._logger = model.python_logger

    def get_all_commands(
        self, mat_id, mat_name, all_mat_props, kn, ks1, ks2, etan, elastic_type, density, thickness
    ):
        self._section_thickness = thickness
        mat_string = ""
        curve_card_1 = ""
        curve_card_2 = ""
        mat_string += "*MAT_COHESIVE_GENERAL_TITLE\n"
        mat_string += f"{mat_name}\n"
        mat_string += "$#" + "".join([self._formatter.field_str(i) for i in self._header_title])[2:]
        mat_string += "\n"
        curve_obj = _DefineCurve(self._model, self._card_format)
        gic = 0.0
        giic = 0.0
        curve_id_1 = 0
        t = 0.0
        if elastic_type == "ISOTROPIC":
            if "PLASTIC" in all_mat_props:
                curve_id_1, curve_card_1, gic, t = curve_obj.create_damage_normalized_curve(
                    mat_id,
                    mat_name,
                    young=kn,
                    damage_len=self._damage_length,
                    curve_data=all_mat_props["PLASTIC"],
                    thickness=self._section_thickness,
                )
            curve_id_2, curve_card_2 = "", ""
        elif elastic_type == "TRACTION":
            curve_id_1, curve_card_1 = curve_obj.create_damage_curve_for_traction(
                mat_id,
                mat_name + " T",
                k=kn,
                e=self._en,
                fe=self._fracture_energy,
                thickness=self._section_thickness,
            )
            curve_id_2, curve_card_2 = curve_obj.create_damage_curve_for_traction(
                mat_id,
                mat_name + " S",
                k=ks1,
                e=self._es1,
                fe=self._fracture_energy,
                thickness=self._section_thickness,
            )
            gic = kn * self._en * self._en / 2 + self._fracture_energy
            giic = ks1 * self._es1 * self._es1 / 2 + self._fracture_energy
        header_data = self._header
        header_data[0] = mat_id
        header_data[1] = density
        header_data[5] = curve_id_1
        header_data[6] = gic
        header_data[7] = giic
        mat_string += self._formatter.field_int(header_data[0])
        mat_string += "".join([self._formatter.field_float(i) for i in header_data[1:5]])
        mat_string += self._formatter.field_int(header_data[5])
        mat_string += "".join([self._formatter.field_float(i) for i in header_data[6:]])
        mat_string += "\n"
        if elastic_type == "ISOTROPIC":
            self._data_line['D1_DATA'][1] = t
            self._data_line['D1_DATA'][2] = 0.0
        elif elastic_type == "TRACTION":
            self._data_line['D1_DATA'][1] = kn * self._en
            self._data_line['D1_DATA'][2] = ks1 * self._es1
        self._data_line['D1_DATA'][4] = curve_id_2
        mat_string += (
            "$#" + "".join([self._formatter.field_str(i) for i in self._data_line['D1_TITLE']])[2:]
        )
        mat_string += "\n"
        mat_string += "".join(
            [self._formatter.field_float(i) for i in self._data_line['D1_DATA'][:4]]
        )
        if curve_id_2 != "":
            mat_string += self._formatter.field_int(self._data_line['D1_DATA'][4])
        else:
            mat_string += self._formatter.field_str(self._data_line['D1_DATA'][4])
        mat_string += "\n"
        mat_string += curve_card_1
        mat_string += curve_card_2

        return mat_string


class _MatAddDamageDiem:
    __slots__ = (
        '_card_format',
        '_data_dict',
        '_formatter',
        '_format_map',
        '_header_title',
        '_header',
        '_data_line',
        '_damage_length',
        '_curve_id',
        '_strain_at_dmg_ini',
        '_strs_tria',
        '_strn_rate',
        '_dyna_commands',
        '_model',
        '_logger',
    )

    def __init__(self, model: prime.Model, card_format="SHORT"):
        self._card_format = card_format
        self._data_dict = {}
        self._formatter = _FormatDynaCards(self._card_format)
        self._format_map = {"SHORT": 10, "LONG": 20}
        self._header_title = ["mid", "ndiemc", "dinit", "deps", "numfjp"]
        self._header = [1, 1.0, 0.0, 0.00001, 5]
        self._data_line = {
            "D1_TITLE": ['dityp', 'p1', 'p2', 'p3', 'p4', 'p5'],
            "D1_DATA": [0.0, 0, 0.0, 0.0, 1.0, 0.0],
            "D2_TITLE": ['detyp', 'dctyp', 'q1', 'q2', 'q3', 'q4'],
            "D2_DATA": [0.0, 0.0, 0.0, 1.0, 0.0, 0.0],
        }
        self._damage_length = 0.0
        self._curve_id = 1
        self._strain_at_dmg_ini = 0.0
        self._strs_tria = 0.0
        self._strn_rate = 0.0
        self._dyna_commands = ""
        self._model = model
        self._logger = model.python_logger

    def damage_evolution(self, mat_id, mat_name, all_mat_props):
        dmg_evol_props = all_mat_props["DAMAGE EVOLUTION"]
        params = dmg_evol_props['Parameters']
        degrade = "MAXIMUM"
        softening = "LINEAR"
        d_type = "DISPLACEMENT"
        if "SOFTENING" in params:
            softening = params["SOFTENING"]
        if "DEGRADATION" in params:
            degrade = params["DEGRADATION"]
        if "TYPE" in params:
            d_type = params["TYPE"]
        if degrade != "MAXIMUM" or softening != "LINEAR" or d_type != "DISPLACEMENT":
            self._logger.warning(
                f"Warning: Parameter on Damage Evolution (MAT:{mat_name} ID: {mat_id}) "
                f"is not processed. check the material definition"
            )
        if "Data" in dmg_evol_props and dmg_evol_props["Data"] is not None:
            str = (
                f"Effective total or plastic displacement at failure, "
                f"measured from the time of damage initiation"
            )
            if str in dmg_evol_props["Data"]:
                self._damage_length = dmg_evol_props["Data"][str][0]

    def damage_initiation(self, mat_id, mat_name, all_mat_props):
        dmg_ini_props = all_mat_props["DAMAGE INITIATION"]
        params = dmg_ini_props['Parameters']
        criterion = "DUCTILE"
        if "CRITERION" in params:
            criterion = params["CRITERION"]
        if criterion != "DUCTILE":
            self._logger.warning(
                f"Warning: Parameter on Damage Initiation (MAT:{mat_name} ID: {mat_id}) "
                f"is not processed. check the material definition"
            )
        if "Data" in dmg_ini_props and dmg_ini_props["Data"] is not None:
            if "Equivalent fracture strain at damage initiation" in dmg_ini_props["Data"]:
                self._strain_at_dmg_ini = dmg_ini_props["Data"][
                    "Equivalent fracture strain at damage initiation"
                ][0]
            if "Stress triaxiality" in dmg_ini_props["Data"]:
                self._strs_tria = dmg_ini_props["Data"]["Stress triaxiality"][0]
            if "Strain rate" in dmg_ini_props["Data"]:
                self._strn_rate = dmg_ini_props["Data"]["Strain rate"][0]

    def get_all_commands(self, mat_id, mat_name, all_mat_props, material_used_with_shell, max_id):
        mat_string = ""
        mat_string += "*MAT_ADD_DAMAGE_DIEM_TITLE\n"
        mat_string += f"{mat_name}\n"
        mat_string += "$#" + "".join([self._formatter.field_str(i) for i in self._header_title])[2:]
        mat_string += "\n"
        curve_obj = _DefineCurve(self._model, self._card_format)
        curve_id, curve_card = curve_obj.write_damage_curve(
            mat_id, mat_name, [self._strs_tria, self._strain_at_dmg_ini]
        )
        header_data = self._header
        header_data[0] = mat_id
        mat_string += self._formatter.field_int(header_data[0])
        mat_string += "".join([self._formatter.field_float(i) for i in header_data[1:4]])
        mat_string += self._formatter.field_int(header_data[4])
        mat_string += "\n"
        self._data_line['D1_DATA'][1] = curve_id
        mat_string += (
            "$#" + "".join([self._formatter.field_str(i) for i in self._data_line['D1_TITLE']])[2:]
        )
        mat_string += "\n"
        mat_string += self._formatter.field_float(self._data_line['D1_DATA'][0])
        mat_string += self._formatter.field_int(self._data_line['D1_DATA'][1])
        mat_string += "".join(
            [self._formatter.field_float(i) for i in self._data_line['D1_DATA'][2:]]
        )
        mat_string += "\n"
        self._data_line['D2_DATA'][2] = self._damage_length
        mat_string += (
            "$#"
            + "".join([self._formatter.field_str(i) for i in self._data_line["D2_TITLE"]])[2:]
            + "\n"
        )
        mat_string += (
            "".join([self._formatter.field_float(i) for i in self._data_line["D2_DATA"]]) + "\n"
        )

        if self._damage_length == 0.0 and self._strain_at_dmg_ini == 0.0 and self._strs_tria == 0.0:
            return ""
        else:
            str_2d = ""
            if material_used_with_shell:
                str_2d = mat_string.replace(
                    self._formatter.field_int(mat_id),
                    self._formatter.field_int(max_id * 3 + mat_id),
                )
            return mat_string + str_2d + curve_card


class _MatAddInelasticity:
    __slots__ = (
        '_card_format',
        '_data_dict',
        '_formatter',
        '_format_map',
        '_header_title',
        '_header',
        '_data_line',
        '_neilinks',
        '_neilinks_count',
        '_model',
        '_logger',
    )

    def __init__(self, model: prime.Model, card_format="SHORT"):
        self._card_format = card_format
        self._data_dict = {}
        self._neilinks = 1
        self._formatter = _FormatDynaCards(self._card_format)
        self._format_map = {"SHORT": 10, "LONG": 20}
        self._header_title = ["mid", "nielinks", "-", "-", "-", "aopt", "macf", "beta"]
        self._header = [1, 1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        self._data_line = {
            "D1_TITLE": ["nielaws", "weight"],
            "D1_DATA": [1, 0],
            "D2_TITLE": ["law", "model"],
            "D2_DATA": [6, 1],
            "D3_TITLE": ["p1", "p2", "-", "-", "-", "-", "-"],
            "D3_DATA": [1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        }
        self._model = model
        self._logger = model.python_logger

    def neilinks(self, count):
        self._neilinks_count = count

    # def get_formatted_string(self,data_list):
    # length = self._format_map[self._card_format]
    # temp_str = ""
    # for data in data_list:
    # data_str = f"{data}"
    # temp_str += " "* (length - len(data_str)) + data_str
    # temp_str+="\n"
    # return temp_str

    def get_weight_factor(self, mat_id, mat_name, all_mat_props):
        weight_sum = 0
        mat_props = all_mat_props["VISCOELASTIC"]
        if (
            mat_props["Parameters"]
            and "TIME" in mat_props["Parameters"]
            and mat_props["Parameters"]["TIME"] == "PRONY"
        ):
            g = mat_props["Data"]['g']
            if 'k' in mat_props["Data"]:
                k = mat_props["Data"]['k']
            else:
                k = [0.0] * len(g)
            t = mat_props["Data"]['t']
            plastic_data = {}
            for pnt in zip(g, k, t):
                if float(pnt[1]) in plastic_data.keys():
                    plastic_data[float(pnt[1])].append([float(pnt[0]), float(pnt[2])])
                else:
                    plastic_data[float(pnt[1])] = [[float(pnt[0]), float(pnt[2])]]
            max_data_lines = 0
            if len(plastic_data.keys()) > 1:
                self._logger.warning(
                    f"More than one temperature data is provided in the material "
                    f"(ID : {mat_id} Name: {mat_name}). Please verify the material data."
                )
            for tb_temp, data_temp in plastic_data.items():
                data_lines_length = len(data_temp)
                if data_lines_length > max_data_lines:
                    max_data_lines = data_lines_length
                data_for_temp = sorted(data_temp, key=lambda x: x[0])
                for count, plst_data in enumerate(data_for_temp):
                    weight_sum += float(plst_data[0])
                    self._data_dict[f"D{count + 1}_Weight"] = plst_data[0]
                    self._data_dict[f"D{count + 1}_P1"] = 1 / plst_data[1]
                self._neilinks = count + 1
            if weight_sum > 1:
                self._logger.warning(
                    f"Weight sum of the hyperleastic material {mat_name} is more than 1"
                )
            weight_factor = 1 / (1 - weight_sum)
            # self._logger.info(f"weight_factor1 {weight_factor}")
            return weight_factor
        else:
            self._logger.warning(
                f"The visco-elasticity available in the material "
                f"(ID : {mat_id} Name: {mat_name}) is not translated. "
                f"Only Prony series is supported."
            )
            return 1

    def visco_elasticity(self, mat_id, all_mat_props):
        mat_string = ""
        mat_props = all_mat_props["VISCOELASTIC"]
        if (
            mat_props["Parameters"]
            and "TIME" in mat_props["Parameters"]
            and mat_props["Parameters"]["TIME"] == "PRONY"
        ):
            mat_string += "*MAT_ADD_INELASTICITY\n"
            mat_string += (
                "$#" + "".join([self._formatter.field_str(i) for i in self._header_title])[2:]
            )
            mat_string += "\n"
            header_data = self._header
            header_data[0] = mat_id
            header_data[1] = self._neilinks
            mat_string += self._formatter.field_int(header_data[0])
            mat_string += self._formatter.field_int(header_data[1])
            mat_string += self._formatter.field_float(header_data[2])
            mat_string += self._formatter.field_float(header_data[3])
            mat_string += self._formatter.field_float(header_data[4])
            mat_string += self._formatter.field_float(header_data[5])
            mat_string += self._formatter.field_float(header_data[6])
            mat_string += self._formatter.field_float(header_data[7])
            mat_string += "\n"
            data_dict = self._data_dict
            for i in range(1, self._neilinks + 1):
                current_data_line = self._data_line
                current_data_line["D1_DATA"][1] = float(
                    data_dict[f"D{i}_Weight"]
                    if len("{0}".format(data_dict[f"D{i}_Weight"]))
                    <= self._format_map[self._card_format]
                    else round(data_dict[f"D{i}_Weight"], self._format_map[self._card_format] - 2)
                )
                current_data_line["D3_DATA"][0] = float(
                    data_dict[f"D{i}_P1"]
                    if len("{0}".format(data_dict[f"D{i}_P1"]))
                    <= self._format_map[self._card_format]
                    else round(data_dict[f"D{i}_P1"], self._format_map[self._card_format] - 2)
                )
                mat_string += (
                    "$#"
                    + "".join(
                        [self._formatter.field_str(i) for i in current_data_line["D1_TITLE"]]
                    )[2:]
                    + "\n"
                )
                mat_string += self._formatter.field_int(current_data_line["D1_DATA"][0])
                mat_string += self._formatter.field_exp(current_data_line["D1_DATA"][1]) + "\n"
                # mat_string += \
                # "".join(
                # [self._formatter.field_float(i) for i in current_data_line["D1_DATA"][1:]]
                # ) + "\n"
                mat_string += (
                    "$#"
                    + "".join(
                        [self._formatter.field_str(i) for i in current_data_line["D2_TITLE"]]
                    )[2:]
                    + "\n"
                )
                # mat_string += \
                # "".join(
                # [self._formatter.field_float(i) for i in current_data_line["D2_DATA"]]
                # ) + "\n"
                mat_string += self._formatter.field_int(current_data_line["D2_DATA"][0])
                mat_string += self._formatter.field_int(current_data_line["D2_DATA"][1]) + "\n"
                mat_string += (
                    "$#"
                    + "".join(
                        [self._formatter.field_str(i) for i in current_data_line["D3_TITLE"]]
                    )[2:]
                    + "\n"
                )
                mat_string += self._formatter.field_float(current_data_line["D3_DATA"][0])
                mat_string += (
                    "".join(
                        [self._formatter.field_float(i) for i in current_data_line["D3_DATA"][1:]]
                    )
                    + "\n"
                )
        return mat_string


class MaterialProcessor:
    """Processes the material information.

    Processes simulation data to generate LS-DYNA commands.

    Parameters
    ----------
    model : prime.Model
        Model that the methods are to work on.
    sim_data : dict
        The simulation data in json dictionary format containing materials and zone information.
    card_format : str, optional
        The LS-DYNA card format for writing. Defaults to "SHORT".

    Notes
    -----
    **This is a beta class**. **The behavior and implementation may change in future**.
    """

    __slots__ = (
        '_card_format',
        '_sim_data',
        '_raw_materials_data',
        '_zone_data',
        '_mat_id',
        '_wt_factor',
        '_material_assignedTo_zones',
        '_material_dyna_cards',
        '_set_part_dyna_cards',
        '_damping_dyna_cards',
        '_formatter',
        '_model',
        '_logger',
    )

    def __init__(
        self,
        model: prime.Model,
        sim_data: dict,
        card_format: str = "SHORT",
    ):
        """Initialize class variables and the superclass."""
        self._card_format = card_format
        self._sim_data = sim_data
        self._raw_materials_data = sim_data['Materials']
        self._zone_data = sim_data['Zones']
        self._mat_id = 0
        self._wt_factor = 1.0
        self._material_assignedTo_zones = {}
        self._material_dyna_cards = []
        self._set_part_dyna_cards = []
        self._damping_dyna_cards = []
        self._formatter = _FormatDynaCards(self._card_format)
        self._model = model
        self._logger = model.python_logger

    def get_all_material_commands(self) -> str:
        """Generate and return all the material commands to be added to the LS-DYNA export file.

        Returns
        -------
            str:
                A string containing all the material commands.

        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.
        """
        if not self._material_assignedTo_zones:
            self._map_zone_type_with_material()
        mats_not_in_zones = list(
            set(self._raw_materials_data.keys()).difference(
                set(self._material_assignedTo_zones.keys())
            )
        )
        if mats_not_in_zones:
            self._logger.warning(
                f'the materials that are not in any zones {str(mats_not_in_zones)}'
            )
        # self._logger.info(self._material_assignedTo_zones)
        # for mat_name in self._material_assignedTo_zones:
        for mat_name in self._raw_materials_data:
            dyna_mat_card, dyna_set_part, dyna_damping_card = self._get_mat_comands(mat_name)
            # self._logger.info("start")
            # self._logger.info(dyna_mat_card)
            # self._logger.info(dyna_set_part)
            # self._logger.info(dyna_damping_card)
            # self._logger.info("end")
            self._material_dyna_cards.append(dyna_mat_card)
            # self._set_part_dyna_cards.append(dyna_set_part)
            # self._damping_dyna_cards.append(dyna_damping_card)
        # return ''.join(
        # self._material_dyna_cards+self._set_part_dyna_cards+self._damping_dyna_cards
        # )
        return ''.join(self._material_dyna_cards)

    def get_material_commands_by_material_name(self, mat_name: str) -> str:
        """Generate and return the material commands for a specific material given it's name.

        This is to be added to the LS-DYNA export file.

        Parameters
        ----------
            mat_name : str
                The name of the material.

        Returns
        -------
            str:
                A string containing the material commands for the given material.

        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.
        """
        if not self._material_assignedTo_zones:
            self._map_zone_type_with_material()
        if mat_name not in self._material_assignedTo_zones:
            self._material_assignedTo_zones[mat_name] = []
        dyna_mat_card, dyna_set_part, dyna_damping_card = self._get_mat_comands(mat_name)
        mat_data = self._raw_materials_data[mat_name]
        # self._logger.info(mat_data)
        dyna_text_data = ''.join([dyna_mat_card, dyna_set_part, dyna_damping_card])
        return dyna_text_data

    def get_material_commands_by_material_id(self, id: int) -> str:
        """Generate and return the material commands for a specific material given it's id.

        This is to be added to the LS-DYNA export file.

        Parameters
        ----------
            id : int
                Material id to generate material commands for.

        Returns
        -------
            str
                A string containing the material commands for the given material.

        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.
        """
        if not self._material_assignedTo_zones:
            self._map_zone_type_with_material()
        dyna_text_data = ''
        for mat_name in self._raw_materials_data:
            mat_data = self._raw_materials_data[mat_name]
            if mat_data['id'] == id:
                if mat_name not in self._material_assignedTo_zones:
                    self._material_assignedTo_zones[mat_name] = []
                mat_data = self._raw_materials_data[mat_name]
                # self._logger.info(mat_data)
                dyna_mat_card, dyna_set_part, dyna_damping_card = self._get_mat_comands(mat_name)
                dyna_text_data = ''.join([dyna_mat_card, dyna_set_part, dyna_damping_card])
                break
        return dyna_text_data

    def _get_max_id(self):
        part = self._model.parts[0]
        fileio = prime.FileIO(self._model)
        max_id = self._sim_data['SimulationData']['max_id']
        return int(max_id)

    def _get_zone_with_id(self, _id):
        for zone in self._zone_data:
            zone_details = self._zone_data[zone]
            try:
                if zone_details['id'] == _id:
                    zone_name = zone
                    zone_details = zone_details
                    return zone_name, zone_details
            except:
                pass
        return None, {}

    def _is_material_used_with_shell(self, mat_name):
        zone_types_for_2d_plasticity = ['Membrane', 'Shell']
        zone_type = None
        zone_details = {}
        used_with_shell = False
        if mat_name not in self._material_assignedTo_zones:
            used_with_shell = False
        else:
            if self._material_assignedTo_zones[mat_name]:
                for zone_id in self._material_assignedTo_zones[mat_name]:
                    zone_name, zone_details = self._get_zone_with_id(zone_id)
                    if zone_details and zone_details['Type'] in zone_types_for_2d_plasticity:
                        used_with_shell = True
                        break

        return used_with_shell

    def _is_material_used_with_membrane(self, mat_name):
        zone_types_for_2d_plasticity = ['Membrane']
        zone_details = {}
        used_with_shell = False
        if mat_name not in self._material_assignedTo_zones:
            used_with_shell = False
        else:
            if self._material_assignedTo_zones[mat_name]:
                for zone_id in self._material_assignedTo_zones[mat_name]:
                    _zone_name, zone_details = self._get_zone_with_id(zone_id)
                    if zone_details and zone_details['Type'] in zone_types_for_2d_plasticity:
                        used_with_shell = True
                        break

        return used_with_shell

    def _material_is_cohesive(self, mat_name):
        zone_name = None
        zone_details = {}
        if mat_name not in self._material_assignedTo_zones:
            zone_name = None
        else:
            if self._material_assignedTo_zones[mat_name]:
                zone_name, zone_details = self._get_zone_with_id(
                    self._material_assignedTo_zones[mat_name][0]
                )
            else:
                zone_name, zone_details = None, {}
        if zone_name is not None and zone_details['Type'] == 'Cohesive':
            return True, zone_details, zone_name
        else:
            return False, zone_details, zone_name

    def _get_cohesive_section_thickness(self, zone_details, zone_name):
        thickness = 0.1
        if "ThicknessMode" in zone_details:
            if zone_details['ThicknessMode'] != 'SPECIFIED':
                self._logger.warning(
                    f'Cohesive zone {zone_name} does not have specified thickness.'
                )
        else:
            self._logger.warning(
                f'Cohesive zone {zone_name} does not have Thickness Mode specified.'
            )
        if "Thickness" in zone_details:
            thickness = zone_details["Thickness"]
        else:
            self._logger.warning(
                f"Cohesive zone {zone_name} does not have thickness specified. "
                f"0.1 is used by default for calculations."
            )
        return thickness

    def _map_zone_type_with_material(self):
        for zone in self._zone_data:
            zone_details = self._zone_data[zone]
            # self._logger.info(zone)
            # self._logger.info(zone_details)
            if 'Material' not in zone_details:
                self._logger.warning(f'Warning: Material is not specified for zone {zone}')
                continue
            if zone_details['Material'] in self._material_assignedTo_zones:
                try:
                    zoneId = zone_details['id']
                    self._material_assignedTo_zones[zone_details['Material']].append(zoneId)
                except:
                    self._logger.warning(f'Zone {zone} does not have id for it ')
                    pass
            else:
                try:
                    zoneId = zone_details['id']
                    self._material_assignedTo_zones[zone_details['Material']] = [zoneId]
                except:
                    self._material_assignedTo_zones[zone_details['Material']] = []
                    self._logger.warning(f'Zone {zone} does not have id for it ')

    def _get_mat_comands(self, mat_name):
        mat_data = self._raw_materials_data[mat_name]
        self._mat_id = mat_data['id']
        processed_entities = [
            'PLASTIC',
            'ELASTIC',
            "VISCOELASTIC",
            "HYPERFOAM",
            "DAMPING",
            "HYPERELASTIC",
            "DAMAGE EVOLUTION",
            "DAMAGE INITIATION",
            "BRITTLE CRACKING",
        ]
        # self._logger.info(mat_data)
        dyna_mat_card = ''
        dyna_set_part = ''
        dyna_damping_card = ''
        if "Parameters" in mat_data:
            self._logger.warning(f"Parameter on Material {mat_name} are not processed.")
        hyperelast = _MatHyperelastic(self._model, card_format=self._card_format)
        visco = _MatAddInelasticity(self._model, card_format=self._card_format)
        write_low_density_foam = True
        hyperfoam = _MatViscoelasticHillFoam(self._model, card_format=self._card_format)
        linear_plastic = _MatPiecewiseLinearPlasticity(self._model, card_format=self._card_format)
        damage = _MatAddDamageDiem(self._model, card_format=self._card_format)
        britle_glass = _MatGlass(self._model, card_format=self._card_format)
        mat_cohesive_general = False
        damage_cohesive = _CohesiveMaterialMapper(self._model, card_format=self._card_format)
        damage_in_mat = False
        is_cohesive, zone_details, zone_name = self._material_is_cohesive(mat_name)
        thickness = 0.1
        if is_cohesive:
            thickness = self._get_cohesive_section_thickness(zone_details, zone_name)
        elastic_type = "ISOTROPIC"
        e, pr, sigy, etan = 0.0, 0.0, 0.0, 0.0
        density = 1e-9
        for prop in mat_data:
            if prop == 'id':
                continue
            elif prop not in processed_entities:
                if prop != 'DENSITY' and prop != "UNIAXIAL TEST DATA":
                    self._logger.warning(
                        f"The property {prop} for Material {mat_name} is not processed."
                    )
                continue
            # self._logger.info("Next")
            if 'DENSITY' in self._raw_materials_data[mat_name]:
                mat_props = self._raw_materials_data[mat_name]
                density = self._process_density(mat_props, mat_name)
            if prop == "ELASTIC":
                e, pr, sigy, etan, elastic_type = self._get_elastic_modulus(
                    mat_data, mat_name, self._mat_id
                )
                if is_cohesive is False:
                    if "PLASTIC" not in mat_data and "BRITTLE CRACKING" not in mat_data:
                        function = self._process_elastic_modulus
                        mapdl_str, elastic_type = function(
                            mat_data, mat_name, self._mat_id, density
                        )
                        dyna_mat_card += mapdl_str
                else:
                    function = self._process_elastic_modulus
                    if "PLASTIC" not in mat_data and "DAMAGE INITIATION" not in mat_data:
                        mapdl_str, elastic_type = function(
                            mat_data, mat_name, self._mat_id, density
                        )
                        dyna_mat_card += mapdl_str
            elif prop == "PLASTIC":
                if "ELASTIC" in mat_data:
                    e, pr, sigy, etan, elastic_type = self._get_elastic_modulus(
                        mat_data, mat_name, self._mat_id
                    )
                if is_cohesive is False:
                    max_id = self._get_max_id()
                    material_used_with_shell = self._is_material_used_with_shell(mat_name)
                    dyna_mat_card += linear_plastic.write_piecewise_linear_plasticity(
                        mat_data,
                        mat_name,
                        self._mat_id,
                        e,
                        pr,
                        sigy,
                        etan,
                        density,
                        material_used_with_shell,
                        max_id=max_id,
                    )
                else:
                    if "DAMAGE INITIATION" not in mat_data:
                        dyna_mat_card += linear_plastic.write_piecewise_linear_plasticity(
                            mat_data,
                            mat_name,
                            self._mat_id,
                            e,
                            pr,
                            sigy,
                            etan,
                            density,
                            False,
                            max_id=0,
                        )
            elif prop == "DAMAGE EVOLUTION":
                if is_cohesive:
                    damage_cohesive.damage_evolution(self._mat_id, mat_name, mat_data)
                else:
                    damage.damage_evolution(self._mat_id, mat_name, mat_data)
                damage_in_mat = True
            elif prop == "DAMAGE INITIATION":
                if is_cohesive:
                    damage_cohesive.damage_initiation(self._mat_id, mat_name, mat_data)
                else:
                    damage.damage_initiation(self._mat_id, mat_name, mat_data)
                damage_in_mat = True
            elif prop == "VISCOELASTIC":
                self._wt_factor = visco.get_weight_factor(self._mat_id, mat_name, mat_data)
                # self._logger.info(f"self._wt_factor 1 =  {self._wt_factor}")
                dyna_mat_card += visco.visco_elasticity(self._mat_id, mat_data)
            elif prop == "HYPERELASTIC":
                if "VISCOELASTIC" in mat_data:
                    self._wt_factor = visco.get_weight_factor(self._mat_id, mat_name, mat_data)
                dyna_mat_card += hyperelast.define_hyper_elastic(
                    self._mat_id, mat_name, mat_data, weight=self._wt_factor, density=density
                )
            elif prop == "HYPERFOAM":
                if "VISCOELASTIC" in mat_data:
                    self._wt_factor = visco.get_weight_factor(self._mat_id, mat_name, mat_data)
                # self._logger.info(f"self._wt_factor 2 =  {self._wt_factor}")
                dyna_mat_card += hyperfoam.define_visco_hill_foam(
                    self._mat_id,
                    mat_name,
                    mat_data,
                    weight=self._wt_factor,
                    density=density,
                    write_low_density_foam=write_low_density_foam,
                )
            # elif prop == "DAMPING":
            # function = self._process_damping_data
            # dyna_set_part, dyna_damping_card = function(
            # mat_data[prop], mat_name, self._mat_id
            # )
            elif prop == "BRITTLE CRACKING":
                if "ELASTIC" in mat_data:
                    e, pr, sigy, etan, elastic_type = self._get_elastic_modulus(
                        mat_data, mat_name, self._mat_id
                    )
                dyna_mat_card += britle_glass.get_britle_glass_commands(
                    self._mat_id, mat_name, mat_data, e, pr, density=density
                )
        if damage_in_mat and is_cohesive is False:
            material_used_with_shell = self._is_material_used_with_shell(mat_name)
            max_id = self._get_max_id()
            dyna_mat_card += damage.get_all_commands(
                self._mat_id, mat_name, mat_data, material_used_with_shell, max_id
            )
        if damage_in_mat and is_cohesive:
            dyna_mat_card += damage_cohesive.get_all_commands(
                self._mat_id,
                mat_name,
                mat_data,
                e,
                pr,
                sigy,
                etan,
                elastic_type,
                density,
                thickness,
                mat_cohesive_general,
            )
        return dyna_mat_card, dyna_set_part, dyna_damping_card

    def _process_damping_data(self, property_dict, mat_name, mat_id):
        alpha_damping = 0.0
        alpha_str = ''
        beta_damping = 0.0
        beta_str = ''
        damping_commands = ''
        damping_set = ''
        if property_dict['Parameters'] is None:
            self._logger.warning(f"*DAMPING does not have parameters to process.")
        if 'ALPHA' in property_dict['Parameters']:
            alpha_damping = float(property_dict['Parameters']['ALPHA'])
        if 'BETA' in property_dict['Parameters']:
            beta_damping = float(property_dict['Parameters']['BETA'])
        if (
            'COMPOSITE' in property_dict['Parameters']
            and float(property_dict['Parameters']['COMPOSITE']) != 0.0
        ):
            self._logger.warning(
                f"Parameter {'COMPOSITE'} on *DAMPING is not processed for {mat_name}."
            )
        if alpha_damping == 0.0 and beta_damping == 0.0:
            return damping_commands, damping_set
        if alpha_damping != 0.0:
            alpha_str += '*DAMPING_PART_MASS_SET\n'
            alpha_str += self._formatter.field_str(
                '9' + '0' * (8 - len(str(mat_id)) - 1) + str(mat_id)
            )
            alpha_str += self._formatter.field_float(alpha_damping)
            alpha_str += self._formatter.field_str('1.')
            alpha_str += self._formatter.field_str('0\n')
            damping_commands += alpha_str
        if beta_damping != 0.0:
            beta_str += '*DAMPING_PART_STIFFNESS_SET\n'
            beta_str += self._formatter.field_str(
                '9' + '0' * (8 - len(str(mat_id)) - 1) + str(mat_id)
            )
            beta_str += self._formatter.field_float(beta_damping)
            beta_str += self._formatter.field_str('\n')
            damping_commands += beta_str
        # if not self._material_assignedTo_zones[mat_name]:
        damping_set += "*SET_PART_TITLE\n"
        damping_set += f"DAMP_SET_PART_FOR_MATERIAL_{mat_name}\n"
        damping_set += (
            self._formatter.field_str('9' + '0' * (8 - len(str(mat_id)) - 1) + str(mat_id)) + '\n'
        )
        for i, val in enumerate(self._material_assignedTo_zones[mat_name]):
            damping_set += self._formatter.field_int(val)
            if (i + 1) % 8 == 0:
                damping_set += '\n'
        if len(self._material_assignedTo_zones[mat_name]) % 8 != 0:
            damping_set += '\n'
        # if self._material_assignedTo_zones[mat_name]:
        #     self._logger.warning(
        # f"material {mat_name} is not used for any parts in the model."
        # )
        #     return '', ''
        return damping_commands, damping_set

    def _process_density(self, mat_props, mat_name):
        property_dict = mat_props['DENSITY']
        if "Parameters" in property_dict and property_dict['Parameters'] is not None:
            self._logger.warning(f"Parameter on *DENSITY are not processed.")
        density = property_dict['Data']['Mass density']
        if 'Temperature' in property_dict['Data']:
            temperature = property_dict['Data']['Temperature']
            if len(density) != len(temperature):
                self._logger.warning(
                    f"data values on *DENSITY are not consistent for material {mat_name}."
                )
        if len(density) > 1:
            self._logger.warning(
                f"there are multiple data values on *DENSITY, "
                f"use MPTEMP and MPDATA to define the material property."
                f"Density is not processed correctly for material {mat_name}"
            )
            density_data = float(density[0])
        else:
            density_data = float(density[0])
        return density_data

    def _process_elastic_modulus(self, mat_props, mat_name, mat_id, density):
        property_dict = mat_props['ELASTIC']
        mat_elastic_card = ''
        elastic_type = property_dict["Parameters"]["TYPE"]
        if elastic_type == "ISOTROPIC" or elastic_type == "ISO":
            # self._logger.warning(
            # f"Only isotropic elastic modulus is processed, "
            # f"Elastic Modulus for the material {material} "
            #       f"is not processed."
            # )
            # return ''
            youngs_mod = property_dict['Data']['E']
            nu = property_dict['Data']['V']
            # temperature = property_dict['Data']['Temperature']
            if 'Temperature' in property_dict['Data']:
                temperature = property_dict['Data']['Temperature']
                if len(youngs_mod) != len(temperature):
                    self._logger.warning(
                        f"data values on *ELASTIC are not consistent for material {mat_name}."
                    )
            if len(youngs_mod) != len(nu):
                self._logger.warning(
                    f"data values on *ELASTIC are not consistent for material {mat_name}."
                )
            if len(youngs_mod) > 1:
                self._logger.warning(
                    f"there are multiple data values on *ELASTIC, "
                    f"use MPTEMP and MPDATA to define the material property."
                    f"elastic properties are not processed correctly for material {mat_name}"
                )
            # self._logger.info(youngs_mod)
            # self._logger.info(nu)
            elastic_modulus = float(youngs_mod[0])
            nu = float(nu[0])
            if mat_name not in self._material_assignedTo_zones:
                zone_name = None
            else:
                if self._material_assignedTo_zones[mat_name]:
                    zone_name, zone_details = self._get_zone_with_id(
                        self._material_assignedTo_zones[mat_name][0]
                    )
                else:
                    zone_name, zone_details = None, ''
            # if zone_name is not None and zone_details['Type'] == 'Cohesive':
            # self._logger.warning(
            # f"The material {mat_name} is assigned to cohesive component "
            # f"{zone_name}. It is not yet processed"
            # )
            # else:
            mat_elastic_card += "*MAT_ELASTIC_TITLE\n"
            mat_elastic_card += f"{mat_name}\n"
            mat_elastic_card += (
                f"${self._formatter.field_str('MID|')}"
                f"{self._formatter.field_str('RO|')}"
                f"{self._formatter.field_str('E|')}"
                f"{self._formatter.field_str('PR|')}"
                f"{''.join([self._formatter.field_str('|')]*4)}\n"
            )
            mat_elastic_card += (
                f"{self._formatter.field_int(mat_id)}"
                f"{self._formatter.field_exp(density)}"
                f"{self._formatter.field_float(elastic_modulus)}"
                f"{self._formatter.field_exp(nu)}"
                f"{''.join([self._formatter.field_str('0.')]*4)}\n"
            )
            if self._is_material_used_with_membrane(mat_name):
                max_id = self._get_max_id()
                mat_fabric = _MatFabric(self._model, card_format=self._card_format)
                mat_elastic_card += mat_fabric.write_mat_fabric(
                    mat_name, mat_id, nu, density, max_id=max_id
                )
        elif elastic_type == "TRACTION":
            kn = property_dict['Data']['E/Knn']
            ks1 = property_dict['Data']['G1/Kss']
            ks2 = property_dict['Data']['G2/Ktt']
            if 'Temperature' in property_dict['Data']:
                temperature = property_dict['Data']['Temperature']
                if len(kn) != len(temperature):
                    self._logger.warning(
                        f"data values on *ELASTIC are not consistent for material {mat_name}."
                    )
            mat_elastic_card += "*MAT_COHESIVE_ELASTIC_TITLE\n"
            mat_elastic_card += f"{mat_name}\n"
            mat_elastic_card += (
                f"${self._formatter.field_str('MID|')}"
                f"{self._formatter.field_str('RO|')}"
                f"{self._formatter.field_str('E|')}"
                f"{self._formatter.field_str('PR|')}"
                f"{self._formatter.field_str('KS|')}"
                f"{self._formatter.field_str('KN|')}\n"
            )
            mat_elastic_card += (
                f"{self._formatter.field_int(mat_id)}"
                f"{self._formatter.field_exp(density)}"
                f"{self._formatter.field_str('')}"
                f"{self._formatter.field_str('')}"
                f"{self._formatter.field_float(ks1[0])}"
                f"{self._formatter.field_float(kn[0])}\n"
            )
        else:
            self._logger.warning(
                f"Elastic Modulus with type = {property_dict['Parameters']['TYPE']} "
                f"is not processed."
            )
            return '', elastic_type
        return mat_elastic_card, elastic_type

    def _get_elastic_modulus(self, mat_props, mat_name, mat_id):
        property_dict = mat_props['ELASTIC']
        elastic_type = property_dict["Parameters"]["TYPE"]
        if elastic_type == "ISOTROPIC" or elastic_type == "ISO":
            # self._logger.warning(f"Only isotropic elastic modulus is processed, "
            # f"Elastic Modulus for the material {material} "
            #       f"is not processed.")
            # return ''
            youngs_mod = property_dict['Data']['E']
            nu = property_dict['Data']['V']
            # temperature = property_dict['Data']['Temperature']
            if 'Temperature' in property_dict['Data']:
                temperature = property_dict['Data']['Temperature']
                if len(youngs_mod) != len(temperature):
                    self._logger.warning(
                        f"data values on *ELASTIC are not consistent for material {mat_name}."
                    )
            if len(youngs_mod) != len(nu):
                self._logger.warning(
                    f"data values on *ELASTIC are not consistent for material {mat_name}."
                )
            if len(youngs_mod) > 1:
                self._logger.warning(
                    f"there are multiple data values on *ELASTIC, "
                    f"use MPTEMP and MPDATA to define the material property."
                    f"elastic properties are not processed correctly for material {mat_name}"
                )
            # self._logger.info(youngs_mod)
            # self._logger.info(nu)
            elastic_modulus = float(youngs_mod[0])
            nu = float(nu[0])
            return elastic_modulus, nu, 0.0, 0.0, elastic_type
        elif elastic_type == "TRACTION":
            kn = property_dict['Data']['E/Knn']
            ks1 = property_dict['Data']['G1/Kss']
            ks2 = property_dict['Data']['G2/Ktt']
            if 'Temperature' in property_dict['Data']:
                temperature = property_dict['Data']['Temperature']
                if len(kn) != len(temperature):
                    self._logger.warning(
                        f"data values on *ELASTIC are not consistent for material {mat_name}."
                    )
            if len(kn) != len(ks1):
                self._logger.warning(
                    f"data values on *ELASTIC are not consistent for material {mat_name}."
                )
            if len(kn) > 1:
                self._logger.warning(
                    f"there are multiple data values on *ELASTIC, "
                    f"use MPTEMP and MPDATA to define the material property."
                    f"elastic properties are not processed correctly for material {mat_name}"
                )
            return float(kn[0]), float(ks1[0]), float(ks2[0]), 0.0, elastic_type
        else:
            return 0.0, 0.0, 0.0, 0.0, elastic_type


class DatabaseProcessor:
    """Processes the part's simulation data and generates LS-DYNA cards for database keywords.

    Parameters
    ----------
    model : prime.Model
        Model that the methods are to work on.
    steps_data : dict
        The steps data extracted from the part's simulation data.
    card_format : str, optional
        The LS-DYNA card format for writing. Defaults to "SHORT".

    Notes
    -----
    **This is a beta API**. **The behavior and implementation may change in future**.
    """

    __slots__ = (
        '_steps_data',
        '_time',
        '_card_format',
        '_formatter',
        '_format_map',
        '_header_title',
        '_header_title4',
        '_header_title5',
        '_header',
        '_header4',
        '_header5',
        '_model',
        '_logger',
    )

    def __init__(self, model: prime.Model, steps_data: dict, card_format: str = "SHORT"):
        """Initialize class variables and the superclass."""
        self._steps_data = steps_data
        self._time = 0.0
        self._card_format = card_format
        self._formatter = _FormatDynaCards(self._card_format)
        self._format_map = {"SHORT": 10, "LONG": 20}
        self._header_title = [
            "dt",
            "binary",
            "lcur",
            "ioopt",
            "option1",
            "option2",
            "option3",
            "option4",
        ]
        self._header_title4 = ["iglb", "ixyz", "ivel", "iacc", "istrs", "istra", "ised"]
        self._header_title5 = ["iform", "ibinary"]
        self._header = [1.000e-03, 3, 0, 1, 0, 0, 0, 0]
        self._header4 = [1, 1, 0, 0, 0, 0, 0]
        self._header5 = [0, 1]
        self._model = model
        self._logger = model.python_logger

    def get_output_database_keywords(self) -> str:
        """Generate and return the LS-DYNA database keyword cards.

        Returns
        -------
            str
                A string containing the LS-DYNA database keyword cards for writing.

        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.
        """
        time = self._get_dynamic_analysis_time_period()
        database_keyword = ""
        database_maps = [
            'DATABASE_BNDOUT',
            'DATABASE_DISBOUT',
            'DATABASE_DEFORC',
            'DATABASE_ELOUT',
            'DATABASE_GLSTAT',
            'DATABASE_JNTFORC',
            'DATABASE_MATSUM',
            'DATABASE_NCFORC',
            'DATABASE_NODOUT',
            'DATABASE_RBDOUT',
            'DATABASE_RCFORC',
            'DATABASE_SLEOUT',
            'DATABASE_SPCFORC',
            'DATABASE_SWFORC',
        ]
        for i in range(len(database_maps)):
            database_keyword += "*" + str(database_maps[i]) + "\n"
            database_keyword += (
                "$#"
                + "".join([self._formatter.field_str(i) for i in self._header_title])[2:]
                + "\n"
            )
            header_data = self._header
            database_keyword += self._formatter.field_float(header_data[0] * time)
            database_keyword += self._formatter.field_int(header_data[1])
            database_keyword += self._formatter.field_int(header_data[2])
            database_keyword += self._formatter.field_int(header_data[3])
            database_keyword += self._formatter.field_int(header_data[4])
            database_keyword += self._formatter.field_int(header_data[5])
            database_keyword += self._formatter.field_int(header_data[6])
            database_keyword += self._formatter.field_int(header_data[7])
            database_keyword += "\n"
        database_keyword += "*DATABASE_FORMAT\n"
        database_keyword += (
            "$#" + "".join([self._formatter.field_str(i) for i in self._header_title5])[2:] + "\n"
        )
        database_keyword += self._formatter.field_int(self._header5[0])
        database_keyword += self._formatter.field_int(self._header5[1])
        database_keyword += "\n"
        return database_keyword

    def _get_dynamic_analysis_time_period(self):
        step_data = self._steps_data
        for i in range(len(step_data)):
            if 'Dynamic' in step_data[i]:
                dynamic_data = step_data[i]['Dynamic']
                if type(dynamic_data) == list:
                    dynamic_data = dynamic_data[0]
                if 'Data' in dynamic_data:
                    data = dynamic_data['Data']
                    if 'time_period' in data:
                        time_period = float(data['time_period'])
                self._time += time_period
        return self._time
