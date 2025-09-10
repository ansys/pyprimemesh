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

"""Module for MAPDL cdb export utilities."""

########################### [TODO] ##################################
# [TODO] code quality of this file is not up to PyPrimeMesh standards,
# please move the code to cpp or improve the code quality
########################### [TODO] ##################################

import json
import os
import re
from typing import Tuple

import ansys.meshing.prime as prime
from ansys.meshing.prime.autogen.fileiostructs import ExportMapdlCdbParams

__all__ = ['generate_mapdl_commands']


class _TractionProperties:
    DAMAGE_EVOLUTION_ENERGY = 1000
    NOM_STRESS_1 = 1e10
    NOM_STRESS_2 = 1e10
    NOM_STRESS_3 = 1e10


class _FormatEntities:
    __slots__ = ('_card_format', '_format_map')

    def __init__(self, card_format="LONG"):
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
            if abs(float(num)) < 1000:
                field = str(num)[:field_len]
            elif len(str(int(float(num)))) < 7:
                field = str(num)[:field_len]
            else:
                field = self.field_exp(num)
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


class _ModelInformation:
    model_simulation_data = None


class _TimePointsProcessor:
    __slots__ = ('_time_data', '_file_name', '_formatter', '_model', '_logger')

    def __init__(self, model: prime.Model, data, file_name=''):
        self._time_data = data
        self._file_name = file_name
        self._formatter = _FormatEntities()
        self._model = model
        self._logger = model.python_logger

    def write_timepoint_table_to_file(self, mapdl_commands):
        with open(self._file_name, 'a') as file_time_pt:
            file_time_pt.write(mapdl_commands)

    def get_all_timepoints_commands(self):
        time_pt_data = self._time_data
        time_pt_commands = ''
        for time_pt_table_name, time_pt_table_data in time_pt_data.items():
            time_pt_commands += self._get_commands(time_pt_table_name, time_pt_table_data)
        if os.path.isfile(self._file_name) and time_pt_commands != "":
            self.write_timepoint_table_to_file(time_pt_commands)
        else:
            self._logger.warning(
                f"Warning: Please provide the valid file name to write data."
                f"or check the table is processed correctly."
            )
        return time_pt_commands

    def _get_commands(self, time_pt_table_name, time_pt_table_data):
        mapdl_commands = ''
        params = time_pt_table_data['Parameters']
        if "GENERATE" in params:
            self._logger.warning(
                f"Warning: timepoint table with argument generate is not processed."
            )
            return mapdl_commands
        if "INPUT" in params:
            self._logger.warning(
                f"Warning: timepoint table with argument generate is not processed."
            )
        pt_data = time_pt_table_data['Data']['time_points']
        formatter_pt_data = [f"{self._formatter.field_str(pt)}" for pt in pt_data]
        all_values = []
        all_values.extend(formatter_pt_data)
        format_output = ""
        for i in range(0, len(all_values), 4):
            values = all_values[i : i + 4]
            format_output += ''.join(values) + '\n'
        tpname = get_modified_component_name(time_pt_table_name)
        mapdl_commands += f"*DIM, {tpname}, ARRAY, {len(pt_data)}, 1, 1,\n"
        mapdl_commands += f"*PREAD, {tpname}, {len(pt_data)}\n"
        mapdl_commands += format_output
        mapdl_commands += "END PREAD\n"
        return mapdl_commands


class _OutputIntervalProcessor:
    __slots__ = ('_formatter', '_model', '_logger')

    def __init__(self, model: prime.Model):
        self._formatter = _FormatEntities()
        self._model = model
        self._logger = model.python_logger

    def write_interval_points_table_to_file(self, mapdl_commands):
        # with open(self._file_name, 'a') as file_time_pt:
        # file_time_pt.write(mapdl_commands)
        if os.path.isfile(_AmplitudeProcessor._amplitude_file):
            with open(_AmplitudeProcessor._amplitude_file, 'w') as file_ampl:
                file_ampl.write('/prep7\n')
        if _AmplitudeProcessor._amplitude_file:
            with open(_AmplitudeProcessor._amplitude_file, 'a') as file_ampl:
                file_ampl.write(mapdl_commands)
        else:
            self._logger.info(
                f"Please specify the file path to write amplitude tables- "
                f"(_AmplitudeProcessor._amplitude_file = FilePathLocation). "
                f"Interval Tables are not written to the file"
            )

    def get_commands(self, time_pt_table_name, number_interval, delta_time, step_start_time):
        mapdl_commands = ''
        formatter_pt_data = [
            step_start_time + i * delta_time / number_interval
            for i in range(1, number_interval + 1)
        ]
        formatter_pt_data = sorted(list(set(formatter_pt_data)))
        formatter_pt_data = [self._formatter.field_float(i) for i in formatter_pt_data]
        all_values = []
        all_values.extend(formatter_pt_data)
        format_output = ""
        for i in range(0, len(all_values), 4):
            values = all_values[i : i + 4]
            format_output += ''.join(values) + '\n'
        mapdl_commands += f"*DIM, {time_pt_table_name}, ARRAY, {len(formatter_pt_data)}, 1, 1,\n"
        mapdl_commands += f"*PREAD, {time_pt_table_name}, {len(formatter_pt_data)}\n"
        mapdl_commands += format_output
        mapdl_commands += "END PREAD\n"
        return mapdl_commands


class _AmplitudeProcessor:
    _amplitude_file = ""
    _amplitude_count = 0
    __slots__ = (
        '_amplitudes_data',
        '_step_start_time',
        '_step_end_time',
        '_scale_factor',
        '_relative_value',
        '_step_time',
        '_definition',
        '_modified_amplitude_name',
        '_formatter',
        '_model',
        '_logger',
    )

    def __init__(self, model: prime.Model, data):
        self._amplitudes_data = data
        self._step_start_time = 0.0
        self._step_end_time = 1.0
        self._scale_factor = 1.0
        self._relative_value = True
        self._step_time = True
        self._definition = 'TABULAR'
        self._modified_amplitude_name = None
        self._formatter = _FormatEntities()
        self._model = model
        self._logger = model.python_logger

    def write_amplitude_table_to_file(self, mapdl_commands):
        if _AmplitudeProcessor._amplitude_file:
            with open(_AmplitudeProcessor._amplitude_file, 'a') as file_ampl:
                file_ampl.write(mapdl_commands)
        else:
            self._logger.info(
                f"Please specify the file path to write amplitude tables-  "
                f"(_AmplitudeProcessor._amplitude_file = FilePathLocation)"
            )

    def get_all_amplitude_commands(self):
        amplitudes_data = self._amplitudes_data
        amplitude_commands = ''
        for ampl_name, ampl_table_data in amplitudes_data.items():
            self._modified_amplitude_name = ampl_name
            amplitude_commands += self._get_commands(ampl_name, ampl_table_data)
        return amplitude_commands

    def get_mapdl_commands_for_amplitude(
        self,
        amplitude_name,
        modified_amplitude_name,
        applied_on,
        step_start_time=0.0,
        step_end_time=1.0,
        scale_factor=1.0,
    ):
        _AmplitudeProcessor._amplitude_count += 1
        self._modified_amplitude_name = (
            modified_amplitude_name + "_" + str(_AmplitudeProcessor._amplitude_count)
        )
        # self._logger.info(f"scale_factor = {scale_factor}")
        # self._logger.info(f"step_start_time = {step_start_time}")
        # self._logger.info(f"step_end_time = {step_end_time}")
        self._scale_factor = float(scale_factor)
        self._step_start_time = float(step_start_time)
        self._step_end_time = float(step_end_time)
        amplitudes_data = self._amplitudes_data
        amplitude_commands = ''
        if amplitude_name not in amplitudes_data.keys():
            self._logger.warning(
                f"Amplitude table '{amplitude_name}' is not defined with *AMPLITUDE."
            )
            return amplitude_commands
        for ampl_name, ampl_table_data in amplitudes_data.items():
            if amplitude_name == ampl_name:
                amplitude_commands += self._get_commands(ampl_name, ampl_table_data, applied_on)
                break
        return amplitude_commands

    def _get_commands(self, amplitude_name, ampl_table_data, applied_on="Not Provided"):
        amplitude_commands = ''
        if type(ampl_table_data) == dict:
            if 'Data' not in ampl_table_data or ampl_table_data['Data'] is None:
                self._logger.warning(
                    f"Warning: datalines are not present on Amplitude table '{amplitude_name}', "
                    f" this is not processed"
                )
                return amplitude_commands
            self._relative_value = True
            self._step_time = True
            interval = None
            begin = 0.0
            self._definition = 'TABULAR'
            if 'Parameters' in ampl_table_data and ampl_table_data['Parameters'] is not None:
                if (
                    "VALUE" in ampl_table_data['Parameters']
                    and ampl_table_data['Parameters']["VALUE"] == "RELATIVE"
                ):
                    self._relative_value = False
                if (
                    "TIME" in ampl_table_data['Parameters']
                    and ampl_table_data['Parameters']["TIME"] == "TOTAL TIME"
                ):
                    self._step_time = False
                if "FIXED INTERVAL" in ampl_table_data['Parameters']:
                    interval = float(ampl_table_data['Parameters']["FIXED INTERVAL"])
                if "BEGIN" in ampl_table_data['Parameters']:
                    begin = float(ampl_table_data['Parameters']["BEGIN"])
                if "SMOOTH" in ampl_table_data['Parameters']:
                    self._logger.warning(
                        f"Warning: SMOOTH Parameter on Amplitude table '{amplitude_name}' "
                        f"is not processed"
                    )
                if "INPUT" in ampl_table_data['Parameters']:
                    self._logger.warning(
                        f"Warning: INPUT Parameter on Amplitude table '{amplitude_name}' "
                        f"is not processed"
                    )
                    return amplitude_commands
                if "DEFINITION" not in ampl_table_data['Parameters']:
                    self._definition = 'TABULAR'
                else:
                    self._definition = ampl_table_data['Parameters']["DEFINITION"]
            amplitude_commands += "\n"
            amplitude_commands += f"! Defining table with name: {amplitude_name}, "
            if applied_on != "Not Provided":
                amplitude_commands += f"and it is used with component name/node id : {applied_on}"
            amplitude_commands += "\n"
            if self._definition == 'TABULAR':
                amplitude_commands += self._process_tabular_data(
                    amplitude_name, ampl_table_data['Data']
                )
            elif self._definition == 'EQUALLY SPACED':
                amplitude_commands += self._process_equally_spaced_data(
                    amplitude_name, ampl_table_data['Data'], begin, interval
                )
            elif self._definition == 'PERIODIC':
                amplitude_commands += self._process_periodic_data(
                    amplitude_name, ampl_table_data['Data']
                )
            else:
                self._logger.warning(
                    f"Warning: *AMPLITUDE ('{amplitude_name}') with DEFINITION type "
                    f"{ampl_table_data['Parameters']['DEFINITION']} is not processed"
                )
        return amplitude_commands

    def _process_periodic_amplitude_table(self, name, magn, freq):
        table_string = """!
! ANSYS Function Representation
!
*DIM,{0},TABLE,6,6,2,,,,0
!
! Begin of equation: time (N)
{0}(0,0,1)= 0, -999
{0}(2,0,1)= 0.0
{0}(3,0,1)= 0.0
{0}(4,0,1)= 0.0
{0}(5,0,1)= 0.0
{0}(6,0,1)= 0.0
{0}(0,1,1)= 1.0, 99, 0, 1, 1, 0, 0
{0}(0,2,1)= 0.0,
{0}(0,3,1)=   1,
{0}(0,4,1)= 0.0,
{0}(0,5,1)= 0.0,
{0}(0,6,1)= 0.0,
! End of equation: time (N)
!
! Begin of equation: {1}*sin({2}*time) (N)
{0}(0,0,2)= -999, -999
{0}(2,0,2)= 0.0
{0}(3,0,2)= 0.0
{0}(4,0,2)= 0.0
{0}(5,0,2)= 0.0
{0}(6,0,2)= 0.0
{0}(0,1,2)= 1.0, -1, 0, {2}, 0, 0, 1
{0}(0,2,2)= 0.0, -2, 0, 1, -1, 3, 1
{0}(0,3,2)=   0, -1, 9, 1, -2, 0, 0
{0}(0,4,2)= 0.0, -2, 0, {1}, 0, 0, -1
{0}(0,5,2)= 0.0, -3, 0, 1, -2, 3, -1
{0}(0,6,2)= 0.0, 99, 0, 1, -3, 0, 0
! End of equation: {1}*sin({2}*time) (N)

"""
        # string.format(name, amplitude, frequency)
        return table_string.format(name, magn, freq)

    def _process_periodic_amplitude_table_complete_single_term(
        self, name, magn, A0, t0, A1, B1, freq
    ):
        table_string = """!
! A0 = {2}
! Omega = {6}
! t0 = {3}
! A1 = {4}
! B1 = {5}
! Magnitude = {1}

/com,*********** Create Displacement Tables and Functions ******
!
! ANSYS Function Representation
!
*DIM,{0},TABLE,6,20,2,,,,0
!
! Begin of equation: time (mm)
{0}(0,0,1)= 0, -999
{0}(2,0,1)= 0.0
{0}(3,0,1)= 0.0
{0}(4,0,1)= 0.0
{0}(5,0,1)= 0.0
{0}(6,0,1)= 0.0
{0}(0,1,1)= 1.0, 99, 0, 1, 1, 0, 0
{0}(0,2,1)= 0.0,
{0}(0,3,1)=   0,
{0}(0,4,1)= 0.0,
{0}(0,5,1)= 0.0,
{0}(0,6,1)= 0.0,
{0}(0,7,1)= 0.0,
{0}(0,8,1)= 0.0,
{0}(0,9,1)= 0.0,
{0}(0,10,1)= 0.0,
{0}(0,11,1)= 0.0,
{0}(0,12,1)= 0.0,
{0}(0,13,1)= 0.0,
{0}(0,14,1)= 0.0,
{0}(0,15,1)= 0.0,
{0}(0,16,1)= 0.0,
{0}(0,17,1)= 0.0,
{0}(0,18,1)= 0.0,
{0}(0,19,1)= 0.0,
{0}(0,20,1)= 0.0,
! End of equation: time (mm)
!
! Begin of equation: Magnitude*(A0 + (A1*cos(Omega*(time-t0)) + B1*sin(Omega*(time-t0)))) (mm)
! Begin of equation: {1}*({2} + ({4}*cos({6}*(time-{3})) + {5}*sin({6}*(time-{3})))) (mm)
{0}(0,0,2)= -999, -999
{0}(2,0,2)= 0.0
{0}(3,0,2)= 0.0
{0}(4,0,2)= 0.0
{0}(5,0,2)= 0.0
{0}(6,0,2)= 0.0
{0}(0,1,2)= 1.0, -1, 0, {3}, 0, 0, 1
{0}(0,2,2)= 0.0, -2, 0, 1, 1, 2, -1
{0}(0,3,2)=   0, -1, 0, {6}, 0, 0, -2
{0}(0,4,2)= 0.0, -3, 0, 1, -1, 3, -2
{0}(0,5,2)= 0.0, -1, 10, 1, -3, 0, 0
{0}(0,6,2)= 0.0, -2, 0, {4}, 0, 0, -1
{0}(0,7,2)= 0.0, -3, 0, 1, -2, 3, -1
{0}(0,8,2)= 0.0, -1, 0, {3}, 0, 0, 1
{0}(0,9,2)= 0.0, -2, 0, 1, 1, 2, -1
{0}(0,10,2)= 0.0, -1, 0, {6}, 0, 0, -2
{0}(0,11,2)= 0.0, -4, 0, 1, -1, 3, -2
{0}(0,12,2)= 0.0, -1, 9, 1, -4, 0, 0
{0}(0,13,2)= 0.0, -2, 0, {5}, 0, 0, -1
{0}(0,14,2)= 0.0, -4, 0, 1, -2, 3, -1
{0}(0,15,2)= 0.0, -1, 0, 1, -3, 1, -4
{0}(0,16,2)= 0.0, -2, 0, {2}, 0, 0, -1
{0}(0,17,2)= 0.0, -3, 0, 1, -2, 1, -1
{0}(0,18,2)= 0.0, -1, 0, {1}, 0, 0, -3
{0}(0,19,2)= 0.0, -2, 0, 1, -1, 3, -3
{0}(0,20,2)= 0.0, 99, 0, 1, -2, 0, 0
! End of equation: Magnitude*(A0 + (A1*cos(Omega*(time-t0)) + B1*sin(Omega*(time-t0)))) (mm)
"""
        return table_string.format(name, magn, A0, t0, A1, B1, freq)

    def _process_periodic_data(self, amplitude_name, ampl_table_data):
        amplitude_commands = ""
        data = ampl_table_data
        freq = 0.0
        terms = 1
        t0 = 0.0
        A0 = 0.0
        A = []
        B = []
        if "number_of_terms" in data:
            terms = int(data["number_of_terms"])
        if "circular_frequency" in data:
            # freq = float(data["circular_frequency"]) * 180 / math.pi
            freq = float(data["circular_frequency"])
        if "t0" in data:
            t0 = float(data["t0"])
        if "A0" in data:
            A0 = float(data["A0"])
        if "A" in data:
            A = data["A"]
        if "B" in data:
            B = data["B"]
        if terms > 1:
            self._logger.warning(
                f"Warning: multiple Sine/Cosine terms for Amplitude Table '{amplitude_name}' "
                f"is not processed. Only First term is used to define table "
                f"please check the table created with name: "
                f"{self._modified_amplitude_name}"
            )
        if t0 != 0:
            self._logger.warning(
                f"Warning: nonzero value of 't0' is specified. "
                f"This is not supported in Ansys MAPDL solver directly. "
                f"Split the step in two to create equivalent effect. "
                f"Table is written with t0 = 0.0"
            )
        # for i, pt in enumerate(zip(A, B)):
        # if i == 0 and float(pt[0]) != 0:
        # self._logger.warning(
        # f"Cosine terms for Amplitude Table '{amplitude_name}' is not processed."
        # f" please check the table created with name: "
        # f"{self._modified_amplitude_name}"
        # )
        # if i == 0 and float(pt[1]) != 1:
        # self._logger.warning(
        # f"Sine terms for Amplitude Table '{amplitude_name}' is  not equal to 1, "
        # f"A*SIN(w*time) equation is processed please check the table "
        # f"created with name: {self._modified_amplitude_name}"
        # )
        # amplitude_commands += self._process_periodic_amplitude_table(
        # self._modified_amplitude_name, self._scale_factor, freq
        # )
        if A:
            A1 = A[0]
        if B:
            B1 = B[0]
        amplitude_commands += self._process_periodic_amplitude_table_complete_single_term(
            self._modified_amplitude_name, self._scale_factor, A0, t0, A1, B1, freq
        )
        return amplitude_commands

    def _process_equally_spaced_data(self, amplitude_name, ampl_table_data, begin, interval):
        amplitude_commands = ""
        data_lines = ampl_table_data
        formatted_amp = []
        formatted_time = []
        if 'amplitude' in data_lines:
            amp = data_lines['amplitude']
            if self._relative_value:
                formatted_amp = [
                    f"{self._formatter.field_float(float(value)*self._scale_factor)}"
                    for value in amp
                ]
            else:
                formatted_amp = [f"{self._formatter.field_float(float(value))}" for value in amp]
        initial_time_skip = (self._step_end_time - self._step_start_time) * 1e-5
        # if 'time_or_frequency' in data_lines:
        # time = data_lines['time_or_frequency']
        if interval is None:
            self._logger.warning(
                f"Warning: FIXED INTERVAL Parameter is not provided on Amplitude table "
                f"'{amplitude_name}' table is not processed"
            )
            return amplitude_commands
        if not self._step_time:
            formatted_time = [
                f"{self._formatter.field_float(i*float(interval)+begin)}"
                for i in range(0, len(formatted_amp))
            ]
        else:
            formatted_time = [
                f"{self._formatter.field_float(i*float(interval)+begin+self._step_start_time)}"
                for i in range(0, len(formatted_amp))
            ]
            if self._step_start_time != 0.0:
                ff = self._formatter.field_float(float(formatted_time[0]) + initial_time_skip)
                formatted_time[0] = f"{ff}"
        if self._step_time and self._step_start_time != 0.0:
            formatted_time.insert(0, f"{self._formatter.field_float(0.0)}")
            formatted_time.insert(1, f"{self._formatter.field_float(float(self._step_start_time))}")
            formatted_amp.insert(0, f"{self._formatter.field_float(0.0)}")
            formatted_amp.insert(1, f"{self._formatter.field_float(0.0)}")
            # add two times there! 0, current step start time
        fixed_value = [self._formatter.field_str('0.7888609052210E-30')]
        all_values = []
        all_values.extend(fixed_value)
        all_values.extend(formatted_time)
        all_values.extend(fixed_value)
        all_values.extend(formatted_amp)
        format_output = ''
        for i in range(0, len(all_values), 4):
            values = all_values[i : i + 4]
            format_output += ''.join(values) + '\n'
        man = self._modified_amplitude_name
        amplitude_commands += f"*DIM, {man}, TABLE, {len(formatted_amp)}, 1, 1,\n"
        amplitude_commands += f"*PREAD, {man}, {len(formatted_amp)+len(formatted_time)+2}\n"
        amplitude_commands += format_output
        amplitude_commands += "END PREAD\n"
        amplitude_commands += "\n"
        return amplitude_commands

    def _process_tabular_data(self, amplitude_name, ampl_table_data):
        amplitude_commands = ""
        data_lines = ampl_table_data
        formatted_amp = []
        formatted_time = []
        if 'amplitude' in data_lines:
            amp = data_lines['amplitude']
            if self._relative_value:
                formatted_amp = [
                    f"{self._formatter.field_float(float(value)*self._scale_factor)}"
                    for value in amp
                ]
            else:
                formatted_amp = [f"{self._formatter.field_float(float(value))}" for value in amp]
        initial_time_skip = (self._step_end_time - self._step_start_time) * 1e-5
        if 'time_or_frequency' in data_lines:
            time = data_lines['time_or_frequency']
            if not self._step_time:
                formatted_time = [f"{self._formatter.field_float(float(value))}" for value in time]
            else:
                formatted_time = [
                    f"{self._formatter.field_float(float(value)+self._step_start_time)}"
                    for value in time
                ]
                if self._step_start_time != 0.0:
                    ff = self._formatter.field_float(float(formatted_time[0]) + initial_time_skip)
                    formatted_time[0] = f"{ff}"
        if self._step_time and self._step_start_time != 0.0:
            formatted_time.insert(0, f"{self._formatter.field_float(0.0)}")
            formatted_time.insert(1, f"{self._formatter.field_float(float(self._step_start_time))}")
            formatted_amp.insert(0, f"{self._formatter.field_float(0.0)}")
            formatted_amp.insert(1, f"{self._formatter.field_float(0.0)}")
            # add two times there! 0, current step start time
        fixed_value = [self._formatter.field_str('0.7888609052210E-30')]
        all_values = []
        all_values.extend(fixed_value)
        all_values.extend(formatted_time)
        all_values.extend(fixed_value)
        all_values.extend(formatted_amp)
        format_output = ''
        for i in range(0, len(all_values), 4):
            values = all_values[i : i + 4]
            format_output += ''.join(values) + '\n'
        man = self._modified_amplitude_name
        amplitude_commands += f"*DIM, {man}, TABLE, {len(formatted_amp)}, 1, 1,\n"
        amplitude_commands += f"*PREAD, {man}, {len(formatted_amp)+len(formatted_time)+2}\n"
        amplitude_commands += format_output
        amplitude_commands += "END PREAD\n"
        return amplitude_commands


class _MaterialProcessor:
    __slots__ = (
        '_raw_materials_data',
        '_zone_data',
        '_enable_hm_comments',
        '_mat_id',
        '_material_linked_to_zone_type',
        '_cohezive_zone_thickness_data',
        '_property_function_map',
        '_model',
        '_logger',
        '_skip_comments',
    )

    def __init__(
        self,
        model: prime.Model,
        raw_materials_data,
        zone_data,
        hm_comments=False,
        skip_comments=True,
    ):
        self._raw_materials_data = raw_materials_data
        self._zone_data = zone_data
        self._mat_id = 0
        self._enable_hm_comments = hm_comments
        self._material_linked_to_zone_type = {}
        self._cohezive_zone_thickness_data = {}
        self._property_function_map = {
            'DENSITY': self._process_density,
            'ELASTIC': self._process_elastic_modulus,
            'PLASTIC': self._process_plastic_data,
            'HYPERELASTIC': self._process_hyperelastic_data,
            'DAMPING': self._process_damping_data,
            'EXPANSION': self._process_expansion_data,
            'DAMAGE EVOLUTION': self._process_damage_evolution_data,
            'DAMAGE INITIATION': self._process_damage_initiation_data,
            'HYPERFOAM': self._process_hyperfoam_data,
            'VISCOELASTIC': self._process_viscoelastic_data,
        }
        self._model = model
        self._logger = model.python_logger
        self._skip_comments = skip_comments

    def _map_zone_type_with_material(self):
        if self._zone_data is None:
            return
        for zone in self._zone_data:
            zone_details = self._zone_data[zone]
            if 'Type' not in zone_details:
                self._logger.warning(f'Warning: Type is not specified for zone {zone}')
                continue
            if zone_details['Type'] not in ['Shell', 'Solid', 'Cohesive', 'Beam']:
                self._logger.warning(
                    f"Warning: Type of {zone} in not mapped to "
                    f"material ({zone_details['Type']})"
                )
                self._logger.info(zone_details['Type'])
                continue
            if 'Material' not in zone_details:
                self._logger.warning(f'Warning: Material is not specified for zone {zone}')
                continue
            if zone_details['Type'] == 'Cohesive':
                self._cohezive_zone_thickness_data[zone_details['Material']] = {
                    'ThicknessMode': None,
                    'Thickness': 1.0,
                }
                if 'ThicknessMode' in zone_details:
                    self._cohezive_zone_thickness_data[zone_details['Material']][
                        'ThicknessMode'
                    ] = zone_details['ThicknessMode']
                if 'Thickness' in zone_details:
                    self._cohezive_zone_thickness_data[zone_details['Material']][
                        'Thickness'
                    ] = zone_details['Thickness']
            if zone_details['Material'] in self._material_linked_to_zone_type:
                if self._material_linked_to_zone_type[zone_details['Material']] in [
                    'Shell',
                    'Solid',
                    'beam',
                ]:
                    if zone_details['Type'] == 'Cohesive':
                        self._logger.warning(
                            f"Warning: Material:'{zone_details['Material']}' is used for "
                            f" {zone_details['Type']} and one of these [Shell, Solid, beam]"
                        )
                elif self._material_linked_to_zone_type[zone_details['Material']] == 'Cohesive':
                    if zone_details['Type'] in ['Shell', 'Solid', 'beam']:
                        self._logger.warning(
                            f"Warning: Material:'{zone_details['Material']}' is used for "
                            f"{zone_details['Type']} and cohesive"
                        )
            else:
                self._material_linked_to_zone_type[zone_details['Material']] = zone_details['Type']

    def get_all_material_commands(self):
        mapdl_text_data_list = []
        self._map_zone_type_with_material()
        for material in self._raw_materials_data:
            if material not in self._material_linked_to_zone_type:
                self._material_linked_to_zone_type[material] = None
            # self._logger.info(f"Processing Material: {material}")
            mapdl_text_data = self._get_mat_comands(material)
            mapdl_text_data_list.append(mapdl_text_data)
        return '\n\n'.join(mapdl_text_data_list)

    def _get_mat_comands(self, material):
        mat_data = self._raw_materials_data[material]
        self._mat_id = mat_data['id']
        processed_entities = [
            'DENSITY',
            'ELASTIC',
            'PLASTIC',
            'Parameters',
            "HYPERELASTIC",
            "DAMPING",
            "EXPANSION",
            'DAMAGE INITIATION',
            'DAMAGE EVOLUTION',
            'HYPERFOAM',
            'VISCOELASTIC',
        ]
        # self._logger.info(mat_data)
        mapdl_text_data = ""
        hm_comment = self._enable_hm_comments and self._skip_comments is False
        if hm_comment:
            mapdl_text_data += "!!HMNAME MAT \n"
            mapdl_text_data += f'!!{self._mat_id:>10} "{material}"\n'
        else:
            mapdl_text_data += f"! material '{material}' \n"
        if "Parameters" in mat_data:
            self._logger.warning(f"Parameter on Material {material} are not processed.")
        for prop in mat_data:
            if prop == 'id':
                continue
            elif prop not in processed_entities:
                if prop not in ['HMComments', 'Comments', "UNIAXIAL TEST DATA"]:
                    self._logger.warning(
                        f"The property {prop} for Material {material} is not processed."
                    )
                continue
            function = self._property_function_map[prop]
            mapdl_text_data += function(mat_data[prop], material, self._mat_id)
        return mapdl_text_data

    def get_material_commands_by_material_name(self, mat_name):
        self._map_zone_type_with_material()
        if mat_name not in self._material_linked_to_zone_type:
            self._material_linked_to_zone_type[mat_name] = None
        mapdl_text_data = self._get_mat_comands(mat_name)
        mat_data = self._raw_materials_data[mat_name]
        # self._logger.info(mat_data)
        return mapdl_text_data

    def get_material_commands_by_material_id(self, id):
        self._map_zone_type_with_material()
        mapdl_text_data = ''
        for material in self._raw_materials_data:
            # self._logger.info(f"Processing Material: {material}")
            mat_data = self._raw_materials_data[material]
            if mat_data['id'] == id:
                if material not in self._material_linked_to_zone_type:
                    self._material_linked_to_zone_type[material] = None
                mapdl_text_data = self._get_mat_comands(material)
                break
        return mapdl_text_data

    def _process_damage_initiation_data(self, property_dict, material, mat_id):

        damage_init_data = ''

        data = []
        parameters = []

        if self._material_linked_to_zone_type[material] == 'Cohesive':
            return ''

        if 'Parameters' in property_dict and property_dict['Parameters'] is not None:
            parameters = property_dict['Parameters']
        if 'Data' in property_dict and property_dict['Data'] is not None:
            data = property_dict['Data']
        if 'DEPENDENCIES' in parameters:
            self._logger.warning(
                f"*DAMAGE INITIATION has argument DEPENDENCIES. "
                f"*DAMAGE INITIATION is not processed for material {material}"
            )
            return ''

        if parameters["CRITERION"] != "DUCTILE":
            self._logger.warning(
                f"*DAMAGE INITIATION has argument Criteron-{parameters['CRITERION']}. "
                f"*DAMAGE INITIATION is not processed for material {material}"
            )
            return ''
        if parameters["CRITERION"] == "DUCTILE":
            f_strain = [None]
            t_stress = [None]
            if "Equivalent fracture strain at damage initiation" in data:
                f_strain = data["Equivalent fracture strain at damage initiation"]
            if "Stress triaxiality" in data:
                t_stress = data["Stress triaxiality"]
            strain_rate = [None] * len(f_strain)
            temperature = [None] * len(f_strain)
            if "Strain rate" in data:
                strain_rate = data["Strain rate"]
            if "Temperature" in data:
                temperature = data["Temperature"]

            if len(temperature) != len(f_strain) or len(strain_rate) != len(f_strain):
                self._logger.warning(
                    f"Inconsistent temperature/strain_rate data on *DAMAGE INITIATION."
                    f"*DAMAGE INITIATION is not processed for material {material}"
                )
                return ''

            damage_init_data += f"TB, CDM, {mat_id},,,DUCT\n"
            for fs, ts, sr, temp in zip(f_strain, t_stress, strain_rate, temperature):
                if temp is not None:
                    damage_init_data += f"TBTEMP,{temp}\n"
                damage_init_data += f"TBPT, DEFI, {ts}, {fs}\n"
            damage_init_data += "\n"
        return damage_init_data

    def get_weight_factor(self, mat_id, material):
        weight_sum = 0
        weight_factor = 1
        all_mat_props = self._raw_materials_data[material]
        if 'VISCOELASTIC' not in all_mat_props:
            return weight_factor
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

            if len(plastic_data.keys()) > 1:
                self._logger.warning(
                    f"More than one temperature data is provided in the material "
                    f"(ID : {mat_id} Name: {material}). Please verify the material data."
                )
            for tb_temp, data_temp in plastic_data.items():

                data_for_temp = sorted(data_temp, key=lambda x: x[0])
                for count, plst_data in enumerate(data_for_temp):
                    weight_sum += float(plst_data[0])

            if weight_sum > 1:
                self._logger.warning(
                    f"Weight sum of the hyperleastic material {material} is more than 1"
                )
            weight_factor = 1 / (1 - weight_sum)
            # self._logger.info(f"weight_factor1 {weight_factor}")
            return weight_factor
        else:
            self._logger.warning(
                f"The visco-elasticity available in the material "
                f"(ID : {mat_id} Name: {material}) is not translated. "
                f"Only Prony series is supported."
            )
            return weight_factor

    def _process_viscoelastic_data(self, property_dict, material, mat_id):
        viscoelastic_data = ''

        if (
            property_dict["Parameters"]
            and "TIME" in property_dict["Parameters"]
            and property_dict["Parameters"]["TIME"] == "PRONY"
        ):
            g = property_dict["Data"]['g']
            if 'k' in property_dict["Data"]:
                k = property_dict["Data"]['k']
            else:
                k = [0.0] * len(g)
            if 't' in property_dict["Data"]:
                t = property_dict["Data"]['t']
            else:
                t = [0.0] * len(g)
            plastic_data = {}
            for pnt in zip(g, k, t):
                if float(pnt[1]) in plastic_data.keys():
                    plastic_data[float(pnt[1])].append([float(pnt[0]), float(pnt[2])])
                else:
                    plastic_data[float(pnt[1])] = [[float(pnt[0]), float(pnt[2])]]

            if len(plastic_data.keys()) > 1:
                self._logger.warning(
                    f"More than one temperature data is provided in the material "
                    f"(ID : {mat_id} Name: {mat_name}). Please verify the material data."
                )

            key = list(plastic_data.keys())[0]
            data = plastic_data[key]

            viscoelastic_data += f"TB, PRONY, {mat_id},,,SHEAR\n"
            for g, t in data:
                viscoelastic_data += f"TBDATA,, {g}, {t}\n"
            viscoelastic_data += "\n"

            viscoelastic_data += f"TB, PRONY, {mat_id},,,BULK\n"
            for g, t in data:
                viscoelastic_data += f"TBDATA,, {g}, {t}\n"
            viscoelastic_data += "\n"

        else:
            self._logger.warning(
                f"Only TIME=PRONY is processed for VISCOELASTIC material. "
                f"Material {material} is not processed completely."
            )

        return viscoelastic_data

    def _process_hyperfoam_data(self, property_dict, material, mat_id):
        hyperfoam_data = ''
        data = []
        parameters = []
        if 'Parameters' in property_dict and property_dict['Parameters'] is not None:
            parameters = property_dict['Parameters']
        if 'Data' in property_dict and property_dict['Data'] is not None:
            data = property_dict['Data']
        n = 1
        if 'N' in parameters:
            n = int(parameters['N'])
        poisson = None
        if 'POISSON' in parameters:
            poisson = float(parameters['POISSON'])
        if 'TEST DATA INPUT' in parameters:
            uniaxial_test_data = []
            if 'UNIAXIAL TEST DATA' in self._raw_materials_data[material]:
                if 'Data' in self._raw_materials_data[material]['UNIAXIAL TEST DATA']:
                    uniaxial_test_data = self._raw_materials_data[material]['UNIAXIAL TEST DATA'][
                        'Data'
                    ]
            hyperfoam_data = self._hyperfoam_with_test_data(n, uniaxial_test_data, poisson, mat_id)
        else:
            weight_factor = 1
            if not ('MODULI' in parameters and parameters['MODULI'] == 'INSTANTANEOUS'):
                weight_factor = self.get_weight_factor(mat_id, material)
            hyperfoam_data = self._hyperfoam_with_coeffs(n, data, mat_id, weight_factor)
        return hyperfoam_data

    def _hyperfoam_with_coeffs(self, n, data, mat_id, weight_factor):
        hyperfoam_coeff_data = ''
        data = {
            k: [float(x) for x in v if x is not None] if v is not None else None
            for k, v in data.items()
        }
        u1 = data['u1']
        a1 = data['a1']
        v1 = [0.0] * len(u1)
        if 'v1' in data and data['v1'] is not None:
            v1 = data['v1']
        if n > 1:
            u2 = data['u2']
            a2 = data['a2']
            v2 = [0.0] * len(u2)
            if 'v2' in data and data['v2'] is not None:
                v2 = data['v2']
        if n > 2:
            u3 = data['u3']
            a3 = data['a3']
            v3 = [0.0] * len(u3)
            if 'v3' in data and data['v3'] is not None:
                v3 = data['v3']
        if n > 3:
            u4 = data['u4']
            a4 = data['a4']
            v4 = [0.0] * len(u4)
            if 'v4' in data and data['v4'] is not None:
                v4 = data['v4']
        if n > 4:
            u5 = data['u5']
            a5 = data['a5']
            v5 = [0.0] * len(u5)
            if 'v5' in data and data['v5'] is not None:
                v5 = data['v5']
        if n > 5:
            u6 = data['u6']
            a6 = data['a6']
            v6 = [0.0] * len(u6)
            if 'v6' in data and data['v6'] is not None:
                v6 = data['v6']
        temperature = [None] * len(u1)
        if 'Temperature' in data:
            temperature = data['Temperature']

        hyperfoam_coeff_data += f"TB, HYPE, {mat_id},,{n},FOAM\n"
        for i in range(len(temperature)):
            if temperature[i] is not None:
                hyperfoam_coeff_data += f"TBTEMP,{temperature[i]}\n"
            u1a = 2 * u1[i] / a1[i] * weight_factor
            a1a = a1[i]
            hyperfoam_coeff_data += f"TBDATA, 1, {u1a}, {a1a}"
            if n > 1:
                u2a = 2 * u2[i] / a2[i] * weight_factor
                a2a = a2[i]
                hyperfoam_coeff_data += f", {u2a}, {a2a}"
            if n > 2:
                u3a = 2 * u3[i] / a3[i] * weight_factor
                a3a = a3[i]
                hyperfoam_coeff_data += f", {u3a}, {a3a}"
            if n > 3:
                u4a = 2 * u4[i] / a4[i] * weight_factor
                a4a = a4[i]
                hyperfoam_coeff_data += "\n"
                hyperfoam_coeff_data += f"TBDATA, 7, {u4a}, {a4a}"
            if n > 4:
                u5a = 2 * u5[i] / a5[i] * weight_factor
                a5a = a5[i]
                hyperfoam_coeff_data += f", {u5a}, {a5a}"
            if n > 5:
                u6a = 2 * u6[i] / a6[i] * weight_factor
                a6a = a6[i]
                hyperfoam_coeff_data += f", {u6a}, {a6a}"
            hyperfoam_coeff_data += "\n"

            b1a = v1[i] / (1 - 2 * v1[i])
            hyperfoam_coeff_data += f"TBDATA, {n*2 + 1}, {b1a}"
            if n > 1:
                b2a = v2[i] / (1 - 2 * v2[i])
                hyperfoam_coeff_data += f", {b2a}"
            if n > 2:
                b3a = v3[i] / (1 - 2 * v3[i])
                hyperfoam_coeff_data += f", {b3a}"
            if n > 3:
                b4a = v4[i] / (1 - 2 * v4[i])
                hyperfoam_coeff_data += f", {b4a}"
            if n > 4:
                b5a = v5[i] / (1 - 2 * v5[i])
                hyperfoam_coeff_data += f", {b5a}"
            if n > 5:
                b6a = v6[i] / (1 - 2 * v6[i])
                hyperfoam_coeff_data += f", {b6a}"
            hyperfoam_coeff_data += "\n"
            hyperfoam_coeff_data += "\n"
        return hyperfoam_coeff_data

    def _hyperfoam_with_test_data(self, n, data, poisson, mat_id):
        stress = data['Nominal stress']
        strain = data['Nominal strain']
        lateral_strain = [0.0] * len(stress)
        lateral_strain_key = (
            "Nominal lateral strain, . Default is zero. Not needed if the POISSON "
            "parameter is specified on the *HYPERFOAM option"
        )
        if lateral_strain_key in data:
            lateral_strain = data[lateral_strain_key]
        if poisson is None:
            poisson = float(lateral_strain[0])
        beta_ansys = poisson / (1 - 2 * poisson)
        hyperfoam_test_to_data = ''
        hyperfoam_test_to_data += f'*create, unia_test_material_{mat_id}.exp\n'
        hyperfoam_test_to_data += f'/1, epto\n'
        hyperfoam_test_to_data += f'/2, s\n'
        for i in range(len(stress)):
            hyperfoam_test_to_data += f'{strain[i]}, {stress[i]}\n'
        hyperfoam_test_to_data += f'*end\n'

        hyperfoam_test_to_data += f"TB, HYPE, {mat_id},,{n},FOAM\n"
        hyperfoam_test_to_data += f"TBTEMP,0\n"

        hyperfoam_test_to_data += f"TBDATA, 1, 1, 1"
        if n > 1:
            hyperfoam_test_to_data += f", 1, 1"
        if n > 2:
            hyperfoam_test_to_data += f", 1, 1"
        if n > 3:
            hyperfoam_test_to_data += "\n"
            hyperfoam_test_to_data += f"TBDATA, 7, 1, 1"
        if n > 4:
            hyperfoam_test_to_data += f", 1, 1"
        if n > 5:
            hyperfoam_test_to_data += f", 1, 1"
        hyperfoam_test_to_data += "\n"

        hyperfoam_test_to_data += f"TBDATA, {n*2 + 1}, {beta_ansys}"
        if n > 1:
            hyperfoam_test_to_data += f", {beta_ansys}"
        if n > 2:
            hyperfoam_test_to_data += f", {beta_ansys}"
        if n > 3:
            hyperfoam_test_to_data += f", {beta_ansys}"
        if n > 4:
            hyperfoam_test_to_data += f", {beta_ansys}"
        if n > 5:
            hyperfoam_test_to_data += f", {beta_ansys}"
        hyperfoam_test_to_data += "\n"

        hyperfoam_test_to_data += f'\n'
        hyperfoam_test_to_data += f'TBFT, EADD, {mat_id}, UNIA, unia_test_material_{mat_id}.exp\n'
        hyperfoam_test_to_data += f'TBFT, FADD, {mat_id}, HYPER, FOAM, {n}\n'
        for i in range(1, n + 1):
            hyperfoam_test_to_data += f'TBFT, SET, {mat_id}, HYPER, FOAM, {n}, {2*i-1}, 0.001\n'
            hyperfoam_test_to_data += f'TBFT, SET, {mat_id}, HYPER, FOAM, {n}, {2*i}, 0.001\n'
        for i in range(1, n + 1):
            hyperfoam_test_to_data += (
                f'TBFT, SET, {mat_id}, HYPER, FOAM, {n}, {2*n+i}, {beta_ansys}\n'
            )
        hyperfoam_test_to_data += f'\n'
        for i in range(1, n + 1):
            hyperfoam_test_to_data += f'TBFT, FIX, {mat_id}, HYPER, FOAM, {n}, {2*n+i}, 1\n'
        hyperfoam_test_to_data += f'\n'
        # hyperfoam_test_to_data += f'TBFT, SET, {mat_id}, HYPER, FOAM, {n}, TREF, 0\n'
        # hyperfoam_test_to_data += f'TBFT, SET, {mat_id}, HYPER, FOAM, {n}, TDEP, 0\n'
        hyperfoam_test_to_data += f'\n'
        hyperfoam_test_to_data += f'TBFT, SOLVE, {mat_id}, HYPER, FOAM, {n}, 1, 100, 0, 0\n'
        hyperfoam_test_to_data += f'\n'
        hyperfoam_test_to_data += f'TBFT, FSET, {mat_id}, HYPER, FOAM, {n}\n'

        return hyperfoam_test_to_data

    def _process_damage_evolution_data(self, property_dict, material, mat_id):

        damage_evol_data = ''

        if self._material_linked_to_zone_type[material] == 'Cohesive':
            return ''

        data = []
        parameters = []

        if 'Parameters' in property_dict and property_dict['Parameters'] is not None:
            parameters = property_dict['Parameters']
        if 'Data' in property_dict and property_dict['Data'] is not None:
            data = property_dict['Data']

        if 'DEPENDENCIES' in parameters:
            self._logger.warning(
                f"*DAMAGE EVOLUTION has argument DEPENDENCIES. "
                f"*DAMAGE EVOLUTION is not processed for material {material}"
            )
            return ''
        if parameters['TYPE'] != "DISPLACEMENT":
            self._logger.warning(
                f"*DAMAGE EVOLUTION has argument TYPE - {parameters['TYPE']}. "
                f"*DAMAGE EVOLUTION is not processed for material {material}"
            )
            return ''
        if "SOFTENING" in parameters and parameters['SOFTENING'] != "LINEAR":
            self._logger.warning(
                f"*DAMAGE EVOLUTION has argument SOFTENING - {parameters['SOFTENING']}. "
                f"*DAMAGE EVOLUTION is not processed for material {material}"
            )
            return ''
        if "DEGRADATION" in parameters and parameters['DEGRADATION'] != "MAXIMUM":
            self._logger.warning(
                f"*DAMAGE EVOLUTION has argument DEGRADATION - {parameters['DEGRADATION']}. "
                f"*DAMAGE EVOLUTION is not processed for material {material}"
            )
            return ''
        if "MIXED MODE BEHAVIOR" in parameters:
            self._logger.warning(
                f"*DAMAGE EVOLUTION has argument MIXED MODE BEHAVIOR. "
                f"*DAMAGE EVOLUTION is not processed for material {material}"
            )
            return ''

        disp_at_failure = []
        disp_str = (
            f"Effective total or plastic displacement at failure, "
            f"measured from the time of damage initiation"
        )
        if disp_str in data:
            disp_at_failure = data[disp_str]

        temperature = [None] * len(disp_at_failure)

        if "Temperature" in data:
            temperature = data['Temperature']

        damage_evol_data += f"TB, CDM, {mat_id},,,LIND\n"
        for disp, temp in zip(disp_at_failure, temperature):
            if temp is not None:
                damage_evol_data += f"TBTEMP,{temp}\n"
            d = disp
            if float(disp) == 0:
                d = '1e-6'
            damage_evol_data += f"TBDATA, 1, {d}\n"
        damage_evol_data += "\n"
        return damage_evol_data

    def _process_expansion_data(self, property_dict, material, mat_id):
        expansion_data = ''
        zero = 0.0
        data = []
        parameters = []
        if 'Parameters' in property_dict and property_dict['Parameters'] is not None:
            parameters = property_dict['Parameters']
        if 'Data' in property_dict and property_dict['Data'] is not None:
            data = property_dict['Data']
        exp_type = 'ISO'
        if 'ZERO' in parameters:
            zero = float(parameters['ZERO'])
        if 'TYPE' in parameters:
            exp_type = parameters['TYPE']
        if 'DEPENDENCIES' in parameters or 'PORE FLUID' in parameters or 'USER' in parameters:
            self._logger.warning(
                f"Arguments PORE FLUID, DEPENDENCIES and USER on "
                f"*EXPANSION are not processed for material {material}"
            )
            return ''
        if exp_type == 'SHORT FIBER' or exp_type == 'ANISO':
            self._logger.warning(
                f"*EXPANSION of type SHORT FIBER and ANISO are "
                f"not processed for material {material}."
            )
            return ''
        if 'ZERO' in parameters:
            expansion_data += f"MP,REFT,{mat_id},{zero}\n"
        if exp_type == 'ISO':
            temperature = [None]
            ctes = [None]
            if 'Temperature' in data:
                temperature = data['Temperature']
            if 'A' in data:
                ctes = data['A']
            expansion_data += f"TB, CTE, {mat_id},,,\n"
            for temp, cte in zip(temperature, ctes):
                if temp is not None:
                    expansion_data += f"TBTEMP,{temp}\n"
                expansion_data += f"TBDATA, 1, {cte}\n"
        if exp_type == 'ORTHO':
            if 'A11' in data:
                ctexs = data['A11']
            cteys = ['0.0'] * len(ctexs)
            if 'A22' in data:
                cteys = data['A22']
            ctezs = ['0.0'] * len(ctexs)
            if 'A33' in data:
                ctezs = data['A33']
            temperature = [None] * len(ctexs)
            if 'Temperature' in data:
                temperature = data['Temperature']
            expansion_data += f"TB, CTE, {mat_id},,,\n"
            for temp, ctex, ctey, ctez in zip(temperature, ctexs, cteys, ctezs):
                if temp is not None:
                    expansion_data += f"TBTEMP,{temp}\n"
                expansion_data += f"TBDATA, 1, {ctex}, {ctey}, {ctez}\n"
            expansion_data += "\n"
        return expansion_data

    def _process_damping_data(self, property_dict, material, mat_id):
        damping_data = ''
        if property_dict['Parameters'] is None:
            self._logger.warning(f"*DAMPING does not have parameters to process.")
        else:
            if 'ALPHA' in property_dict['Parameters']:
                damping_data += f"MP, ALPD, {mat_id}, {property_dict['Parameters']['ALPHA']} \n"
            if float(property_dict['Parameters']['BETA']) != 0.0:
                damping_data += f"MP, BETD, {mat_id}, {property_dict['Parameters']['BETA']} \n"
            if float(property_dict['Parameters']['COMPOSITE']) != 0.0:
                self._logger.warning(f"Parameter {'COMPOSITE'} on *DAMPING is not processed.")
        damping_data += f"\n"
        return damping_data

    def _process_density(self, property_dict, material, mat_id):
        density_data = ''
        data = []
        if 'Data' in property_dict and property_dict['Data'] is not None:
            data = property_dict['Data']
        if "Parameters" in property_dict and property_dict['Parameters'] is not None:
            self._logger.warning(f"Parameter on *DENSITY are not processed.")
        density = data['Mass density']
        if 'Temperature' in data:
            temperature = data['Temperature']
            if len(density) != len(temperature):
                self._logger.warning(
                    f"data values on *DENSITY are not consistent for material {material}."
                )
        if len(density) > 1:
            self._logger.warning(
                f"there are multiple data values on *DENSITY, "
                f"use MPTEMP and MPDATA to define the material property."
                f"Density is not processed correctly for material {material}"
            )
            density_data += f"MP,DENS,{mat_id},{density[0]}\n"
        else:
            density_data += f"MP,DENS,{mat_id},{density[0]}\n"
        density_data += f"\n"
        return density_data

    def _process_elastic_modulus(self, property_dict, material, mat_id):
        elastic_modulus = ''
        data = []
        if 'Data' in property_dict and property_dict['Data'] is not None:
            data = property_dict['Data']
        if (
            property_dict["Parameters"]["TYPE"] == "ISOTROPIC"
            or property_dict["Parameters"]["TYPE"] == "ISO"
        ):
            # self._logger.warning(f"Only isotropic elastic modulus is processed, "
            # f"Elastic Modulus for the material {material} "
            #       f"is not processed.")
            # return ''
            youngs_mod = data['E']
            nu = data['V']
            # temperature = data['Temperature']
            if 'Temperature' in data:
                temperature = data['Temperature']
                if len(youngs_mod) != len(temperature):
                    self._logger.warning(
                        f"data values on *ELASTIC are not consistent for material {material}."
                    )
            if len(youngs_mod) != len(nu):
                self._logger.warning(
                    f"data values on *ELASTIC are not consistent for material {material}."
                )
            if len(youngs_mod) > 1:
                self._logger.warning(
                    f"there are multiple data values on *ELASTIC, "
                    f"use MPTEMP and MPDATA to define the material property."
                    f"elastic properties are not processed correctly "
                    f"for material {material}"
                )
                if self._material_linked_to_zone_type[material] == 'Cohesive':
                    elastic_modulus += f"TB, ELAS, {mat_id}, 1, 2,ISOT\n"
                    elastic_modulus += f"TBDATA, 1, {youngs_mod[0]}, {nu[0]}\n"
                    # elastic_modulus += f"TB, GASKET, {mat_id}, 1, 2,elas\n"
                    # elastic_modulus += f"TBDATA, 1, {youngs_mod[0]}, {nu[0]}\n"
                else:
                    elastic_modulus += f"MP,EX,{mat_id},{youngs_mod[0]}\n"
                    elastic_modulus += f"MP,NUXY,{mat_id},{nu[0]}\n"
            else:
                if self._material_linked_to_zone_type[material] == 'Cohesive':
                    elastic_modulus += f"TB, ELAS, {mat_id}, 1, 2,ISOT\n"
                    elastic_modulus += f"TBDATA, 1, {youngs_mod[0]}, {nu[0]}\n"
                    # elastic_modulus += f"TB, GASKET, {mat_id}, 1, 2,elas\n"
                    # elastic_modulus += f"TBDATA, 1, {youngs_mod[0]}, {nu[0]}\n"
                else:
                    elastic_modulus += f"MP,EX,{mat_id},{youngs_mod[0]}\n"
                    elastic_modulus += f"MP,NUXY,{mat_id},{nu[0]}\n"
            elastic_modulus += f"\n"
        elif property_dict["Parameters"]["TYPE"] == "TRACTION":
            if self._material_linked_to_zone_type[material] != 'Cohesive':
                self._logger.warning(
                    f"Elastic Modulus with type = TRACTION is defined "
                    f"for non cohesive material {material}, "
                    f" this is not processed."
                )
                return ''
            knn = data['E/Knn']
            kss = data['G1/Kss']
            ktt = data['G2/Ktt']
            t = self._cohezive_zone_thickness_data[material]['Thickness']
            # temperature = data['Temperature']
            if 'Temperature' in data:
                temperature = data['Temperature']
                if len(knn) != len(temperature):
                    self._logger.warning(
                        f"data values on *ELASTIC are not consistent for material {material}."
                    )
            if len(knn) != len(kss):
                self._logger.warning(
                    f"data values on *ELASTIC are not consistent for material {material}."
                )
            if len(knn) > 1:
                self._logger.warning(
                    f"there are multiple data values on *ELASTIC, "
                    f"use MPTEMP and MPDATA to define the material property."
                    f"elastic properties are not processed correctly "
                    f"for material {material}"
                )
            c1 = _TractionProperties.NOM_STRESS_1
            c3 = _TractionProperties.NOM_STRESS_2
            dt = c3 / float(kss[0]) * t
            dn = c1 / float(knn[0]) * t
            c2 = _TractionProperties.DAMAGE_EVOLUTION_ENERGY + dn
            c4 = _TractionProperties.DAMAGE_EVOLUTION_ENERGY + dt
            c5 = dn / c2
            elastic_modulus += f"TB,CZM,{mat_id},1,,BILI \n"
            elastic_modulus += f"TBDATA,1,{c1},{c2},{c3},{c4},{c5},"
        else:
            self._logger.warning(
                f"Elastic Modulus with type = "
                f"{property_dict['Parameters']['TYPE']} is not processed."
            )
            return ''
        return elastic_modulus

    def _process_plastic_data(self, property_dict, material, mat_id):
        plastic_data = ''
        data = []
        if 'Data' in property_dict and property_dict['Data'] is not None:
            data = property_dict['Data']
        if property_dict["Parameters"]["HARDENING"] != "ISOTROPIC":
            self._logger.warning(
                f"Only HARDENING=ISOTROPIC is processed, "
                f"*PLASTIC for the material {material} "
                f"is not processed."
            )
            return ''
        if self._material_linked_to_zone_type[material] == 'Cohesive':
            return ''
        strains = data['Plastic strain']
        stresses = data['Yield stress']
        # temperature = data['Temperature']
        data_points = len(strains)
        skip_temp = False
        if 'Temperature' in data:
            temperature = data['Temperature']
            unique_temperatures = len(list(set(temperature)))
            data_points = len(strains) / unique_temperatures
            if len(stresses) != len(temperature):
                self._logger.warning(
                    f"data values on *PLASTIC are not consistent for material {material}. "
                    f"Please check the material properties in the cdb file created"
                )
                skip_temp = True
        if len(stresses) != len(strains):
            self._logger.warning(
                f"data values on *PLASTIC are not consistent for material {material}."
            )
        plastic_data += f"TB,PLAS,{mat_id},,{int(data_points)},MISO\n"
        curr_temp = None
        for i, strain in enumerate(strains):
            if 'Temperature' in data and not skip_temp:
                if curr_temp != temperature[i]:
                    curr_temp = temperature[i]
                    plastic_data += f"TBTEMP,{curr_temp}\n"
            plastic_data += f"TBPT,,{strain},{stresses[i]}\n"
        plastic_data += f"\n"
        return plastic_data

    def _process_hyperelastic_data(self, property_dict, material, mat_id):
        hyperelastic_data = ''
        param_keys = property_dict["Parameters"].keys()
        parameters = property_dict["Parameters"]
        data = []

        weight_factor = 1
        if not ('MODULI' in parameters and parameters['MODULI'] == 'INSTANTANEOUS'):
            weight_factor = self.get_weight_factor(mat_id, material)

        if 'Data' in property_dict and property_dict['Data'] is not None:
            data = property_dict['Data']
        if (
            'REDUCED POLYNOMIAL' not in param_keys
            and 'YEOH' not in param_keys
            and 'NEO HOOKE' not in param_keys
            and 'POLYNOMIAL' not in param_keys
        ):
            self._logger.warning(
                f"Only parameter REDUCED POLYNOMIAL, "
                f"YEOH and NEO HOOKE is processed, "
                f"there are more parameters on *HYPERELASTIC,*HYPERELASTIC "
                f"for material {material} is not processed."
            )
            return ''
        if self._material_linked_to_zone_type[material] == 'Cohesive':
            return ''
        if 'NEO HOOKE' in param_keys:
            if 'Temperature' in data:
                temperature = data['Temperature']
                temp_data_points = len(temperature)
            else:
                self._logger.warning(
                    f"temperature is not provided for HYPERELASTIC material: {material}."
                )
                temp_data_points = 1
                temperature = [None]
            if 'C10' in data.keys():
                c10 = data['C10']
                if 'D1' in data.keys():
                    d1 = data['D1']
                else:
                    d1 = [0.0] * len(c10)
            hyperelastic_data += f"TB,HYPE,{mat_id},,,NEO\n"
            for i in range(len(temperature)):
                if temperature[i] is not None:
                    hyperelastic_data += f"TBTEMP, {temperature[i]}\n"
                hyperelastic_data += f"TBDATA, 1, {float(c10[i])*2}, {d1[i]}\n"
        if 'REDUCED POLYNOMIAL' in param_keys or 'YEOH' in param_keys:
            if 'Temperature' in data:
                temperature = data['Temperature']
                temp_data_points = len(temperature)
            else:
                self._logger.warning(
                    f"temperature is not provided for HYPERELASTIC material: {material}."
                )
                temp_data_points = 1
                temperature = [None]
            number_of_constants = 3
            data = {
                k: [float(x) for x in v if x is not None] if v is not None else None
                for k, v in data.items()
            }
            if 'C10' in data.keys():
                number_of_constants = 1
                c10 = data['C10']
                if 'D1' in data.keys():
                    d1 = data['D1']
                else:
                    d1 = [0.0] * len(c10)
            if 'C20' in data.keys():
                number_of_constants = 2
                c20 = data['C20']
                if 'D2' in data.keys():
                    d2 = data['D2']
                else:
                    d2 = [0.0] * len(c20)
            if 'C30' in data.keys():
                number_of_constants = 3
                c30 = data['C30']
                if 'D3' in data.keys():
                    d3 = data['D3']
                else:
                    d3 = [0.0] * len(c30)
            hyperelastic_data += f"TB,HYPE,{mat_id},,{number_of_constants},YEOH\n"
            for i in range(len(temperature)):
                if temperature[i] is not None:
                    hyperelastic_data += f"TBTEMP, {temperature[i]}\n"
                if number_of_constants == 1:
                    hyperelastic_data += f"TBDATA, 1, {c10[i]*weight_factor}, {d1[i]}\n"
                elif number_of_constants == 2:
                    hyperelastic_data += f"TBDATA, 1, {c10[i]*weight_factor}, "
                    hyperelastic_data += f"{c20[i]*weight_factor}, {d1[i]}, {d2[i]}\n"
                elif number_of_constants == 3:
                    hyperelastic_data += (
                        f"TBDATA, 1, {c10[i]*weight_factor}, {c20[i]*weight_factor}, "
                        f"{c30[i]*weight_factor}, {d1[i]}, {d2[i]}, {d3[i]}\n"
                    )
                else:
                    pass
        if 'POLYNOMIAL' in param_keys:
            if 'Temperature' in data:
                temperature = data['Temperature']
                temp_data_points = len(temperature)
            else:
                self._logger.warning(
                    f"temperature is not provided for HYPERELASTIC material: {material}."
                )
                temp_data_points = 1
                temperature = [None]
            number_of_constants = 3
            if 'C10' in data.keys():
                number_of_constants = 1
                c10 = data['C10']
                if 'D1' in data.keys():
                    d1 = data['D1']
                else:
                    d1 = [0.0] * len(c10)
                if 'C01' in data.keys():
                    c01 = data['C01']
                else:
                    c01 = [0.0] * len(c10)

            if 'C20' in data.keys():
                number_of_constants = 2
                c20 = data['C20']
                if 'D2' in data.keys():
                    d2 = data['D2']
                else:
                    d2 = [0.0] * len(c20)
                if 'C02' in data.keys():
                    c02 = data['C02']
                else:
                    c02 = [0.0] * len(c20)
                if 'C11' in data.keys():
                    c11 = data['C11']
                else:
                    c11 = [0.0] * len(c20)

            if 'C30' in data.keys():
                number_of_constants = 3
                c30 = data['C30']
                if 'D3' in data.keys():
                    d3 = data['D3']
                else:
                    d3 = [0.0] * len(c30)
                if 'C03' in data.keys():
                    c03 = data['C03']
                else:
                    c03 = [0.0] * len(c30)
                if 'C21' in data.keys():
                    c21 = data['C21']
                else:
                    c21 = [0.0] * len(c30)
                if 'C12' in data.keys():
                    c12 = data['C12']
                else:
                    c12 = [0.0] * len(c30)
            order_N = number_of_constants
            if "N" in param_keys:
                order_N = int(property_dict["Parameters"]["N"])
            if order_N > 3:
                self._logger.warning(
                    f"HYPERELASTIC material order (N) "
                    f"greater than 3 is not processed.: {material}."
                )
                return hyperelastic_data

            hyperelastic_data += f"TB,HYPE,{mat_id},,{number_of_constants},POLY\n"

            for i in range(len(temperature)):
                if temperature[i] is not None:
                    hyperelastic_data += f"TBTEMP, {temperature[i]}\n"
                if number_of_constants == 1:
                    hyperelastic_data += f"TBDATA, 1, {c10[i]}, {c01[i]}, {d1[i]}\n"
                elif number_of_constants == 2:
                    hyperelastic_data += (
                        f"TBDATA, 1, {c10[i]}, {c01[i]}, {c20[i]}, {c11[i]}, {c02[i]}, {d1[i]}\n"
                    )
                    hyperelastic_data += f"TBDATA, 7, {d2[i]}\n"
                elif number_of_constants == 3:
                    hyperelastic_data += (
                        f"TBDATA, 1, {c10[i]}, {c01[i]}, {c20[i]}, {c11[i]}, {c02[i]}, {c30[i]}\n"
                    )
                    hyperelastic_data += (
                        f"TBDATA, 7, {c21[i]}, {c12[i]}, {c03[i]}, {d1[i]}, {d2[i]}, {d3[i]}\n"
                    )
                else:
                    pass
        # if 'REDUCED POLYNOMIAL' in param_keys:
        #     if 'Temperature' in data:
        #         temperature = data['Temperature']
        #         temp_data_points = len(temperature)
        #     else:
        #         self._logger.warning(
        # f"temperature is not provided for HYPERELASTIC material: {material}."
        # )
        #         temp_data_points = 1
        #         temperature = [None]
        hyperelastic_data += f"\n"
        # self._logger.info(hyperelastic_data)
        return hyperelastic_data


class _JointMaterialProcessor:
    __slots__ = (
        '_raw_joint_materials_data',
        '_mat_id',
        '_enable_hm_comments',
        '_property_function_map',
        '_model',
        '_logger',
        '_skip_comments',
    )

    def __init__(
        self, model: prime.Model, raw_joint_materials_data, hm_comments=False, skip_comments=True
    ):
        self._raw_joint_materials_data = raw_joint_materials_data
        self._mat_id = 0
        self._enable_hm_comments = hm_comments
        self._property_function_map = {
            'CONNECTOR ELASTICITY': self._process_elasticity,
            'CONNECTOR DAMPING': self._process_damping,
        }
        self._model = model
        self._logger = model.python_logger
        self._skip_comments = skip_comments

    def get_all_material_commands(self):
        mapdl_text_data_list = []
        if self._raw_joint_materials_data:
            for material in self._raw_joint_materials_data:
                self._logger.info(f"Processing Material: {material}")
                mapdl_text_data = self._get_mat_comands(material)
                mapdl_text_data_list.append(mapdl_text_data)
        return '\n\n'.join(mapdl_text_data_list)

    def _get_mat_comands(self, material):
        mat_data = self._raw_joint_materials_data[material]
        self._mat_id = mat_data['id']
        processed_entities = ['CONNECTOR ELASTICITY', 'CONNECTOR DAMPING']
        # self._logger.info(mat_data)
        mapdl_text_data = ""
        hm_comment = self._enable_hm_comments and self._skip_comments is False
        if hm_comment:
            mapdl_text_data += "!!HMNAME MAT \n"
            mapdl_text_data += f'!!{self._mat_id:>10} "{material}"\n'
        else:
            mapdl_text_data += f"! material '{material}' \n"
        if "Parameters" in mat_data:
            self._logger.warning(f"Parameter on Material {material} are not processed.")
        for prop in mat_data:
            if prop == 'id' or prop == "CONNECTOR CONSTITUTIVE REFERENCE":
                continue
            elif prop not in processed_entities:
                if prop not in ['HMComments', 'Comments']:
                    self._logger.warning(
                        f"The property {prop} for Material {material} is not processed."
                    )
                continue
            function = self._property_function_map[prop]
            mapdl_text_data += function(mat_data[prop], material, self._mat_id)
        return mapdl_text_data

    def get_material_commands_by_material_name(self, mat_name):
        mapdl_text_data = self._get_mat_comands(mat_name)
        mat_data = self._raw_joint_materials_data[mat_name]
        # self._logger.info(mat_data)
        return mapdl_text_data

    def get_material_commands_by_material_id(self, id):
        mapdl_text_data = ''
        for material in self._raw_joint_materials_data:
            # self._logger.info(f"Processing Material: {material}")
            mat_data = self._raw_joint_materials_data[material]
            if mat_data['id'] == id:
                mapdl_text_data = self._get_mat_comands(material)
                break
        return mapdl_text_data

    def get_new_point(self, pt_d, d1, f1, d2, f2):
        new_f = f1 + (pt_d - d1) * (f1 - f2) / (d1 - d2)
        new_d = pt_d
        return new_d, new_f

    def _process_elasticity(self, property_dict, material, mat_id):
        comps_linear_mapping = {
            '1': '1',
            '2': '7',
            '3': '12',
            '4': '16',
            '5': '19',
            '6': '21',
        }
        comps_nonlinear_mapping = {
            '1': 'JNS1',
            '2': 'JNS2',
            '3': 'JNS3',
            '4': 'JNS4',
            '5': 'JNS5',
            '6': 'JNS6',
        }
        all_linear = True
        for comp_data in property_dict:
            if 'Parameters' not in comp_data:
                self._logger.warning(
                    f"Parameter on Connector elasticity for "
                    f"Material {material} is not available."
                )
            else:
                if 'NONLINEAR' in comp_data['Parameters']:
                    all_linear = False
                    break
        all_rigid = True
        for comp_data in property_dict:
            if 'Parameters' not in comp_data:
                self._logger.warning(
                    f"Parameter on Connector elasticity for "
                    f"Material {material} is not available."
                )
            else:
                if 'RIGID' not in comp_data['Parameters']:
                    all_rigid = False
                    break
        elasticity_data = ''
        if all_linear or all_rigid:
            elasticity_data += f"TB, JOIN, {mat_id}, 1,, STIF\n"
        if not all_rigid:
            diagonal_stiffness = ["1", "2", "3", "4", "5", "6"]
            for comp_data in property_dict:
                # self._logger.info(comp_data)
                if 'Parameters' not in comp_data:
                    self._logger.warning(
                        f"Parameter on Connector elasticity for "
                        f"Material {material} is not available."
                    )
                else:
                    if 'RIGID' in comp_data['Parameters']:
                        ff = comps_linear_mapping[comp_data['Parameters']['COMPONENT']]
                        elasticity_data += f"TBDATA, {ff}, 1e6\n"
                        continue
                    if 'NONLINEAR' in comp_data['Parameters']:
                        relative_disp = comp_data['Data']["Displacement"]
                        relative_disp = [float(i) for i in relative_disp]
                        stiff = comp_data['Data']["Load"]
                        stiff = [float(i) for i in stiff]
                        if 'temperature' in comp_data['Data']:
                            temperatures = comp_data['Data']["temperature"]
                            if len(temperatures) != len(stiff):
                                self._logger.warning(
                                    f"Data for Connector elasticity for Material {material}, "
                                    f"is not conststent with tempereture, "
                                    f"values are not processed"
                                )
                            else:
                                temp_val = None
                                elasticity_temporary_data = ""
                                starts_with_negative = False
                                reached_positive = False
                                sign_changed = False
                                super_counter = 0
                                counter = 0
                                point_added = False
                                for d, f, t in zip(relative_disp, stiff, temperatures):
                                    if temp_val != float(t):
                                        counter = 0
                                    if (
                                        sign_changed == False
                                        and counter == 0
                                        and super_counter != 0
                                    ):
                                        d_temp, f_temp = self.get_new_point(
                                            1e-5,
                                            relative_disp[super_counter - 2],
                                            stiff[super_counter - 2],
                                            relative_disp[super_counter - 1],
                                            stiff[super_counter - 1],
                                        )
                                        elasticity_temporary_data += f"TBPT,,{d_temp},{f_temp}\n"
                                        point_added = True
                                    if temp_val != float(t):
                                        elasticity_temporary_data += f"TBTEMP, {t}\n"
                                        starts_with_negative = False
                                        reached_positive = False
                                        sign_changed = False
                                        counter = 0
                                        point_added = False
                                        temp_val = float(t)
                                    if counter == 0 and d < 0:
                                        starts_with_negative = True
                                    elif counter == 0 and d >= 0:
                                        d_temp, f_temp = self.get_new_point(
                                            -1e-5,
                                            relative_disp[super_counter],
                                            stiff[super_counter],
                                            relative_disp[super_counter + 1],
                                            stiff[super_counter + 1],
                                        )
                                        elasticity_temporary_data += f"TBPT,,{d_temp},{f_temp}\n"
                                        point_added = True
                                    elif d == 0 and starts_with_negative == True:
                                        reached_positive = True
                                    if d >= 0:
                                        sign_changed = True
                                    elasticity_temporary_data += f"TBPT,,{d},{f}\n"
                                    if reached_positive:
                                        d_temp, f_temp = self.get_new_point(
                                            1e-5, d_previous, f_previous, d, f
                                        )
                                        elasticity_temporary_data += f"TBPT,,{d_temp},{f_temp}\n"
                                        reached_positive = False
                                        point_added = True
                                    d_previous = d
                                    f_previous = f
                                    counter += 1
                                    super_counter += 1
                                if sign_changed == False:
                                    d_temp, f_temp = self.get_new_point(
                                        1e-5,
                                        relative_disp[-2],
                                        stiff[-2],
                                        relative_disp[-1],
                                        stiff[-1],
                                    )
                                    elasticity_temporary_data += f"TBPT,,{d_temp},{f_temp}\n"
                                    point_added = True
                                if point_added == False:
                                    points = int(len(stiff) / len(list(set(temperatures))))
                                else:
                                    points = int(len(stiff) / len(list(set(temperatures)))) + 1
                                clms = comps_nonlinear_mapping[comp_data['Parameters']['COMPONENT']]
                                elasticity_data += f"TB, JOIN, {mat_id}, , {points}, {clms}\n"
                                elasticity_data += elasticity_temporary_data
                        else:
                            elasticity_temporary_data = ""
                            starts_with_negative = False
                            reached_positive = False
                            sign_changed = False
                            counter = 0
                            point_added = False
                            for d, f in zip(relative_disp, stiff):
                                if counter == 0 and d < 0:
                                    starts_with_negative = True
                                elif counter == 0 and d >= 0:
                                    d_temp, f_temp = self.get_new_point(
                                        -1e-5,
                                        relative_disp[0],
                                        stiff[0],
                                        relative_disp[1],
                                        stiff[1],
                                    )
                                    elasticity_temporary_data += f"TBPT,,{d_temp},{f_temp}\n"
                                    point_added = True
                                elif d == 0 and starts_with_negative == True:
                                    reached_positive = True

                                if d >= 0:
                                    sign_changed = True

                                elasticity_temporary_data += f"TBPT,,{d},{f}\n"

                                if reached_positive:
                                    d_temp, f_temp = self.get_new_point(
                                        1e-5, d_previous, f_previous, d, f
                                    )
                                    elasticity_temporary_data += f"TBPT,,{d_temp},{f_temp}\n"
                                    point_added = True
                                    reached_positive = False
                                d_previous = d
                                f_previous = f
                                counter += 1
                            if sign_changed == False:
                                d_temp, f_temp = self.get_new_point(
                                    1e-5, relative_disp[-2], stiff[-2], relative_disp[-1], stiff[-1]
                                )
                                elasticity_temporary_data += f"TBPT,,{d_temp},{f_temp}\n"
                                point_added = True
                            if point_added == False:
                                points = len(stiff)
                            else:
                                points = len(stiff) + 1
                            clms = comps_nonlinear_mapping[comp_data['Parameters']['COMPONENT']]
                            elasticity_data += f"TB, JOIN, {mat_id}, , {points}, {clms}\n"
                            elasticity_data += elasticity_temporary_data
                    elif not all_linear:
                        if len(comp_data['Data']['Stiffness']) != 1:
                            self._logger.warning(
                                f"Data for Connector elasticity for Material {material}, "
                                f"has multiple stiffness values, "
                                f"tempereture dependent values are not processed"
                            )
                        clms = comps_nonlinear_mapping[comp_data['Parameters']['COMPONENT']]
                        stiff_val = float(comp_data['Data']['Stiffness'][0]) * 1000
                        elasticity_data += f"TB, JOIN, {mat_id}, 1, 3, {clms}\n"
                        elasticity_data += f"TBPT, , -1000.0, -{stiff_val}\n"
                        elasticity_data += "TBPT, , 0.0, 0.0\n"
                        elasticity_data += f"TBPT, , 1000.0, {stiff_val}\n"
                    else:
                        if len(comp_data['Data']['Stiffness']) != 1:
                            self._logger.warning(
                                f"Data for Connector elasticity for Material {material}, "
                                f"has multiple stiffness values, "
                                f"tempereture dependent values are not processed"
                            )
                        clms = comps_linear_mapping[comp_data['Parameters']['COMPONENT']]
                        cds = comp_data['Data']['Stiffness'][0]
                        elasticity_data += f"TBDATA, {clms}, {cds}\n"
                        if comp_data['Parameters']['COMPONENT'] in diagonal_stiffness:
                            diagonal_stiffness.remove(comp_data['Parameters']['COMPONENT'])
            insert_stiffness = os.getenv("MAPDL_JOINT_SMALL_STIFF")
            if (
                insert_stiffness
                and insert_stiffness.lower().strip() == 'true'
                and len(diagonal_stiffness) != 6
            ):
                for component_number in diagonal_stiffness:
                    # if component_number in ['4','5','6']:
                    clms = comps_linear_mapping[component_number]
                    cds = "0.000001"
                    elasticity_data += f"TBDATA, {clms}, {cds}\n"
        else:
            elasticity_data += f"TBDATA,  1, 1e6\n"
            elasticity_data += f"TBDATA,  7, 1e6\n"
            elasticity_data += f"TBDATA, 12, 1e6\n"
            elasticity_data += f"TBDATA, 16, 1e6\n"
            elasticity_data += f"TBDATA, 19, 1e6\n"
            elasticity_data += f"TBDATA, 21, 1e6\n"
        return elasticity_data

    def _process_damping(self, property_dict, material, mat_id):
        # self._logger.info("property_dict: ", property_dict)
        comps_linear_mapping = {
            '1': '1',
            '2': '7',
            '3': '12',
            '4': '16',
            '5': '19',
            '6': '21',
        }
        comps_nonlinear_mapping = {
            '1': 'JND1',
            '2': 'JND2',
            '3': 'JND3',
            '4': 'JND4',
            '5': 'JND5',
            '6': 'JND6',
        }
        all_linear = True
        for comp_data in property_dict:
            if 'Parameters' not in comp_data:
                self._logger.warning(
                    f"Parameter on Connector elasticity for "
                    f"Material {material} is not available."
                )
            else:
                if 'NONLINEAR' in comp_data['Parameters']:
                    all_linear = False
                    break
        damping_data = ''
        if all_linear:
            damping_data += f"TB, JOIN, {mat_id}, 1,, DAMP\n"
        for comp_data in property_dict:
            if 'Parameters' not in comp_data:
                self._logger.warning(
                    f"Parameter on Connector damping for " f"Material {material} is not available."
                )
            else:
                if 'TYPE' in comp_data['Parameters']:
                    if comp_data['Parameters']['TYPE'] != "VISCOUS":
                        self._logger.warning(
                            f"Parameter TYPE on Connector damping for Material {material}"
                            f" is {comp_data['Parameters']['TYPE']}, "
                            f"only TYPE= VISCOUS is processed."
                        )
                if 'NONLINEAR' in comp_data['Parameters']:
                    # self._logger.info('nonlinear')
                    relative_disp = comp_data['Data']["velocity"]
                    damp = comp_data['Data']["force"]
                    if 'temperature' in comp_data['Data']:
                        self._logger.info('nonlinear temp')
                        temperatures = comp_data['Data']["temperature"]
                        if len(temperatures) != len(damp):
                            self._logger.warning(
                                f"Data for Connector elasticity for Material {material}, "
                                f"is not conststent with tempereture, "
                                f"values are not processed"
                            )
                        else:
                            temp_val = None
                            damp_temporary_data = ""
                            for d, f, t in zip(relative_disp, damp, temperatures):
                                if temp_val != float(t):
                                    damp_temporary_data += f"TBTEMP, {t}\n"
                                    temp_val = float(t)
                                damp_temporary_data += f"TBPT,,{d},{f}\n"
                            s1 = int(len(damp) / len(list(set(temperatures))))
                            s2 = comps_nonlinear_mapping[comp_data['Parameters']['COMPONENT']]
                            damping_data += f"TB, JOIN, {mat_id}, , {s1}, {s2}\n"
                            damping_data += damp_temporary_data
                    else:
                        damp_temporary_data = ""
                        for d, f in zip(relative_disp, damp):
                            damp_temporary_data += f"TBPT,,{d},{f}\n"
                        s1 = len(damp)
                        s2 = comps_nonlinear_mapping[comp_data['Parameters']['COMPONENT']]
                        damping_data += f"TB, JOIN, {mat_id}, , {s1}, {s2}\n"
                        damping_data += damp_temporary_data
                    # self._logger.info(damping_data)
                elif not all_linear:
                    # self._logger.info('not all linear')
                    if len(comp_data['Data']['damping_coeff']) != 1:
                        self._logger.warning(
                            f"Data for Connector elasticity for Material {material}, "
                            f"has multiple damping values, "
                            f"tempereture dependent values are not processed"
                        )
                    s1 = comps_nonlinear_mapping[comp_data['Parameters']['COMPONENT']]
                    damp_coeff = float(comp_data['Data']['damping_coeff'][0]) * 1000
                    damping_data += f"TB, JOIN, {mat_id}, 1, 3, {s1}\n"
                    damping_data += f"TBPT, , -1000.0, -{damp_coeff}\n"
                    damping_data += "TBPT, , 0.0, 0.0\n"
                    damping_data += f"TBPT, , 1000.0, {damp_coeff}\n"
                else:
                    # self._logger.info('linear')
                    if len(comp_data['Data']['damping_coeff']) != 1:
                        self._logger.warning(
                            f"Data for Connector elasticity for Material {material}, "
                            f"has multiple damping values, "
                            f"tempereture dependent values are not processed"
                        )
                    s1 = comps_linear_mapping[comp_data['Parameters']['COMPONENT']]
                    s2 = comp_data['Data']['damping_coeff'][0]
                    damping_data += f"TBDATA, {s1}, {s2}\n"
        return damping_data

    def _precess_ref_length(self, property_dict):
        ref_length = [''] * 6
        property_dict = property_dict[0]
        comp1_str = "Length1"
        comp2_str = "Length2"
        comp3_str = "Length3"
        comp4_str = "Angle1"
        comp5_str = "Angle2"
        comp6_str = "Angle3"
        data = []
        if 'Data' in property_dict and property_dict['Data'] is not None:
            data = property_dict['Data']
        # self._logger.info("property_dict")
        # self._logger.info(property_dict)
        # self._logger.info(data)
        if comp1_str in data:
            ref_length[0] = data[comp1_str]
        if comp2_str in data:
            ref_length[1] = data[comp2_str]
        if comp3_str in data:
            ref_length[2] = data[comp3_str]
        if comp4_str in data:
            ref_length[3] = data[comp4_str]
        if comp5_str in data:
            ref_length[4] = data[comp5_str]
        if comp6_str in data:
            ref_length[5] = data[comp6_str]
        return ref_length


class _BoundaryProcessor:
    __slots__ = (
        '_simulation_data',
        '_boundaries_data',
        '_step_start_time',
        '_step_end_time',
        '_ddele_added',
        '_ampl_commands',
        '_model',
        '_logger',
    )

    def __init__(
        self, model: prime.Model, data, step_start_time=0.0, step_end_time=1.0, sim_data=None
    ):
        self._simulation_data = sim_data
        self._boundaries_data = data
        self._step_start_time = step_start_time
        self._step_end_time = step_end_time
        self._ddele_added = False
        self._ampl_commands = ""
        self._model = model
        self._logger = model.python_logger

    def get_ampl_commands(self):
        return self._ampl_commands

    def get_all_boundary_commands(self):
        boundaries_data = self._boundaries_data
        boundary_commands = ''
        for boundary_data in boundaries_data:
            # self._logger.info(boundary_data)
            boundary_commands += self._get_commands(boundary_data)
            # self._logger.info(boundary_commands)
        return boundary_commands

    def get_boundary_commands_by_id(self, boundary_id):
        pass

    def get_boundary_comp_name_with_base_motion(self, base_motion_name):
        boundaries_data = self._boundaries_data
        comp_names = []
        for boundary_data in boundaries_data:
            if 'Parameters' in boundary_data:
                params = boundary_data['Parameters']
                if params is not None and 'BASE NAME' in params:
                    if params['BASE NAME'] == base_motion_name:
                        data_lines = boundary_data['Data']
                        if data_lines is not None:
                            for data_line in data_lines:
                                comp_names.append(
                                    get_modified_component_name(
                                        str(data_line['node_set']), 'NSET', self._simulation_data
                                    )
                                )
                else:
                    if base_motion_name == "":
                        data_lines = boundary_data['Data']
                        if data_lines is not None:
                            for data_line in data_lines:
                                comp_names.append(
                                    get_modified_component_name(
                                        str(data_line['node_set']), 'NSET', self._simulation_data
                                    )
                                )

        return comp_names

    def _get_commands(self, boundary_data):
        # self._logger.info("boundary data is ")
        # self._logger.info(boundary_data)
        boundary_commands = ''
        dof_map = {
            1: 'UX',
            2: 'UY',
            3: 'UZ',
            4: 'ROTX',
            5: 'ROTY',
            6: 'ROTZ',
        }
        amplitude = None
        if 'Parameters' in boundary_data and boundary_data['Parameters'] is not None:
            params = boundary_data['Parameters']
            if 'OP' in params and params['OP'] == 'NEW' and self._ddele_added == False:
                self._ddele_added = True
                boundary_commands += "DDELE,ALL,ALL \n"
            if 'AMPLITUDE' in params:
                # self._logger.info("Tabular Boundary condition is not processed.")
                amplitude = params['AMPLITUDE']
        data_lines = boundary_data['Data']
        for data_line in data_lines:
            if len(data_line) == 0:
                continue
            # self._logger.info("\nthe data line is ", data_line)
            additional_bcs = ''
            first = int(data_line['first_degree'])
            mag = 0.0
            if 'magnitude' in data_line:
                mag = data_line['magnitude']
            if 'last_degree' not in data_line:
                last = first + 1
            elif data_line['last_degree'].strip() == '':
                last = first + 1
            else:
                last = int(data_line['last_degree']) + 1
            if amplitude is not None:
                # modified_amplitude_name = f"{amplitude}_{get_modified_component_name(
                # data_line['node_set'])}"
                modified_amplitude_name = "AMPL_BOUNDARY"
                applied_on = get_modified_component_name(
                    str(data_line['node_set']), 'NSET', self._simulation_data
                )
                ampl_processor = _AmplitudeProcessor(
                    self._model, self._simulation_data["Amplitude"]
                )
                ampl_commands = ampl_processor.get_mapdl_commands_for_amplitude(
                    amplitude,
                    modified_amplitude_name,
                    applied_on,
                    step_start_time=self._step_start_time,
                    step_end_time=self._step_end_time,
                    scale_factor=mag,
                )
                self._ampl_commands += ampl_commands
                # ampl_processor.write_amplitude_table_to_file(ampl_commands)
            if last > 7:
                self._logger.warning(
                    f"Warning: only "
                    f"({[i for i in range(first, min(last,7))]}) "
                    f"boundary data dofs from {first} to {last} are processed"
                )
            for i in range(first, min(last, 7)):
                if data_line['node_set'].isnumeric():
                    boundary_commands += f"D, {data_line['node_set']}, {dof_map[i]}, "
                else:
                    cmname = get_modified_component_name(
                        data_line['node_set'], 'NSET', self._simulation_data
                    )
                    boundary_commands += f"D, {cmname}, {dof_map[i]}, "
                if amplitude is not None:
                    ac = _AmplitudeProcessor._amplitude_count
                    boundary_commands += f"%{modified_amplitude_name}_{ac}%"
                else:
                    boundary_commands += f"{mag}"
                boundary_commands += "\n"
                # if i == first:
                #     boundary_commands += (
                # f"D, {get_modified_component_name(data_line['node_set'])}, {dof_map[i]}, {mag}")
                # else:
                #     additional_bcs += f', {dof_map[i]}'
            # boundary_commands += ', , , ' + additional_bcs + '\n'
        # self._logger.info(boundary_commands)
        return boundary_commands


class _DloadProcessor:
    __slots__ = (
        '_simulation_data',
        '_dloads_data',
        '_step_start_time',
        '_step_end_time',
        '_model',
        '_logger',
    )

    def __init__(
        self, model: prime.Model, data, step_start_time=0.0, step_end_time=1.0, sim_data=None
    ):
        self._simulation_data = sim_data
        self._dloads_data = data
        self._step_start_time = step_start_time
        self._step_end_time = step_end_time
        self._model = model
        self._logger = model.python_logger

    def get_all_dload_commands(self):
        dloads_data = self._dloads_data
        dload_commands = ''
        for dload_data in dloads_data:
            dload_commands += self._get_commands(dload_data)
        return dload_commands

    def get_dload_commands_by_id(self, dload_id):
        pass

    def _get_commands(self, dload_data):
        dload_commands = ''
        op = None
        if 'Parameters' in dload_data and dload_data['Parameters'] is not None:
            params = dload_data['Parameters']
            if 'OP' in params:
                if params['OP'] == 'NEW':
                    op = 'NEW'
                if len(params) > 1:
                    self._logger.warning(f"Warning: parameter on DLOAD keyword are not processed")
            else:
                self._logger.warning(f"Warning: parameter on DLOAD keyword are not processed")
        data_lines = dload_data['Data']
        for data_line in data_lines:
            if len(data_line) == 0:
                continue
            mag = 0
            load_type = None
            elset = None
            if 'element_number_or_set' in data_line:
                elset = get_modified_component_name(
                    data_line['element_number_or_set'], 'ELSET', self._simulation_data
                )
            if 'magnitude' in data_line:
                mag = float(data_line['magnitude'])
            if 'type' in data_line:
                load_type = data_line['type']
            if load_type == "GRAV":
                x = 0.0
                y = 0.0
                z = 0.0
                if 'x' in data_line:
                    x = float(data_line['x'])
                if 'y' in data_line:
                    y = float(data_line['y'])
                if 'z' in data_line:
                    z = float(data_line['z'])
                if elset:
                    if op == 'NEW':
                        dload_commands += f"CMACEL, {elset}, 0.0, 0.0, 0.0 \n"
                    dload_commands += f"CMACEL, {elset}, {-x*mag}, {-y*mag}, {-z*mag}\n"
                else:
                    if op == 'NEW':
                        dload_commands += "ACEL, 0.0, 0.0, 0.0 \n"
                    dload_commands += f"ACEL, {-x*mag}, {-y*mag}, {-z*mag}\n"
        dload_commands += "\n"
        return dload_commands


class _CloadProcessor:
    __slots__ = (
        '_simulation_data',
        '_modal_load_vectors',
        '_step_MSUP',
        '_cloads_data',
        '_step_start_time',
        '_step_end_time',
        '_fedele_added',
        '_load_vestors_in_current_step',
        '_ampl_commands',
        '_model',
        '_logger',
    )

    def __init__(
        self,
        model: prime.Model,
        data,
        step_start_time=0.0,
        step_end_time=1.0,
        step_MSUP=False,
        modal_load_vectors={},
        sim_data=None,
    ):
        self._simulation_data = sim_data
        self._modal_load_vectors = modal_load_vectors
        self._step_MSUP = step_MSUP
        self._cloads_data = data
        self._step_start_time = step_start_time
        self._step_end_time = step_end_time
        self._fedele_added = False
        self._load_vestors_in_current_step = []
        self._ampl_commands = ''
        self._model = model
        self._logger = model.python_logger

    def get_ampl_commands(self):
        return self._ampl_commands

    def get_all_cload_commands(self):
        cloads_data = self._cloads_data
        cload_commands = ''
        if self._step_MSUP:
            cload_commands += f'FDELE, ALL, ALL \n'
            cload_commands += f'SFDELE, ALL, ALL \n'
            cload_commands += f'SFEDELE, ALL, ALL, ALL \n'
            cload_commands += f'ACEL, 0, 0, 0 \n'
            cload_commands += f'\n'
        for cload_data in cloads_data:
            cload_commands += self._get_commands(cload_data)
        if self._step_MSUP:
            for i in list(
                set(self._modal_load_vectors.keys()).difference(
                    set(self._load_vestors_in_current_step)
                )
            ):
                cload_commands += f"LVSCALE, 0, {i}\n"
        return cload_commands

    def get_cload_commands_by_id(self, cload_id):
        pass

    def _get_commands(self, cload_data):
        cload_commands = ''
        cload_lv_scale_commands = ""
        dof_map = {
            1: 'FX',
            2: 'FY',
            3: 'FZ',
            4: 'MX',
            5: 'MY',
            6: 'MZ',
        }
        # self._logger.info(cload_data)
        amplitude = None
        if 'Parameters' in cload_data and cload_data['Parameters'] is not None:
            params = cload_data['Parameters']
            if 'OP' in params and params['OP'] == 'NEW' and self._fedele_added == False:
                self._fedele_added = True
                cload_commands += "FDELE,ALL,ALL \n"
            if 'AMPLITUDE' in params:
                # self._logger.info("Tabular Load condition is not processed.")
                amplitude = params['AMPLITUDE']
        data_lines = cload_data['Data']
        for data_line in data_lines:
            if len(data_line) == 0:
                continue
            dof = int(data_line['degree_of_freedom'])
            mag = 0
            if 'magnitude' in data_line:
                mag = float(data_line['magnitude'])
            if amplitude is not None:
                # modified_amplitude_name = (
                # f"{amplitude}_{get_modified_component_name(data_line['node_set'])}")
                modified_amplitude_name = "AMPL_CLOAD"
                applied_on = get_modified_component_name(
                    str(data_line['node_set']), 'NSET', self._simulation_data
                )
                ampl_processor = _AmplitudeProcessor(
                    self._model, self._simulation_data["Amplitude"]
                )
                ampl_commands = ampl_processor.get_mapdl_commands_for_amplitude(
                    amplitude,
                    modified_amplitude_name,
                    applied_on,
                    step_start_time=self._step_start_time,
                    step_end_time=self._step_end_time,
                    scale_factor=mag,
                )
                self._ampl_commands += ampl_commands
                # ampl_processor.write_amplitude_table_to_file(ampl_commands)
            if data_line['node_set'].isnumeric():
                cload_commands += f"F, {data_line['node_set']}, {dof_map[dof]}, "
            else:
                cmname = get_modified_component_name(
                    data_line['node_set'], 'NSET', self._simulation_data
                )
                cload_commands += f"F, {cmname}, {dof_map[dof]}, "
            if amplitude is not None:
                ac = _AmplitudeProcessor._amplitude_count
                cload_commands += f"%{modified_amplitude_name}_{ac}%"
            else:
                cload_commands += f"{mag}"
            cload_commands += "\n"
            for dict_key, val in self._modal_load_vectors.items():
                if (
                    get_modified_component_name(val["SET"], 'NSET', self._simulation_data)
                    == get_modified_component_name(
                        data_line['node_set'], 'NSET', self._simulation_data
                    )
                    and val["COMP"] == dof_map[dof]
                ):
                    cload_lv_scale_commands += f"LVSCALE, 0, {dict_key}\n"
                    self._load_vestors_in_current_step.append(dict_key)
                    if amplitude:
                        man = modified_amplitude_name
                        ac = _AmplitudeProcessor._amplitude_count
                        cload_lv_scale_commands += f"LVSCALE, %{man}_{ac}%, {dict_key}\n"
                    else:
                        cload_lv_scale_commands += f"LVSCALE, {mag}, {dict_key}\n"
        if self._step_MSUP:
            return cload_lv_scale_commands
        return cload_commands


class _ConnectorMotionProcessor:
    __slots__ = (
        '_simulation_data',
        '_connector_motions_data',
        '_step_start_time',
        '_step_end_time',
        '_fedele_added',
        '_ampl_commands',
        '_model',
        '_logger',
    )

    def __init__(
        self, model: prime.Model, data, step_start_time=0.0, step_end_time=1.0, sim_data=None
    ):
        self._simulation_data = sim_data
        self._connector_motions_data = data
        self._step_start_time = step_start_time
        self._step_end_time = step_end_time
        self._fedele_added = False
        self._ampl_commands = ''
        self._model = model
        self._logger = model.python_logger

    def get_ampl_commands(self):
        return self._ampl_commands

    def get_all_connector_motion_commands(self):
        connector_motions_data = self._connector_motions_data
        connector_motion_commands = ''
        for connector_motion_data in connector_motions_data:
            connector_motion_commands += self._get_commands(connector_motion_data)
        return connector_motion_commands

    def get_connector_motion_commands_by_id(self, connector_motion_id):
        pass

    def _get_commands(self, connector_motion_data):
        connector_motion_commands = ''
        dof_map = {
            1: 'UX',
            2: 'UY',
            3: 'UZ',
            4: 'ROTX',
            5: 'ROTY',
            6: 'ROTZ',
        }
        vel_map = {
            1: 'VELX',
            2: 'VELY',
            3: 'VELZ',
            4: 'OMGX',
            5: 'OMGY',
            6: 'OMGZ',
        }
        acc_map = {
            1: 'ACCX',
            2: 'ACCY',
            3: 'ACCZ',
            4: 'DMGX',
            5: 'DMGY',
            6: 'DMGZ',
        }
        # self._logger.info(connector_motion_data)
        amplitude = None
        fixed = False
        connnector_motion_type = 'DISPLACEMENT'
        if (
            'Parameters' in connector_motion_data
            and connector_motion_data['Parameters'] is not None
        ):
            params = connector_motion_data['Parameters']
            if 'OP' in params and params['OP'] == 'NEW' and self._fedele_added == False:
                self._fedele_added = True
                connector_motion_commands += "DJDELE,ALL,ALL \n"
            if 'AMPLITUDE' in params:
                # self._logger.info("Tabular Load condition is not processed.")
                amplitude = params['AMPLITUDE']
            if 'LOAD CASE' in params:
                self._logger.warning("Load Case in Connector Motion is not processed.")
            if 'TYPE' in params:
                connnector_motion_type = params['TYPE']
            if 'FIXED' in params:
                fixed = True
        data_lines = connector_motion_data['Data']
        for data_line in data_lines:
            if len(data_line) == 0:
                continue
            dof = int(data_line['component_of_motion'])
            mag = 0
            if 'magnitude' in data_line:
                mag = float(data_line['magnitude'])
            if amplitude is not None:
                # modified_amplitude_name = (
                # f"{amplitude}_{get_modified_component_name(data_line['node_set'])}")
                modified_amplitude_name = "AMPL_CONNECTOR_MOTION"
                applied_on = get_modified_component_name(
                    str(data_line['element_number_or_set']), 'ELSET', self._simulation_data
                )
                ampl_processor = _AmplitudeProcessor(
                    self._model, self._simulation_data["Amplitude"]
                )
                ampl_commands = ampl_processor.get_mapdl_commands_for_amplitude(
                    amplitude,
                    modified_amplitude_name,
                    applied_on,
                    step_start_time=self._step_start_time,
                    step_end_time=self._step_end_time,
                    scale_factor=mag,
                )
                # ampl_processor.write_amplitude_table_to_file(ampl_commands)
            if data_line['element_number_or_set'].isnumeric() == False:
                dls = get_modified_component_name(
                    data_line['element_number_or_set'], 'ELSET', self._simulation_data
                )
                connector_motion_commands += f"CMSEL, S, {dls}, ELEM\n"
                connector_motion_commands += f"ELEM_NUM = ELNEXT(0)\n"
                connector_motion_commands += f"DJ, ELEM_NUM, "
            else:
                cmname = get_modified_component_name(
                    str(data_line['element_number_or_set']), 'ELSET', self._simulation_data
                )
                connector_motion_commands += f"DJ, {cmname}, "
            if connnector_motion_type == 'DISPLACEMENT':
                connector_motion_commands += f"{dof_map[dof]}, "
            elif connnector_motion_type == 'VELOCITY':
                connector_motion_commands += f"{vel_map[dof]}, "
            elif connnector_motion_type == 'ACCELERATION':
                connector_motion_commands += f"{acc_map[dof]}, "
            if fixed:
                connector_motion_commands += f"%_FIX%"
            else:
                if amplitude is not None:
                    man = modified_amplitude_name
                    ac = _AmplitudeProcessor._amplitude_count
                    connector_motion_commands += f"%{man}_{ac}%"
                else:
                    connector_motion_commands += f"{mag}"
            connector_motion_commands += "\n"
        return connector_motion_commands


class _BaseMotionProcessor:
    __slots__ = (
        '_simulation_data',
        '_modal_load_vectors',
        '_step_MSUP',
        '_base_motions_data',
        '_step_start_time',
        '_step_end_time',
        '_fedele_added',
        '_load_vestors_in_current_step',
        '_ampl_commands',
        '_model',
        '_logger',
    )

    def __init__(
        self,
        model: prime.Model,
        data,
        step_start_time=0.0,
        step_end_time=1.0,
        step_MSUP=False,
        modal_load_vectors={},
        sim_data=None,
    ):
        self._simulation_data = sim_data
        self._modal_load_vectors = modal_load_vectors
        self._step_MSUP = step_MSUP
        self._base_motions_data = data
        self._step_start_time = step_start_time
        self._step_end_time = step_end_time
        self._fedele_added = False
        self._load_vestors_in_current_step = []
        self._ampl_commands = ''
        self._model = model
        self._logger = model.python_logger

    def get_ampl_commands(self):
        return self._ampl_commands

    def get_all_base_motion_commands(self):
        base_motions_data = self._base_motions_data
        base_motion_commands = ''
        if self._step_MSUP:
            base_motion_commands += f'FDELE, ALL, ALL \n'
            base_motion_commands += f'SFDELE, ALL, ALL \n'
            base_motion_commands += f'SFEDELE, ALL, ALL, ALL \n'
            base_motion_commands += f'ACEL, 0, 0, 0 \n'
            base_motion_commands += f'\n'
        for base_motion_data in base_motions_data:
            base_motion_commands += self._get_commands(base_motion_data)
        if self._step_MSUP:
            for i in list(
                set(self._modal_load_vectors.keys()).difference(
                    set(self._load_vestors_in_current_step)
                )
            ):
                base_motion_commands += f"LVSCALE, 0, {i}\n"
        return base_motion_commands

    def get_base_motion_commands_by_id(self, base_motion_id):
        pass

    def _get_commands(self, base_motion_data):
        base_motion_commands = ''
        base_motion_lv_scale_commands = ''
        dof_map = {
            1: 'UX',
            2: 'UY',
            3: 'UZ',
            4: 'ROTX',
            5: 'ROTY',
            6: 'ROTZ',
        }
        # self._logger.info(base_motion_data)
        amplitude = None
        dof = 0
        scale = 1.0
        base_name = None
        connnector_motion_type = 'DISPLACEMENT'
        if 'Parameters' in base_motion_data and base_motion_data['Parameters'] is not None:
            params = base_motion_data['Parameters']
            if 'AMPLITUDE' in params:
                # self._logger.warning("Tabular Load condition is not processed.")
                amplitude = params['AMPLITUDE']
            else:
                self._logger.warning(
                    f"Warning: Base Motion is not processed for current analysis type."
                )
                return base_motion_commands
            if 'LOAD CASE' in params:
                self._logger.warning("Load Case in base Motion is not processed.")
            if 'TYPE' in params:
                connnector_motion_type = params['TYPE']
            if 'DOF' in params:
                dof = int(params['DOF'])
            if 'SCALE' in params:
                scale = float(params['SCALE'])
            if 'BASE NAME' in params:
                base_name = params['BASE NAME']
        # Processing the Base Motion
        if amplitude is not None:
            # modified_amplitude_name = (
            # f"{amplitude}_{get_modified_component_name(data_line['node_set'])}")
            modified_amplitude_name = "AMPL_BASE_MOTION_" + connnector_motion_type
            applied_on = base_name
            ampl_processor = _AmplitudeProcessor(self._model, self._simulation_data["Amplitude"])
            ampl_commands = ampl_processor.get_mapdl_commands_for_amplitude(
                amplitude,
                modified_amplitude_name,
                applied_on,
                step_start_time=self._step_start_time,
                step_end_time=self._step_end_time,
                scale_factor=scale,
            )
            self._ampl_commands += ampl_commands
            # ampl_processor.write_amplitude_table_to_file(ampl_commands)
        if connnector_motion_type == 'DISPLACEMENT':
            pass
        elif connnector_motion_type == 'VELOCITY':
            pass
        elif connnector_motion_type == 'ACCELERATION':
            pass
        # TODO Define appropriate conversion of applied base motion to the Force
        # TODO LMM (Large Mass Method) to be implemented
        for dict_key, val in self._modal_load_vectors.items():
            # TODO below line compared 'COMP' FZ to dof_map UZ, Take care of this while correction
            if val["SET"] == base_name and val["COMP"] == dof_map[dof]:
                base_motion_lv_scale_commands += f"LVSCALE, 0, {dict_key}\n"
                self._load_vestors_in_current_step.append(dict_key)
                man = modified_amplitude_name
                ac = _AmplitudeProcessor._amplitude_count
                base_motion_lv_scale_commands += f"LVSCALE, %{man}_{ac}%, {dict_key}\n"
        if self._step_MSUP:
            return base_motion_lv_scale_commands
        return base_motion_commands


class _GeneralContactProcessing:
    __slots__ = ('_general_contact_data', '_surface_interaction_data', '_model', '_logger')

    def __init__(self, model: prime.Model, cont_data, surf_interaction_data):
        self._general_contact_data = cont_data
        self._surface_interaction_data = surf_interaction_data
        self._model = model
        self._logger = model.python_logger

    def get_all_general_contact_commands(self):
        gen_c_commands = "! --------------------- General Contact Commands ------------! \n"
        if type(self._general_contact_data) == dict:
            self._logger.info(self._general_contact_data)
            self._logger.info("dict")
            gen_c_commands += self._get_gen_c_commands(self._general_contact_data)
        if type(self._general_contact_data) == list:
            for item in self._general_contact_data:
                self._logger.info(item)
                self._logger.info("list")
                gen_c_commands += self._get_gen_c_commands(item)
        return gen_c_commands

    def _get_gen_c_commands(self, data):
        mapdl_commands = ""
        mapdl_commands += "*GET,REALMAX,ELEM,,RELM\n"
        mapdl_commands += "REALMAX = REALMAX+1\n"
        mapdl_commands += "R,REALMAX\n"
        mapdl_commands += "\n"
        mapdl_commands += "*GET,MATMAX,ELEM,,MATM\n"
        mapdl_commands += "MATMAX = MATMAX+1\n"
        mapdl_commands += "MP,MU,MATMAX,"
        if "Parameters" in data and data["Parameters"] is not None:
            self._logger.warning(
                f"Argument on *CONTACT is not processed, please check the definitions"
            )
        if "ContactPropertyAssignment" in data and data["ContactPropertyAssignment"] is not None:
            prop_assign = data["ContactPropertyAssignment"]
            if 'Data' in prop_assign and prop_assign['Data']:
                prop_data = prop_assign['Data'][0]
                if 'surface1' in prop_data or 'surface2' in prop_data:
                    self._logger.warning(
                        "the surfaces on CONTACT PROPERTY ASSIGNMENT are not processed"
                    )
                if 'surface_interaction' in prop_data:
                    surf_interaction_processor = _SurfaceInteractionProcessing(
                        self._model, self._surface_interaction_data
                    )
                    fric = surf_interaction_processor._get_friction_value_for_interaction(
                        prop_data['surface_interaction']
                    )
                    mapdl_commands += f"{fric}\n"
        mapdl_commands += "\n"
        mapdl_commands += "! NUMCMP,ELEM\n"
        mapdl_commands += "! NUMCMP,NODE\n"
        mapdl_commands_exclude = ''
        if "ContactExclusions" in data and data["ContactExclusions"] is not None:
            exclude = data["ContactExclusions"]
            if 'Data' in exclude and exclude['Data']:
                mapdl_commands_exclude += "ESEL, NONE\n"
                ex_data = exclude['Data']
                for d in ex_data:
                    if 'surface1' in d:
                        mapdl_commands_exclude += f"ESEL, A, {d['surface1']}\n"
                    if 'surface2' in d:
                        mapdl_commands_exclude += f"ESEL, A, {d['surface2']}\n"
                mapdl_commands_exclude += "CM, GEN_C_EXCLUDE, ELEM\n"
                mapdl_commands_exclude += "\n"
        mapdl_commands += mapdl_commands_exclude
        mapdl_commands_include = ""
        if "ContactInclusions" in data and data["ContactInclusions"] is not None:
            include = data["ContactInclusions"]
            if "Parameters" in include and include["Parameters"] is not None:
                mapdl_commands_include += "ESEL, NONE\n"
                mapdl_commands_include += f"ESEL, A, ENAME, ,181\n"
                mapdl_commands_include += f"ESEL, A, ENAME, ,185\n"
            else:
                if 'Data' in include and include['Data']:
                    mapdl_commands_include += "ESEL, NONE\n"
                    in_data = include['Data']
                    for d in in_data:
                        if 'surface1' in d:
                            mapdl_commands_include += f"ESEL, A, {d['surface1']}\n"
                        else:
                            mapdl_commands_include += f"ESEL, A, ENAME, ,181\n"
                            mapdl_commands_include += f"ESEL, A, ENAME, ,185\n"
                        if 'surface2' in d:
                            mapdl_commands_include += f"ESEL, A, {d['surface2']}\n"
        mapdl_commands += mapdl_commands_include
        if mapdl_commands_exclude:
            mapdl_commands += "CMSEL, U, GEN_C_EXCLUDE, ELEM\n"
        mapdl_commands += "NSLE\n"
        mapdl_commands += "\n"
        mapdl_commands += "GCGEN,,30,0\n"
        mapdl_commands += "GCDEF,,ALL,ALL,MATMAX,REALMAX\n"
        mapdl_commands += "!GCDEF,EXCL,EXCL_1,ALL\n"
        mapdl_commands += "KEYO,GCN,11,1\n"
        mapdl_commands += "ALLSEL, ALL, ALL\n"
        mapdl_commands += "\n"
        mapdl_commands += "ESEL,S,ENAME,,177\n"
        mapdl_commands += "EDELE, ALL, ALL\n"
        mapdl_commands += "ALLSEL, ALL, ALL\n"
        return mapdl_commands


class _SurfaceInteractionProcessing:
    __slots__ = ('_surface_interaction', '_model', '_logger')

    def __init__(self, model: prime.Model, data):
        self._surface_interaction = data
        self._model = model
        self._logger = model.python_logger

    def _get_friction_value_for_interaction(self, interaction_name):
        fric = 0.0
        if self._surface_interaction is not None:
            if interaction_name in self._surface_interaction:
                interaction = self._surface_interaction[interaction_name]
                if "Friction" in interaction:
                    try:
                        fric = interaction["Friction"]["Data"]["coefficient"]
                    except:
                        fric = 0.0
        return fric


class _MonitorProcessor:
    __slots__ = ('_simulation_data', '_monitor_data', '_model', '_logger')

    def __init__(self, model: prime.Model, data, sim_data=None):
        self._monitor_data = data
        self._model = model
        self._logger = model.python_logger
        self._simulation_data = sim_data

    def get_monitor_commands(self):
        monitor_commands = ""
        dof_map = {
            1: 'UX',
            2: 'UY',
            3: 'UZ',
            4: 'ROTX',
            5: 'ROTY',
            6: 'ROTZ',
        }
        counter = 0
        for monitor_data in self._monitor_data:
            params = monitor_data['Parameters']
            if params is not None:
                dof = None
                node = None
                if 'FREQUENCY' in params:
                    self._logger.warning('FREQUENCY on *MONITOR is not processed.')
                if 'DOF' in params:
                    dof = int(params['DOF'])
                if 'NODE' in params:
                    node = params['NODE']
                if dof is None or node is None:
                    self._logger.warning(
                        f"NODE/DOF is not provided on *MONITOR. "
                        f"translation of *MONITOR is ignored."
                    )
                else:
                    str_dof = ""
                    str_node = ""
                    if dof in dof_map:
                        str_dof = dof_map[dof]
                    else:
                        self._logger.warning(
                            f"Invalid DOF (not from this 1-6 == UX,UY,UZ,ROTX,ROTY,ROTZ) "
                            f"is provided on *MONITOR. translation of *MONITOR is ignored."
                        )
                        continue
                    if node.isnumeric():
                        str_node = node
                    else:
                        cmname = get_modified_component_name(node, 'NSET', self._simulation_data)
                        monitor_commands += f"CMSEL,S,{cmname},NODE\n"
                        monitor_commands += f"node_id = NDNEXT(0)\n"
                        monitor_commands += f"ALLSEL\n"
                        str_node = 'node_id'
                    counter += 1
                    monitor_commands += f"MONITOR,{counter},{str_node},{str_dof}\n"
        return monitor_commands


class _GlobalDampingProcessing:
    __slots__ = ('_global_damping_data', '_model', '_logger')

    def __init__(self, model: prime.Model, data):
        self._global_damping_data = data
        self._model = model
        self._logger = model.python_logger

    def get_global_damping_commands(self, analysis, msup=False):
        # self._logger.info(analysis)
        # self._logger.info(self._global_damping_data)
        damping_commands = ""
        params = self._global_damping_data[0]['Parameters']
        filed = 'ALL'
        alpha = 0.0
        beta = 0.0
        structural = 0.0
        if 'FIELD' in params:
            field = params['FIELD']
        if 'ALPHA' in params:
            alpha = float(params['ALPHA'])
        if 'BETA' in params:
            beta = float(params['BETA'])
        if 'STRUCTURAL' in params:
            structural = float(params['STRUCTURAL'])
        if filed == 'ACOUSTIC':
            self._logger.warning('Global damping under STEP is not processed.')
            return damping_commands

        if alpha != 0.0:
            damping_commands += f"ALPHAD, {alpha}\n"
        if beta != 0.0:
            damping_commands += f"BETAD, {beta}\n"
        if structural != 0.0:
            if analysis == "MODAL DYNAMIC":
                damping_commands += f"DMPRAT, {structural/2}\n"
            elif analysis == "STEADY STATE DYNAMICS":
                damping_commands += f"DMPSTR, {structural}\n"
            elif analysis == "FREQUENCY":
                damping_commands += f"DMPSTR, {structural}\n"
            else:
                self._logger.warning(
                    'Global damping under STEP is not processed. Please check the results'
                )
        return damping_commands, structural


class _StepProcessor:
    __slots__ = (
        '_simulation_data',
        '_steps_data',
        '_curr_step',
        '_analysis_sequence',
        '_assign_analysis',
        '_time',
        '_step_counter',
        '_ninterval_counter',
        '_previous_analysis',
        '_step_start_time',
        '_step_end_time',
        '_previous_modal_resvec',
        '_step_MSUP',
        '_nrm_key',
        '_modal_load_vectors',
        '_ninterval_mapdl_commands',
        '_cload_ampl_commands',
        '_base_motion_ampl_commands',
        '_boundary_ampl_commands',
        '_connector_motion_ampl_commands',
        '_model',
        '_logger',
        '_model_application',
        '_transient_output_controls',
        '_global_structural_damping_value',
    )

    def __init__(self, model: prime.Model, data, sim_data, model_application):
        self._simulation_data = sim_data
        self._steps_data = data
        self._curr_step = None
        self._analysis_sequence = []
        self._assign_analysis = []
        self._time = 0.0
        self._step_counter = 0
        self._ninterval_counter = 0
        self._previous_analysis = None
        self._step_start_time = None
        self._step_end_time = None
        self._previous_modal_resvec = None
        self._step_MSUP = False
        self._nrm_key = None
        self._modal_load_vectors = {}
        self._ninterval_mapdl_commands = ''
        self._cload_ampl_commands = ''
        self._base_motion_ampl_commands = ''
        self._boundary_ampl_commands = ''
        self._connector_motion_ampl_commands = ''
        self._model = model
        self._logger = model.python_logger
        self._model_application = model_application
        self._transient_output_controls = ""
        self._global_structural_damping_value = 0.0

    def get_cload_ampl_commands(self):
        return self._cload_ampl_commands

    def get_base_motion_ampl_commands(self):
        return self._base_motion_ampl_commands

    def get_boundary_ampl_commands(self):
        return self._boundary_ampl_commands

    def get_connector_motion_ampl_commands(self):
        return self._connector_motion_ampl_commands

    def get_analysis_sequence(self):
        steps = self._steps_data
        analysis_type = None
        self._analysis_sequence.append(None)
        for step in steps:
            # self._logger.info(step)
            if "Static" in step:
                analysis_type = 'STATIC'
            elif "ModalDynamic" in step:
                analysis_type = 'MODAL DYNAMIC'
            elif "Dynamic" in step:
                analysis_type = 'DYNAMIC'
            elif "Frequency" in step:
                analysis_type = 'FREQUENCY'
            elif "SteadyStateDynamics" in step:
                analysis_type = 'STEADY STATE DYNAMICS'
            else:
                self._logger.warning("Warning: analysis type not recognized")
            self._analysis_sequence.append(analysis_type)

    def get_static_analysis_data(self, static_data):
        """Get static analysis details."""
        static_analysis_commands = ''
        # self._logger.info(static_data)
        if type(static_data) == list:
            static_data = static_data[0]
        time_increment = 1.0
        time_period = 1.0
        min_time_increment = 1e-05
        max_time_increment = 1.0
        # if 'Data' in static_data and static_data['Data'] == None:
        # time_increment = 1.0
        # self._logger.info("\nstatic data parent is ", static_data)
        if 'Data' in static_data and static_data['Data'] is not None:
            data = static_data['Data']
            # self._logger.info("\nstatic data is ", data)
            if 'time_increment' in data:
                time_increment = float(data['time_increment'])
            if 'time_period' in data:
                time_period = float(data['time_period'])
                min_time_increment = time_period * 1e-05
            if 'min_time_increment' in data:
                min_time_increment = float(data['min_time_increment'])
            if 'max_time_increment' in data:
                max_time_increment = float(data['max_time_increment'])
            else:
                max_time_increment = time_period
        max_output_intervals = self.get_maximum_output_interval()
        if max_output_intervals != 0:
            if time_increment > (time_period / max_output_intervals):
                time_increment = time_period / max_output_intervals
            if max_time_increment > (time_period / max_output_intervals):
                max_time_increment = time_period / max_output_intervals
        time_interval_val = self.get_output_time_interval()
        if time_interval_val != 0.0:
            time_increment = time_interval_val
            # min_time_increment = time_interval_val
            max_time_increment = time_interval_val
            # if time_increment > time_interval_val:
            # time_increment = time_interval_val
            # if min_time_increment > time_interval_val:
            # min_time_increment = time_interval_val
            # if max_time_increment > time_interval_val:
            # max_time_increment = time_interval_val
        if time_increment > max_time_increment:
            time_increment = max_time_increment
        self._step_start_time = self._time
        self._time += time_period
        self._step_end_time = self._time
        static_analysis_commands += (
            f'! ------------------------------- '
            f'STEP: {self._step_counter} -----------------------\n'
        )
        if self._previous_analysis != "STATIC":
            if self._model_application == prime.CdbAnalysisType.OUTERPANELSTIFFNESS:
                use_quasi = os.getenv("APDL_QUASI")
                if use_quasi == "1":
                    static_analysis_commands += 'ANTYPE, TRANSIENT\n'
                    static_analysis_commands += 'TIMINT, ON\n'
                    static_analysis_commands += 'TINTP, QUASI\n'
                    static_analysis_commands += 'NROPT, FULL\n'
                else:
                    static_analysis_commands += 'ANTYPE, STATIC\n'
            else:
                static_analysis_commands += 'ANTYPE, STATIC\n'
        static_analysis_commands += f'TIME,{self._time}\n'
        static_analysis_commands += f'AUTOTS,ON\n'
        static_analysis_commands += (
            f'DELTIM, {time_increment}, {min_time_increment}, {max_time_increment}, , FORCE\n'
        )
        static_analysis_commands += '\n'
        self._previous_analysis = "STATIC"
        return static_analysis_commands

    def get_modal_dynamic_analysis_data(self, dynamic_data):
        """Get modal dynamic analysis details."""
        dynamic_analysis_commands = ''
        self._step_MSUP = True
        if type(dynamic_data) == list:
            dynamic_data = dynamic_data[0]
        time_increment = 1.0
        time_period = 1.0
        min_time_increment = 1e-05
        max_time_increment = 1.0
        res_modes = None
        if self._previous_modal_resvec:
            res_modes = 'ON'
        transient_integration_param = ''
        if 'Data' in dynamic_data and dynamic_data['Data'] is not None:
            data = dynamic_data['Data']
            if 'time_increment' in data:
                time_increment = float(data['time_increment'])
                min_time_increment = float(data['time_increment'])
                max_time_increment = float(data['time_increment'])
            if 'time_period' in data:
                time_period = float(data['time_period'])
        # max_output_intervals = self.get_maximum_output_interval()
        # if max_output_intervals != 0:
        # if time_increment > (time_period/max_output_intervals):
        # time_increment = (time_period/max_output_intervals)
        # if max_time_increment > (time_period/max_output_intervals):
        # max_time_increment = (time_period/max_output_intervals)
        # time_interval_val = self.get_output_time_interval()
        # if time_interval_val != 0:
        # time_increment = time_interval_val
        # min_time_increment = time_interval_val
        # max_time_increment = time_interval_val
        # # if time_increment > time_interval_val:
        # # time_increment = time_interval_val
        # # if min_time_increment > time_interval_val:
        # # min_time_increment = time_interval_val
        # # if max_time_increment > time_interval_val:
        # # max_time_increment = time_interval_val
        if time_increment > max_time_increment:
            time_increment = max_time_increment
        if 'Parameters' in dynamic_data:
            data = dynamic_data['Parameters']
            if data:
                if 'APPLICATION' in data:
                    if data['APPLICATION'] == 'QUASI-STATIC':
                        transient_integration_param = 'QUASI'
        self._step_start_time = self._time
        self._time += time_period
        self._step_end_time = self._time
        dynamic_analysis_commands += (
            f'! ---------------------------- STEP: {self._step_counter} -----------------------\n'
        )
        if self._previous_analysis == "STATIC":
            dynamic_analysis_commands += 'TINTP, 0.41421,,,,,,-1\n'
            dynamic_analysis_commands += '\n'
            dynamic_analysis_commands += 'SOLO,STOT,FORCE,HHT\n'
            dynamic_analysis_commands += '\n'
            dynamic_analysis_commands += 'IC,ALL,VELX,0,,,,LSIC\n'
            dynamic_analysis_commands += 'IC,ALL,VELY,0,,,,LSIC\n'
            dynamic_analysis_commands += 'IC,ALL,VELZ,0,,,,LSIC\n'
            dynamic_analysis_commands += 'IC,ALL,OMGX,0,,,,LSIC\n'
            dynamic_analysis_commands += 'IC,ALL,OMGY,0,,,,LSIC\n'
            dynamic_analysis_commands += 'IC,ALL,OMGZ,0,,,,LSIC\n'
            dynamic_analysis_commands += 'IC,ALL,ACCX,0,,,,LSIC\n'
            dynamic_analysis_commands += 'IC,ALL,ACCY,0,,,,LSIC\n'
            dynamic_analysis_commands += 'IC,ALL,ACCZ,0,,,,LSIC\n'
            dynamic_analysis_commands += 'IC,ALL,DMGX,0,,,,LSIC\n'
            dynamic_analysis_commands += 'IC,ALL,DMGY,0,,,,LSIC\n'
            dynamic_analysis_commands += 'IC,ALL,DMGZ,0,,,,LSIC\n'
            dynamic_analysis_commands += '\n'
            dynamic_analysis_commands += 'NROPT,FULL\n'
            dynamic_analysis_commands += '\n'
        if self._previous_analysis == "FREQUENCY":
            dynamic_analysis_commands += f'FINISH\n'
            dynamic_analysis_commands += f'\n'
            dynamic_analysis_commands += (
                f'/ASSIGN, rst, step_{self._step_counter}_transient_analysis, rst\n'
            )
            self._assign_analysis.append(f'step_{self._step_counter}_transient_analysis')
            dynamic_analysis_commands += f'/SOLU\n'
        if self._previous_analysis != "MODAL DYNAMIC":
            dynamic_analysis_commands += f'ANTYPE, TRANSIENT\n'
            dynamic_analysis_commands += f'TRNOPT, '
            if "FREQUENCY" in self._analysis_sequence[: self._step_counter]:
                dynamic_analysis_commands += f'MSUP'
                self._step_MSUP = True
                has_modal_output, has_velocities = self.check_modal_output()
                if has_modal_output:
                    dynamic_analysis_commands += f' , , , , YES'
                if has_velocities:
                    dynamic_analysis_commands += f' , , YES'
            else:
                dynamic_analysis_commands += f'FULL'
            dynamic_analysis_commands += f'\n'
        if transient_integration_param:
            dynamic_analysis_commands += f'TINTP, {transient_integration_param}\n'
        dynamic_analysis_commands += f'TIME, {self._time}\n'
        dynamic_analysis_commands += (
            f'DELTIM, {time_increment}, {min_time_increment}, {max_time_increment}\n'
        )
        dynamic_analysis_commands += f'\n'
        if res_modes:
            dynamic_analysis_commands += f'RESVEC, {res_modes}\n'
        dynamic_analysis_commands += f'\n'
        self._previous_analysis = "MODAL DYNAMIC"
        return dynamic_analysis_commands

    def get_dynamic_analysis_data(self, dynamic_data):
        """Get dynamic analysis details."""
        dynamic_analysis_commands = ''
        self._step_MSUP = False
        if type(dynamic_data) == list:
            dynamic_data = dynamic_data[0]
        time_increment = 1.0
        time_period = 1.0
        min_time_increment = 1e-05
        max_time_increment = 1.0
        res_modes = None
        if self._previous_modal_resvec:
            res_modes = 'ON'
        transient_integration_param = ''
        if 'Data' in dynamic_data and dynamic_data['Data'] is not None:
            data = dynamic_data['Data']
            if 'time_increment' in data:
                time_increment = float(data['time_increment'])
            if 'time_period' in data:
                time_period = float(data['time_period'])
                min_time_increment = time_period * 1e-5
            if 'min_time_increment' in data:
                min_time_increment = float(data['min_time_increment'])
            if 'max_time_increment' in data:
                max_time_increment = float(data['max_time_increment'])
            else:
                max_time_increment = time_period
        max_output_intervals = self.get_maximum_output_interval()
        if max_output_intervals != 0:
            if time_increment > (time_period / max_output_intervals):
                time_increment = time_period / max_output_intervals
            if max_time_increment > (time_period / max_output_intervals):
                max_time_increment = time_period / max_output_intervals
            # if time_increment == max_time_increment:
            # min_time_increment = time_increment
        time_interval_val = self.get_output_time_interval()
        if time_interval_val != 0:
            time_increment = time_interval_val
            # min_time_increment = time_interval_val
            max_time_increment = time_interval_val
            # if time_increment > time_interval_val:
            # time_increment = time_interval_val
            # if min_time_increment > time_interval_val:
            # min_time_increment = time_interval_val
            # if max_time_increment > time_interval_val:
            # max_time_increment = time_interval_val
        if time_increment > max_time_increment:
            time_increment = max_time_increment
        if 'Parameters' in dynamic_data:
            data = dynamic_data['Parameters']
            if data:
                if 'APPLICATION' in data:
                    if data['APPLICATION'] == 'QUASI-STATIC':
                        transient_integration_param = 'QUASI'
        self._step_start_time = self._time
        self._time += time_period
        self._step_end_time = self._time
        dynamic_analysis_commands += (
            f'! ------------------------- STEP: {self._step_counter} -----------------------\n'
        )
        if self._previous_analysis == "STATIC":
            dynamic_analysis_commands += 'TINTP, 0.41421,,,,,,-1\n'
            dynamic_analysis_commands += '\n'
            dynamic_analysis_commands += 'SOLO,STOT,FORCE,HHT\n'
            dynamic_analysis_commands += '\n'
            dynamic_analysis_commands += 'IC,ALL,VELX,0,,,,LSIC\n'
            dynamic_analysis_commands += 'IC,ALL,VELY,0,,,,LSIC\n'
            dynamic_analysis_commands += 'IC,ALL,VELZ,0,,,,LSIC\n'
            dynamic_analysis_commands += 'IC,ALL,OMGX,0,,,,LSIC\n'
            dynamic_analysis_commands += 'IC,ALL,OMGY,0,,,,LSIC\n'
            dynamic_analysis_commands += 'IC,ALL,OMGZ,0,,,,LSIC\n'
            dynamic_analysis_commands += 'IC,ALL,ACCX,0,,,,LSIC\n'
            dynamic_analysis_commands += 'IC,ALL,ACCY,0,,,,LSIC\n'
            dynamic_analysis_commands += 'IC,ALL,ACCZ,0,,,,LSIC\n'
            dynamic_analysis_commands += 'IC,ALL,DMGX,0,,,,LSIC\n'
            dynamic_analysis_commands += 'IC,ALL,DMGY,0,,,,LSIC\n'
            dynamic_analysis_commands += 'IC,ALL,DMGZ,0,,,,LSIC\n'
            dynamic_analysis_commands += '\n'
            dynamic_analysis_commands += 'NROPT,FULL\n'
            dynamic_analysis_commands += '\n'
        if self._previous_analysis == "FREQUENCY":
            dynamic_analysis_commands += f'FINISH\n'
            dynamic_analysis_commands += f'\n'
            dynamic_analysis_commands += (
                f'/ASSIGN, rst, step_{self._step_counter}_transient_analysis, rst\n'
            )
            self._assign_analysis.append(f'step_{self._step_counter}_transient_analysis')
            dynamic_analysis_commands += f'/SOLU\n'
        if self._previous_analysis != "DYNAMIC" and self._previous_analysis != "STATIC":
            dynamic_analysis_commands += f'ANTYPE, TRANSIENT\n'
            dynamic_analysis_commands += f'TRNOPT, '
            if "FREQUENCY" in self._analysis_sequence[: self._step_counter]:
                dynamic_analysis_commands += f'MSUP\n'
                self._step_MSUP = True
            else:
                dynamic_analysis_commands += f'FULL\n'
        if transient_integration_param:
            dynamic_analysis_commands += f'TINTP, {transient_integration_param}\n'
        dynamic_analysis_commands += f'TIME, {self._time}\n'
        dynamic_analysis_commands += f'AUTOTS,ON\n'
        dynamic_analysis_commands += (
            f'DELTIM, {time_increment}, {min_time_increment}, {max_time_increment},, FORCE\n'
        )
        dynamic_analysis_commands += f'\n'
        if res_modes:
            dynamic_analysis_commands += f'RESVEC, {res_modes}\n'
        dynamic_analysis_commands += f'\n'
        self._previous_analysis = "DYNAMIC"
        return dynamic_analysis_commands

    def get_frequency_analysis_data(self, frequency_data):
        """Get frequency analysis details."""
        # This is to reset the counter of time when modal analysis is there.
        self._time = 0.0
        frequency_analysis_commands = ''
        if type(frequency_data) == list:
            frequency_data = frequency_data[0]
        steady_state_dynamics_data = self._steps_data
        modopt_method = 'LANB'
        nmodes = 1000
        min_frequency = ''
        max_frequency = ''
        cpxmod = ''
        nrm_key = 'OFF'
        res_modes = None
        data = frequency_data['Data'] if 'Data' in frequency_data else None
        if data is not None and isinstance(data, list):
            first_line = data[0]
        else:
            first_line = data
        if first_line is not None:
            if 'num_eigenvalues' in first_line:
                nmodes = int(first_line['num_eigenvalues'])
            if 'min_frequency' in first_line:
                min_frequency = float(first_line['min_frequency'])
            if 'max_frequency' in first_line:
                max_frequency = float(first_line['max_frequency'])
        if 'Parameters' in frequency_data:
            data = frequency_data['Parameters']
            if data is not None and 'EIGENSOLVER' in data:
                if data['EIGENSOLVER'] == 'SUBSPACE':
                    modopt_method = 'SUBSP'
            # self._logger.info(f"Modal_analysis PArameters: {data}")
            if data is not None and 'NORMALIZATION' in data:
                # self._logger.info(f"Modal_analysis PArameters: {data}")
                # self._logger.info(f"Modal_analysis norm: {data['NORMALIZATION']}")
                if data['NORMALIZATION'] == 'MASS':
                    nrm_key = 'OFF'
                else:
                    nrm_key = 'ON'
            else:
                # self._logger.info(f"Modal_analysis PArameters: {data}")
                # self._logger.info(f"Modal_analysis eigensolver: {data['EIGENSOLVER']}")
                if data is not None and 'EIGENSOLVER' in data and data['EIGENSOLVER'] == 'AMS':
                    nrm_key = 'OFF'
                else:
                    nrm_key = 'ON'
            if data is not None and 'RESIDUAL MODES' in data:
                res_modes = 'ON'
                self._previous_modal_resvec = 'ON'
        if self._simulation_data is not None:
            if "GlobalDamping" in self._curr_step and self._curr_step['GlobalDamping']:
                modopt_method = 'QRDAMP'
            if "ConnectorBehavior" in self._simulation_data:
                all_conn_behavior = self._simulation_data['ConnectorBehavior']
                if all_conn_behavior:
                    for mat in all_conn_behavior:
                        conn_mat = all_conn_behavior[mat]
                        if conn_mat and 'CONNECTOR DAMPING' in conn_mat:
                            for conn_damp in conn_mat['CONNECTOR DAMPING']:
                                if conn_damp and 'Parameters' in conn_damp:
                                    if (
                                        "TYPE" in conn_damp['Parameters']
                                        and conn_damp['Parameters']['TYPE'] == 'VISCOUS'
                                    ):
                                        modopt_method = 'QRDAMP'
                                        break
            if "Materials" in self._simulation_data:
                all_mats = self._simulation_data['Materials']
                if all_mats:
                    for mat in all_mats:
                        _mat = all_mats[mat]
                        if _mat and 'DAMPING' in _mat:
                            if 'Parameters' in _mat['DAMPING']:
                                if "ALPHA" in _mat['DAMPING']['Parameters']:
                                    modopt_method = 'QRDAMP'
                                    break
            if "Mass" in self._simulation_data:
                all_mass = self._simulation_data['Mass']
                if all_mass:
                    for m in all_mass:
                        _m = all_mass[m]
                        if 'Parameters' in _m:
                            if "ALPHA" in _m['Parameters']:
                                modopt_method = 'QRDAMP'
                                break
            if "RotaryInertia" in self._simulation_data:
                all_mass = self._simulation_data['RotaryInertia']
                if all_mass:
                    for m in all_mass:
                        _m = all_mass[m]
                        if 'Parameters' in _m:
                            if "ALPHA" in _m['Parameters']:
                                modopt_method = 'QRDAMP'
                                break
        frequency_analysis_commands += (
            f'! -------------------------- STEP: {self._step_counter} -----------------------\n'
        )
        if self._previous_analysis == "STATIC":
            frequency_analysis_commands += f'FINISH\n'
            frequency_analysis_commands += f'\n'
            frequency_analysis_commands += (
                f'/ASSIGN, rst, step_{self._step_counter}_modal_analysis, rst\n'
            )
            self._assign_analysis.append(f'step_{self._step_counter}_modal_analysis')
            frequency_analysis_commands += f'/SOLU\n'
        if self._previous_analysis != 'FREQUENCY':
            frequency_analysis_commands += f'ANTYPE, MODAL\n'
        frequency_analysis_commands += (
            f'MODOPT, {modopt_method}, {nmodes}, {min_frequency}, '
            f'{max_frequency}, {cpxmod}, {nrm_key}\n'
        )
        if res_modes:
            frequency_analysis_commands += f'RESVEC, {res_modes}\n'
            if not (
                ("Boundary" in self._curr_step and self._curr_step['Boundary'])
                or ("Boundary" in self._simulation_data and self._simulation_data['Boundary'])
            ):
                frequency_analysis_commands += 'KEYW, BETA, 1\n'
                frequency_analysis_commands += 'AIRL, AUTO\n'
        if (
            "MODAL DYNAMIC" in self._analysis_sequence
            or "STEADY STATE DYNAMICS" in self._analysis_sequence
        ):
            frequency_analysis_commands += f'MODCONT, ON\n'
        frequency_analysis_commands += f'MXPAND,,,,'
        if self.store_element_results():
            frequency_analysis_commands += f'YES,,NO'
        frequency_analysis_commands += f'\n'
        frequency_analysis_commands += f'\n'
        self._previous_analysis = "FREQUENCY"
        self._nrm_key = nrm_key
        return frequency_analysis_commands

    def get_steady_state_dynamics_data(self, steady_state_dynamics_data):
        """Get steady state dynamic details."""
        self._step_MSUP = False
        steady_state_dynamics_analysis_commands = ''
        if type(steady_state_dynamics_data) == list:
            steady_state_dynamics_data = steady_state_dynamics_data[0]
        npoints = 1
        min_frequency = ''
        max_frequency = ''
        hropt = 'MSUP'
        res_modes = None
        if self._previous_modal_resvec:
            res_modes = 'ON'
        if (
            'Data' in steady_state_dynamics_data
            and type(steady_state_dynamics_data['Data']) == list
        ):
            data = steady_state_dynamics_data['Data']
            first_line = data[0]
            if 'num_points' in first_line:
                npoints = int(first_line['num_points'])
            if 'min_frequency' in first_line:
                min_frequency = float(first_line['min_frequency'])
            if 'max_frequency' in first_line:
                max_frequency = float(first_line['max_frequency'])
        steady_state_dynamics_analysis_commands += (
            f'! --------------------------- STEP: {self._step_counter} -----------------------\n'
        )
        if self._previous_analysis == "FREQUENCY":
            steady_state_dynamics_analysis_commands += f'FINISH\n'
            steady_state_dynamics_analysis_commands += f'\n'
            steady_state_dynamics_analysis_commands += (
                f'/ASSIGN, rst, step_{self._step_counter}_harmonic_analysis, rst\n'
            )
            self._assign_analysis.append(f'step_{self._step_counter}_harmonic_analysis')
            steady_state_dynamics_analysis_commands += f'/SOLU\n'
        if self._previous_analysis != "STEADY STATE DYNAMICS":
            steady_state_dynamics_analysis_commands += f'ANTYPE, HARMONIC\n'
        steady_state_dynamics_analysis_commands += f'HARFRQ, {min_frequency}, {max_frequency}\n'
        steady_state_dynamics_analysis_commands += f'NSUB, {npoints-1}\n'
        if "FREQUENCY" in self._analysis_sequence[: self._step_counter]:
            # steady_state_dynamics_analysis_commands += f'MSUP\n'
            self._step_MSUP = True
        if self._previous_analysis != "STEADY STATE DYNAMICS":
            steady_state_dynamics_analysis_commands += f'HROUT, OFF\n'
            steady_state_dynamics_analysis_commands += f'KBC, 1\n'
            steady_state_dynamics_analysis_commands += f'HROPT, '
            if "FREQUENCY" in self._analysis_sequence[: self._step_counter]:
                steady_state_dynamics_analysis_commands += f'MSUP\n'
                # self._step_MSUP = True
                has_modal_output, has_velocities = self.check_modal_output()
                if has_modal_output:
                    steady_state_dynamics_analysis_commands += f' , , , YES'
                # if has_velocities:
                # steady_state_dynamics_analysis_commands += f' , , '
            else:
                steady_state_dynamics_analysis_commands += f'FULL\n'
            if res_modes:
                steady_state_dynamics_analysis_commands += f'RESVEC, {res_modes}\n'
        if self._analysis_sequence.count("STEADY STATE DYNAMICS") > 1:
            rpm = self._step_counter - self._analysis_sequence.index("STEADY STATE DYNAMICS") + 1
            steady_state_dynamics_analysis_commands += f'MRPM, {rpm}\n'
        steady_state_dynamics_analysis_commands += f'\n'
        self._previous_analysis = "STEADY STATE DYNAMICS"
        return steady_state_dynamics_analysis_commands

    def get_output_time_interval(self):
        time_interval = 0.0
        if "Output" in self._curr_step:
            output_data = self._curr_step["Output"]
            if not isinstance(output_data, list):
                return time_interval
            for output in output_data:
                if 'Parameters' in output:
                    # self._logger.info(output)
                    parameters = output['Parameters']
                    if 'TIME INTERVAL' in parameters:
                        # self._logger.info(parameters['TIME INTERVAL'])
                        new_time_interval = float(parameters['TIME INTERVAL'])
                        # old_time_interval = time_interval
                        if new_time_interval < time_interval or time_interval == 0.0:
                            # self._logger.info(f'new_time_interval: {new_time_interval}')
                            if time_interval != 0.0:
                                self._logger.warning(
                                    f"'TIME INTERVAL' argument on output keywords "
                                    f"has multiple values in different OUTPUT keywords, "
                                    f"minimum is used while solving"
                                )
                            time_interval = new_time_interval
        return time_interval

    def check_modal_output(self):
        has_modal_output = False
        has_velocities = False
        if "Output" in self._curr_step:
            output_data = self._curr_step["Output"]
            if not isinstance(output_data, list):
                return has_modal_output, has_velocities
            for output in output_data:
                if 'Data' in output and output['Data'] is not None:
                    if 'ModalOutput' in output['Data']:
                        has_modal_output = True
                        for modal_ouput in output['Data']['ModalOutput']:
                            # modal_ouput = output['ModalOutput']
                            for key in modal_ouput['Data']['keys']:
                                if key in ["GV", "GA", "GPV", "GPA", 'A', "A1", "A2", "A3"]:
                                    has_velocities = True
        return has_modal_output, has_velocities

    def get_maximum_output_interval(self):
        ninterval = 0
        if "Output" in self._curr_step:
            output_data = self._curr_step["Output"]
            if not isinstance(output_data, list):
                return ninterval
            for output in output_data:
                if 'Parameters' in output:
                    parameters = output['Parameters']
                    if 'NUMBER INTERVAL' in parameters:
                        new_ninterval = int(parameters['NUMBER INTERVAL'])
                        if new_ninterval > ninterval:
                            ninterval = new_ninterval
        return ninterval

    def store_element_results(self):
        store_el_results = False
        if "Output" in self._curr_step:
            output_data = self._curr_step["Output"]
            for output in output_data:
                if 'Data' in output and output['Data'] is not None:
                    if 'ElementOutput' in output['Data']:
                        for elemout in output['Data']['ElementOutput']:
                            if elemout is not None and elemout['Data'] is not None:
                                for key in elemout['Data']['keys']:
                                    if key in ["S"]:
                                        store_el_results = True
        return store_el_results

    def get_ninterval_mapdl_commands(self):
        return self._ninterval_mapdl_commands

    def get_output_analysis_data(self, output_data):
        """Get analysis output settings."""
        output_analysis_commands = ''
        if not isinstance(output_data, list):
            return output_analysis_commands
        time_points = None
        for output in output_data:
            if 'Parameters' in output:
                parameters = output['Parameters']
                if 'TIME POINT' in parameters:
                    if time_points is not None and time_points != parameters['TIME POINT']:
                        self._logger.warning(
                            f"Warning: There are multiple TIME POINT arrays "
                            f"used in *OUTPUT commands. Only first one will be used"
                        )
                    time_points = parameters['TIME POINT']
                if 'TIME POINTS' in parameters:
                    if time_points is not None and time_points != parameters['TIME POINTS']:
                        self._logger.warning(
                            f"Warning: There are multiple TIME POINT arrays "
                            f"used in *OUTPUT commands. Only first one will be used"
                        )
                    time_points = parameters['TIME POINTS']
        # above lines to be checked because of limitation on ansys OUTRES commands.
        if time_points is not None:
            time_points = get_modified_component_name(time_points)
        if len(output_data) > 0:
            output_analysis_commands += "\n"
            output_analysis_commands += "OUTRES, ERASE\n"
            output_analysis_commands += "OUTRES, ALL, NONE\n"
            if time_points:
                output_analysis_commands += f"OUTRES, EANGL, %{time_points}%\n"
            else:
                # output_analysis_commands += "OUTRES, ALL, NONE\n"
                # TODO Removed this line to avoid complications of
                # multiple tabular output controls with NINTERVAL
                output_analysis_commands += "OUTRES, EANGL, NONE\n"
                pass
            output_analysis_commands += "\n"

        number_interval_to_table = False
        for output in output_data:
            minimum_time_interval = self.get_output_time_interval()
            ninterval = None
            if 'Parameters' in output:
                parameters = output['Parameters']
                if 'NUMBER INTERVAL' in parameters:
                    self._ninterval_counter += 1
                    if number_interval_to_table:
                        sc = self._step_counter
                        ninc = self._ninterval_counter
                        ninterval = f"NINTERVAL_STEP_{sc}_N_{ninc}"
                        delta_time = self._step_end_time - self._step_start_time
                        # int_processor = _OutputIntervalProcessor(self._model)
                        ninterval_mapdl_commands = _OutputIntervalProcessor(
                            self._model
                        ).get_commands(
                            ninterval,
                            int(parameters['NUMBER INTERVAL']),
                            delta_time,
                            self._step_start_time,
                        )
                        self._ninterval_mapdl_commands += ninterval_mapdl_commands
                        # int_processor.write_interval_points_table_to_file(
                        # ninterval_mapdl_commands)
                    else:
                        ninterval = int(parameters['NUMBER INTERVAL'])
            nfreq = None
            if 'Parameters' in output:
                parameters = output['Parameters']
                if 'FREQUENCY' in parameters:
                    nfreq = parameters['FREQUENCY']
            time_interval = None
            if 'Parameters' in output:
                parameters = output['Parameters']
                if 'TIME INTERVAL' in parameters:
                    time_interval = float(parameters['TIME INTERVAL'])
            if time_interval and minimum_time_interval:
                nfreq = int(time_interval / minimum_time_interval)
            if 'Data' in output and output['Data'] is not None:
                if 'ModalOutput' in output['Data']:
                    output_analysis_commands += "MCFOPT, 1, , "
                    if self._nrm_key is not None:
                        if self._nrm_key == "OFF":
                            output_analysis_commands += "0\n"
                        else:
                            output_analysis_commands += "1\n"
                    # if 'Parameters' in nodeout:
                    #    if (
                    #        nodeout['Parameters'] is not None
                    #        and 'NSET' in nodeout['Parameters']
                    #    ):
                    #        output_analysis_commands += get_modified_component_name(
                    #            nodeout['Parameters']['NSET'],'NSET', self._simulation_data)
                if 'EnergyOutput' in output['Data']:
                    for enrgout in output['Data']['EnergyOutput']:
                        if enrgout is not None and enrgout['Data'] is not None:
                            # enrgout = output['EnergyOutput']
                            output_analysis_commands += "OUTRES, "
                            output_analysis_commands += "VENG, "
                            if time_points is not None:
                                output_analysis_commands += f'%{time_points}%, '
                            else:
                                if ninterval:
                                    if number_interval_to_table:
                                        output_analysis_commands += f'%{ninterval}%, '
                                    else:
                                        output_analysis_commands += f'-{ninterval}, '
                                elif nfreq:
                                    output_analysis_commands += f'{nfreq}, '
                                else:
                                    output_analysis_commands += 'ALL, '
                            if 'Parameters' in enrgout:
                                if (
                                    enrgout['Parameters'] is not None
                                    and 'ELSET' in enrgout['Parameters']
                                ):
                                    output_analysis_commands += get_modified_component_name(
                                        enrgout['Parameters']['ELSET'],
                                        'ELSET',
                                        self._simulation_data,
                                    )
                            output_analysis_commands += ', ,\n'
                if 'NodeOutput' in output['Data']:
                    for nodeout in output['Data']['NodeOutput']:
                        if nodeout is not None and nodeout['Data'] is not None:
                            # nodeout = output['NodeOutput']
                            for key in nodeout['Data']['keys']:
                                if key in [
                                    "RF",
                                    "U",
                                    "UT",
                                    "U1",
                                    "U2",
                                    "U3",
                                    "A",
                                    "A1",
                                    "A2",
                                    "A3",
                                    "CF",
                                ]:
                                    if key == "CF":
                                        if 'Parameters' in nodeout:
                                            if (
                                                nodeout['Parameters'] is not None
                                                and 'NSET' in nodeout['Parameters']
                                            ):
                                                output_analysis_commands += (
                                                    "CMSEL,S,"
                                                    + get_modified_component_name(
                                                        nodeout['Parameters']['NSET'],
                                                        'NSET',
                                                        self._simulation_data,
                                                    )
                                                    + ",NODE\n"
                                                )
                                                output_analysis_commands += (
                                                    "NSLE\nESEL,R,ELEM,,174\n"
                                                )
                                                output_analysis_commands += (
                                                    "CM,"
                                                    + get_modified_component_name(
                                                        nodeout['Parameters']['NSET'],
                                                        'NSET',
                                                        self._simulation_data,
                                                    )
                                                    + "_CONTACT, ELEM\n"
                                                )
                                                output_analysis_commands += "ALLSEL\n"
                                            else:
                                                output_analysis_commands += "ESEL,S,ENAME,,174\n"
                                                output_analysis_commands += "CM,All_CONTACT,ELEM\n"
                                                output_analysis_commands += "ALLSEL\n"
                                    output_analysis_commands += "OUTRES, "
                                    if key == "RF":
                                        output_analysis_commands += "RSOL, "
                                        if time_points is not None:
                                            output_analysis_commands += f'%{time_points}%, '
                                        else:
                                            if ninterval:
                                                if number_interval_to_table:
                                                    output_analysis_commands += f'%{ninterval}%, '
                                                else:
                                                    output_analysis_commands += f'-{ninterval}, '
                                            elif nfreq:
                                                output_analysis_commands += f'{nfreq}, '
                                            else:
                                                output_analysis_commands += 'ALL, '
                                    elif key in [
                                        "U",
                                        "UT",
                                        "U1",
                                        "U2",
                                        "U3",
                                        'A',
                                        "A1",
                                        "A2",
                                        "A3",
                                    ]:
                                        output_analysis_commands += "NSOL, "
                                        if time_points is not None:
                                            output_analysis_commands += f'%{time_points}%, '
                                        else:
                                            if ninterval:
                                                if number_interval_to_table:
                                                    output_analysis_commands += f'%{ninterval}%, '
                                                else:
                                                    output_analysis_commands += f'-{ninterval}, '
                                            elif nfreq:
                                                output_analysis_commands += f'{nfreq}, '
                                            else:
                                                output_analysis_commands += 'ALL, '
                                        if 'Parameters' in nodeout:
                                            if (
                                                nodeout['Parameters'] is not None
                                                and 'NSET' in nodeout['Parameters']
                                            ):
                                                output_analysis_commands += (
                                                    get_modified_component_name(
                                                        nodeout['Parameters']['NSET'],
                                                        'NSET',
                                                        self._simulation_data,
                                                    )
                                                )
                                    elif key == "CF":
                                        output_analysis_commands += "MISC, "
                                        if time_points is not None:
                                            output_analysis_commands += f'%{time_points}%, '
                                        else:
                                            if ninterval:
                                                if number_interval_to_table:
                                                    output_analysis_commands += f'%{ninterval}%, '
                                                else:
                                                    output_analysis_commands += f'-{ninterval}, '
                                            elif nfreq:
                                                output_analysis_commands += f'{nfreq}, '
                                            else:
                                                output_analysis_commands += 'ALL, '
                                        if 'Parameters' in nodeout:
                                            if (
                                                nodeout['Parameters'] is not None
                                                and 'NSET' in nodeout['Parameters']
                                            ):
                                                output_analysis_commands += (
                                                    get_modified_component_name(
                                                        nodeout['Parameters']['NSET'],
                                                        'NSET',
                                                        self._simulation_data,
                                                    )
                                                    + "_CONTACT"
                                                )
                                            else:
                                                output_analysis_commands += "All_CONTACT"
                                    output_analysis_commands += ', ,\n'
                                else:
                                    self._logger.warning(
                                        f"warning: node output key '{key}' is not processed."
                                    )
                if 'ElementOutput' in output['Data']:
                    for elemout in output['Data']['ElementOutput']:
                        if elemout is not None and elemout['Data'] is not None:
                            # elemout = output['ElementOutput']
                            for key in elemout['Data']['keys']:
                                if key in [
                                    "S",
                                    "CTF",
                                    "NFORC",
                                    "LE",
                                    "PEEQ",
                                    "SINV",
                                    "PE",
                                    "MISESMAX",
                                    "PEEQ",
                                    "PEEQMAX",
                                    "STH",
                                ]:
                                    output_analysis_commands += "OUTRES, "
                                    if key in ["S", "SINV", "MISESMAX"]:
                                        output_analysis_commands += "STRS, "
                                        if time_points is not None:
                                            output_analysis_commands += f'%{time_points}%, '
                                        else:
                                            if ninterval:
                                                if number_interval_to_table:
                                                    output_analysis_commands += f'%{ninterval}%, '
                                                else:
                                                    output_analysis_commands += f'-{ninterval}, '
                                            elif nfreq:
                                                output_analysis_commands += f'{nfreq}, '
                                            else:
                                                output_analysis_commands += 'ALL, '
                                        if 'Parameters' in elemout:
                                            if (
                                                elemout['Parameters'] is not None
                                                and 'ELSET' in elemout['Parameters']
                                            ):
                                                output_analysis_commands += (
                                                    get_modified_component_name(
                                                        elemout['Parameters']['ELSET'],
                                                        'ELSET',
                                                        self._simulation_data,
                                                    )
                                                )
                                    elif key in ["PEEQ", "PEEQMAX"]:
                                        output_analysis_commands += "NLDAT, "
                                        if time_points is not None:
                                            output_analysis_commands += f'%{time_points}%, '
                                        else:
                                            if ninterval:
                                                if number_interval_to_table:
                                                    output_analysis_commands += f'%{ninterval}%, '
                                                else:
                                                    output_analysis_commands += f'-{ninterval}, '
                                            elif nfreq:
                                                output_analysis_commands += f'{nfreq}, '
                                            else:
                                                output_analysis_commands += 'ALL, '
                                        if 'Parameters' in elemout:
                                            if (
                                                elemout['Parameters'] is not None
                                                and 'ELSET' in elemout['Parameters']
                                            ):
                                                output_analysis_commands += (
                                                    get_modified_component_name(
                                                        elemout['Parameters']['ELSET'],
                                                        'ELSET',
                                                        self._simulation_data,
                                                    )
                                                )
                                    elif key == "PE":
                                        out_cmds = ""
                                        out_cmds += "EPPL, "
                                        if time_points is not None:
                                            out_cmds += f'%{time_points}%, '
                                        else:
                                            if ninterval:
                                                if number_interval_to_table:
                                                    out_cmds += f'%{ninterval}%, '
                                                else:
                                                    out_cmds += f'-{ninterval}, '
                                            elif nfreq:
                                                out_cmds += f'{nfreq}, '
                                            else:
                                                out_cmds += 'ALL, '
                                        if 'Parameters' in elemout:
                                            if (
                                                elemout['Parameters'] is not None
                                                and 'ELSET' in elemout['Parameters']
                                            ):
                                                out_cmds += get_modified_component_name(
                                                    elemout['Parameters']['ELSET'],
                                                    'ELSET',
                                                    self._simulation_data,
                                                )
                                        output_analysis_commands += (
                                            out_cmds
                                            + ', ,\n'
                                            + "OUTRES, "
                                            + out_cmds.replace("EPPL", "NLDAT")
                                        )
                                    elif key == "STH":
                                        comp_name = ""
                                        out_cmds = ""
                                        if (
                                            'Parameters' in elemout
                                            and elemout['Parameters'] is not None
                                            and 'ELSET' in elemout['Parameters']
                                        ):
                                            comp_name += get_modified_component_name(
                                                elemout['Parameters']['ELSET'],
                                                'ELSET',
                                                self._simulation_data,
                                            )
                                        else:
                                            out_cmds += "ESEL, S, ENAME, , 181\n"
                                            out_cmds += "ESEL, A, ENAME, , 281\n"
                                            out_cmds += "CM, SHELL_THICKNESS_STORAGE, ELEM\n"
                                            out_cmds += "ALLSEL\n"
                                            comp_name += "SHELL_THICKNESS_STORAGE"
                                        output_analysis_commands = output_analysis_commands[:-8]
                                        output_analysis_commands += out_cmds
                                        output_analysis_commands += "OUTRES, "
                                        output_analysis_commands += "MISC, "
                                        if time_points is not None:
                                            output_analysis_commands += f'%{time_points}%, '
                                        else:
                                            if ninterval:
                                                if number_interval_to_table:
                                                    output_analysis_commands += f'%{ninterval}%, '
                                                else:
                                                    output_analysis_commands += f'-{ninterval}, '
                                            elif nfreq:
                                                output_analysis_commands += f'{nfreq}, '
                                            else:
                                                output_analysis_commands += 'ALL, '
                                        output_analysis_commands += comp_name
                                    elif key == "LE":
                                        output_analysis_commands += "EPEL, "
                                        if time_points is not None:
                                            output_analysis_commands += f'%{time_points}%, '
                                        else:
                                            if ninterval:
                                                if number_interval_to_table:
                                                    output_analysis_commands += f'%{ninterval}%, '
                                                else:
                                                    output_analysis_commands += f'-{ninterval}, '
                                            elif nfreq:
                                                output_analysis_commands += f'{nfreq}, '
                                            else:
                                                output_analysis_commands += 'ALL, '
                                        if 'Parameters' in elemout:
                                            if (
                                                elemout['Parameters'] is not None
                                                and 'ELSET' in elemout['Parameters']
                                            ):
                                                output_analysis_commands += (
                                                    get_modified_component_name(
                                                        elemout['Parameters']['ELSET'],
                                                        'ELSET',
                                                        self._simulation_data,
                                                    )
                                                )
                                    elif key == "CTF":
                                        output_analysis_commands += "MISC, "
                                        if time_points is not None:
                                            output_analysis_commands += f'%{time_points}%, '
                                        else:
                                            if ninterval:
                                                if number_interval_to_table:
                                                    output_analysis_commands += f'%{ninterval}%, '
                                                else:
                                                    output_analysis_commands += f'-{ninterval}, '
                                            elif nfreq:
                                                output_analysis_commands += f'{nfreq}, '
                                            else:
                                                output_analysis_commands += 'ALL, '
                                        if 'Parameters' in elemout:
                                            if (
                                                elemout['Parameters'] is not None
                                                and 'ELSET' in elemout['Parameters']
                                            ):
                                                output_analysis_commands += (
                                                    get_modified_component_name(
                                                        elemout['Parameters']['ELSET'],
                                                        'ELSET',
                                                        self._simulation_data,
                                                    )
                                                )
                                    elif key == "NFORC":
                                        output_analysis_commands += "NLOAD, "
                                        if time_points is not None:
                                            output_analysis_commands += f'%{time_points}%, '
                                        else:
                                            if ninterval:
                                                if number_interval_to_table:
                                                    output_analysis_commands += f'%{ninterval}%, '
                                                else:
                                                    output_analysis_commands += f'-{ninterval}, '
                                            elif nfreq:
                                                output_analysis_commands += f'{nfreq}, '
                                            else:
                                                output_analysis_commands += 'ALL, '
                                        if 'Parameters' in elemout:
                                            if (
                                                elemout['Parameters'] is not None
                                                and 'ELSET' in elemout['Parameters']
                                            ):
                                                output_analysis_commands += (
                                                    get_modified_component_name(
                                                        elemout['Parameters']['ELSET'],
                                                        'ELSET',
                                                        self._simulation_data,
                                                    )
                                                )
                                    output_analysis_commands += ', ,\n'
                                    last_line = output_analysis_commands.split("\n")[-2]
                                    if "STRS" in last_line and ", SEAM_WELD," in last_line:
                                        new_line = last_line.replace("STRS", "EANGL")
                                        output_analysis_commands += new_line + "\n"
                                else:
                                    self._logger.warning(
                                        f"warning: element output key '{key}' is not processed."
                                    )
                        if (
                            elemout['Parameters'] is not None
                            and 'POSITION' in elemout['Parameters']
                        ):
                            if elemout['Parameters']['POSITION'] == "CENTROIDAL":
                                output_analysis_commands += "RSTC, AUTO, "
                            if (
                                elemout['Parameters'] is not None
                                and 'ELSET' in elemout['Parameters']
                            ):
                                output_analysis_commands += get_modified_component_name(
                                    elemout['Parameters']['ELSET'], 'ELSET', self._simulation_data
                                )
                            output_analysis_commands += "\n"
        return output_analysis_commands

    def create_modal_vectors(self):
        vector_commands = ''
        steps_data = self._steps_data
        dof_map = {
            1: 'FX',
            2: 'FY',
            3: 'FZ',
            4: 'MX',
            5: 'MY',
            6: 'MZ',
        }
        if (
            "STEADY STATE DYNAMICS" in self._analysis_sequence
            or "MODAL DYNAMIC" in self._analysis_sequence
        ):
            count_load_vectors = 0
            # vector_commands += f'FDELE, ALL, ALL \n'
            # vector_commands += f'SFDELE, ALL, ALL \n'
            # vector_commands += f'SFEDELE, ALL, ALL, ALL \n'
            # vector_commands += f'ACEL, 0, 0, 0 \n'
            # vector_commands += f'\n'
            temp_count = 0
            for step_data in steps_data[self._step_counter :]:
                if self._previous_modal_resvec == None:
                    if temp_count != 0:
                        vector_commands += 'SOLVE\n'
                        vector_commands += '\n'
                    vector_commands += f'FDELE, ALL, ALL \n'
                    vector_commands += f'SFDELE, ALL, ALL \n'
                    vector_commands += f'SFEDELE, ALL, ALL, ALL \n'
                    vector_commands += f'ACEL, 0, 0, 0 \n'
                    vector_commands += f'\n'
                temp_count = 1
                if "Cload" in step_data:
                    cloads_data = step_data['Cload']
                    for cload_data in cloads_data:
                        data_lines = cload_data['Data']
                        for data_line in data_lines:
                            if len(data_line) == 0:
                                continue
                            dof = int(data_line['degree_of_freedom'])
                            mag = 0
                            if 'magnitude' in data_line:
                                mag = float(data_line['magnitude'])
                            if self._previous_modal_resvec:
                                if count_load_vectors != 0:
                                    vector_commands += 'SOLVE\n'
                                    vector_commands += '\n'
                                vector_commands += f'FDELE, ALL, ALL \n'
                                vector_commands += f'SFDELE, ALL, ALL \n'
                                vector_commands += f'SFEDELE, ALL, ALL, ALL \n'
                                vector_commands += f'ACEL, 0, 0, 0 \n'
                                vector_commands += f'\n'
                            if data_line['node_set'].isnumeric():
                                cmname = data_line['node_set']
                                vector_commands += (
                                    f"F, " f"{data_line['node_set']}, " f"{dof_map[dof]}, 1\n"
                                )
                            else:
                                cmname = get_modified_component_name(
                                    data_line['node_set'], 'NSET', self._simulation_data
                                )
                                vector_commands += f"F, " f"{cmname}, " f"{dof_map[dof]}, 1\n"
                            count_load_vectors += 1
                            self._modal_load_vectors[count_load_vectors] = {
                                'SET': cmname,
                                "COMP": dof_map[dof],
                            }
                if "BaseMotion" in step_data:
                    base_motions_data = step_data['BaseMotion']
                    for base_motion_data in base_motions_data:
                        params = base_motion_data['Parameters']
                        if len(params) == 0:
                            continue
                        base_name = ""
                        if 'BASE NAME' in params:
                            base_name = get_modified_component_name(
                                params['BASE NAME'], 'NSET', self._simulation_data
                            )
                        boundaries_for_motion = self.get_step_boundary_component_data(
                            self._curr_step["Boundary"], base_name
                        )
                        dof = int(params['DOF'])
                        scale = 0
                        if 'SCALE' in params:
                            scale = float(params['SCALE'])
                        if self._previous_modal_resvec:
                            if count_load_vectors != 0:
                                vector_commands += 'SOLVE\n'
                                vector_commands += '\n'
                            vector_commands += f'FDELE, ALL, ALL \n'
                            vector_commands += f'SFDELE, ALL, ALL \n'
                            vector_commands += f'SFEDELE, ALL, ALL, ALL \n'
                            vector_commands += f'ACEL, 0, 0, 0 \n'
                            vector_commands += f'\n'
                        for item in boundaries_for_motion:
                            vector_commands += f"F, {item}, {dof_map[dof]}, 1\n"
                            count_load_vectors += 1
                            self._modal_load_vectors[count_load_vectors] = {
                                'SET': base_name,
                                "COMP": dof_map[dof],
                            }
        # else:
        # vector_commands += 'SOLVE\n'
        return vector_commands

    def get_step_base_motion_data(self, base_motions_data):
        # self._logger.info(f"scale_factor = {self._scale_factor}")
        # self._logger.info(f"step_start_time = {self._step_start_time}")
        # self._logger.info(f"step_end_time = {self._step_end_time}")
        base_motion_processor = _BaseMotionProcessor(
            self._model,
            base_motions_data,
            self._step_start_time,
            self._step_end_time,
            self._step_MSUP,
            self._modal_load_vectors,
            sim_data=self._simulation_data,
        )
        # TODO this needs to be in List of cloads instead of single base_motion
        base_motion_commands = ''
        base_motion_commands += base_motion_processor.get_all_base_motion_commands()
        self._base_motion_ampl_commands += base_motion_processor.get_ampl_commands()
        return base_motion_commands

    def get_step_connector_motion_data(self, connector_motions_data):
        # self._logger.info(f"scale_factor = {self._scale_factor}")
        # self._logger.info(f"step_start_time = {self._step_start_time}")
        # self._logger.info(f"step_end_time = {self._step_end_time}")
        connector_motion_processor = _ConnectorMotionProcessor(
            self._model,
            connector_motions_data,
            self._step_start_time,
            self._step_end_time,
            sim_data=self._simulation_data,
        )
        # TODO this needs to be in List of cloads instead of single connector_motion
        connector_motion_commands = ''
        connector_motion_commands += connector_motion_processor.get_all_connector_motion_commands()
        self._connector_motion_ampl_commands += connector_motion_processor.get_ampl_commands()
        return connector_motion_commands

    def get_step_cload_data(self, cloads_data):
        # self._logger.info(f"scale_factor = {self._scale_factor}")
        # self._logger.info(f"step_start_time = {self._step_start_time}")
        # self._logger.info(f"step_end_time = {self._step_end_time}")
        cload_processor = _CloadProcessor(
            self._model,
            cloads_data,
            self._step_start_time,
            self._step_end_time,
            self._step_MSUP,
            self._modal_load_vectors,
            sim_data=self._simulation_data,
        )
        # TODO this needs to be in List of cloads instead of single Cload
        cload_commands = ''
        cload_commands += cload_processor.get_all_cload_commands()
        self._cload_ampl_commands += cload_processor.get_ampl_commands()
        return cload_commands

    def get_step_dload_data(self, dloads_data):
        dload_processor = _DloadProcessor(
            self._model,
            dloads_data,
            self._step_start_time,
            self._step_end_time,
            sim_data=self._simulation_data,
        )
        # TODO this needs to be in List of cloads instead of single Cload
        dload_commands = ''
        dload_commands += dload_processor.get_all_dload_commands()
        return dload_commands

    def get_step_boundary_data(self, boundaries_data):
        boundary_processor = _BoundaryProcessor(
            self._model,
            boundaries_data,
            self._step_start_time,
            self._step_end_time,
            sim_data=self._simulation_data,
        )
        # TODO this needs to be in List of boundaries instead of single Boundary
        boundary_commands = ''
        boundary_commands += boundary_processor.get_all_boundary_commands()
        self._boundary_ampl_commands += boundary_processor.get_ampl_commands()
        return boundary_commands

    def get_step_boundary_component_data(self, boundaries_data, base_name):
        boundary_processor = _BoundaryProcessor(
            self._model,
            boundaries_data,
            self._step_start_time,
            self._step_end_time,
            sim_data=self._simulation_data,
        )
        # TODO this needs to be in List of boundaries instead of single Boundary
        comp_names = []
        comp_names.extend(boundary_processor.get_boundary_comp_name_with_base_motion(base_name))
        return comp_names

    def get_global_damping_commnads(self, global_damping_data):
        global_damping_processor = _GlobalDampingProcessing(self._model, global_damping_data)
        (
            global_damping_commands,
            global_structural_damping,
        ) = global_damping_processor.get_global_damping_commands(
            self._previous_analysis, self._step_MSUP
        )
        if (
            'Frequency' in self._curr_step
            or self._analysis_sequence[self._step_counter - 1] == "FREQUENCY"
        ):
            self._global_structural_damping_value += global_structural_damping
        return global_damping_commands

    def get_monitor_commands(self, monitor_data):
        monitor_processor = _MonitorProcessor(self._model, monitor_data, self._simulation_data)
        monitor_commands = monitor_processor.get_monitor_commands()
        return monitor_commands

    def _get_current_step_analysis_type(self, step_data):
        mapdl_step_commands = '/solu\n'
        # processed_analysis_type = ["Static", "FREQUENCY",
        # "MODAL DYNAMIC", "DYNAMIC", "STEADY STATE DYNAMICS"]
        #
        # if "Static" in step_data:
        #     mapdl_step_commands = 'antype, static\n'
        # else:
        #     self._logger.warning("Analysis, type is not processed")
        #     pass
        return mapdl_step_commands

    def _process_step(self, step_data):
        self._curr_step = step_data

        if self._analysis_sequence[self._step_counter] == "STEADY STATE DYNAMICS":
            # self._logger.info(
            # f"Current step is {self._analysis_sequence[self._step_counter]}"
            # )
            self._step_start_time = 0.0
            self._step_end_time = 1.0

        function_maps = {
            'Cload': self.get_step_cload_data,
            'ConnectorMotion': self.get_step_connector_motion_data,
            'BaseMotion': self.get_step_base_motion_data,
            'Boundary': self.get_step_boundary_data,
            'Static': self.get_static_analysis_data,
            'Dynamic': self.get_dynamic_analysis_data,
            'ModalDynamic': self.get_modal_dynamic_analysis_data,
            'Output': self.get_output_analysis_data,
            'Dload': self.get_step_dload_data,
            'Frequency': self.get_frequency_analysis_data,
            'SteadyStateDynamics': self.get_steady_state_dynamics_data,
            'GlobalDamping': self.get_global_damping_commnads,
            'Monitor': self.get_monitor_commands,
        }
        keys = [
            'Static',
            'Dynamic',
            'ModalDynamic',
            'Frequency',
            'SteadyStateDynamics',
            'GlobalDamping',
            'Cload',
            'Boundary',
            'ConnectorMotion',
            'BaseMotion',
            'Dload',
            'Monitor',
            'Output',
        ]
        mapdl_step_commands = ''
        # self._logger.info(step_data.keys())
        for key in keys:
            if key in step_data:
                # self._logger.info('in Keys')
                # self._logger.info(function_maps(step_data[key]))
                function = function_maps[key]
                global_damp_value = 0.0
                if self._global_structural_damping_value:
                    global_damp_value = self._global_structural_damping_value
                key_commands = function(step_data[key])
                # if key == "GlobalDamping" and global_damp_value and (
                #     'SteadyStateDynamics' in step_data or
                #     'ModalDynamic' in step_data
                # ):
                if (
                    key == "GlobalDamping"
                    and global_damp_value
                    and 'SteadyStateDynamics' in step_data
                ):
                    key_commands = ""
                if key == "GlobalDamping" and 'Frequency' in step_data:
                    key_commands = "Placeholder_GlobalDamping\n"
                mapdl_step_commands += key_commands
                if key == "Output" and "Dynamic" in step_data:
                    if "STATIC" in self._analysis_sequence and "DYNAMIC" in self._analysis_sequence:
                        self._transient_output_controls = key_commands
                        self._transient_output_controls += "\nNROPT,FULL\n"
                if key == "Output" and "Static" in step_data:
                    if "STATIC" in self._analysis_sequence and "DYNAMIC" in self._analysis_sequence:
                        mapdl_step_commands += "Placeholder_Transient_Outres\n"
            # else:
            #     self._logger.warning("\nkey not found ", key)
        # self._logger.info(mapdl_step_commands)
        if 'Parameters' in step_data:
            step_params = step_data['Parameters']
            if step_params:
                if 'NLGEOM' in step_params:
                    mapdl_step_commands += "NLGEOM, "
                    if step_params['NLGEOM'] == "YES":
                        mapdl_step_commands += "ON\n"
                    else:
                        mapdl_step_commands += "OFF\n"
                if 'UNSYMM' in step_params:
                    if step_params['UNSYMM'] == "YES":
                        mapdl_step_commands += "NROPT, UNSYM\n"
        mapdl_step_commands += 'RESCONTROL,,NONE,NONE\n'
        mapdl_step_commands += '\n'
        mapdl_step_commands += 'DMPOPT,  RST, YES \n'
        mapdl_step_commands += 'DMPOPT, ESAV,  NO \n'
        mapdl_step_commands += 'DMPOPT, EMAT,  NO \n'
        mapdl_step_commands += 'DMPOPT, FULL,  NO \n'
        mapdl_step_commands += 'DMPOPT, MODE,  YES \n'
        mapdl_step_commands += 'DMPOPT,  MLV,  NO \n'
        mapdl_step_commands += '\n'
        if self._step_counter == 1 or 'AIRL, AUTO' in mapdl_step_commands:
            mapdl_step_commands += '/GST, ON, ON\n'
            mapdl_step_commands += '! Compress contact printout\n'
            mapdl_step_commands += 'CNTR, OUT, yes\n'
            mapdl_step_commands += '! Compress element type printout\n'
            mapdl_step_commands += 'OUTPR, ETYP, COMP\n'
            mapdl_step_commands += '\n'
            mapdl_step_commands += 'CNCH,DMP\n'
            # mapdl_step_commands += 'CNCH,DMP,,,,,,TRIM\n'
            # mapdl_step_commands += '!CNCH,DMP,,,,MPC,32,TRIM\n'
            # mapdl_step_commands += '!CNCH,OVER,,,,,2\n'
            mapdl_step_commands += '\n'
        if 'Frequency' in step_data:
            mapdl_step_commands += self.create_modal_vectors()
            # pass
        # if 'SteadyStateDynamics' in step_data:
        # # TODO use load vectors
        # pass
        mapdl_step_commands += 'SOLVE\n'
        return mapdl_step_commands

    def get_all_steps(self):
        mapdl_commands = []
        self._step_counter = 0
        self.get_analysis_sequence()
        for step_data in self._steps_data:
            # self._logger.info(step_data)
            self._step_counter += 1
            current_step_data = self._process_step(step_data)
            if 'AIRL, AUTO' in current_step_data:
                mapdl_commands = []
            mapdl_commands.append(current_step_data)

        steps_commands = '\n'.join(mapdl_commands)
        if "Placeholder_GlobalDamping" in steps_commands:
            steps_commands = steps_commands.replace(
                "Placeholder_GlobalDamping", f"DMPSTR, {self._global_structural_damping_value}"
            )
        if "Placeholder_Transient_Outres" in steps_commands and not self._transient_output_controls:
            updated_steps_commands = steps_commands.replace("Placeholder_Transient_Outres", "")
        elif "Placeholder_Transient_Outres" in steps_commands and self._transient_output_controls:

            all_lines = self._transient_output_controls.strip().split("\n")
            new_lines = []

            for i, line in enumerate(all_lines, 1):
                if i <= 3:
                    continue
                if "OUTRES" in line:
                    ln_data = line.split(",")
                    ln_data[2] = " LAST"
                    new_lines.append(",".join(ln_data))
                else:
                    new_lines.append(line)

            updated_steps_commands = steps_commands.replace(
                "Placeholder_Transient_Outres", "\n".join(new_lines) + "\n"
            )
        else:
            updated_steps_commands = steps_commands

        return updated_steps_commands

    def get_step_by_step_id(self, step_id):
        mapdl_commands = ''
        self._step_counter = 1
        self._time = 0.0
        self._previous_analysis = None
        self.get_analysis_sequence()
        for step_data in self._steps_data:
            if step_data['id'] == step_id:
                mapdl_commands += self._process_step(step_data)
        return mapdl_commands


class _AxialTempCorrection:
    __slots__ = (
        '_connector_sections',
        '_connector_behavior',
        '_element_wise_csys',
        '_enable_hm_comments',
        '_model',
        '_logger',
    )

    def __init__(
        self,
        model: prime.Model,
        connector_sections,
        connector_behavior,
        element_wise_csys=False,
        hm_comments=False,
    ):
        self._connector_sections = connector_sections
        self._connector_behavior = connector_behavior
        self._element_wise_csys = element_wise_csys
        self._enable_hm_comments = hm_comments
        self._model = model
        self._logger = model.python_logger

    def process_axial_connectors(self):
        axial_modification_string = ""
        for section in self._connector_sections:
            if self._connector_sections[section]['Data']['connection_type'] == 'AXIAL':
                if 'BEHAVIOR' in self._connector_sections[section]['Parameters']:
                    behavior_data = self._connector_behavior[
                        self._connector_sections[section]['Parameters']['BEHAVIOR']
                    ]
                    axial_modification_string += f"\n"
                    axial_modification_string += f"esel,s,mat,,{behavior_data['id']}\n"
                    axial_modification_string += f"eid = ELNEXT(0)\n"
                    axial_modification_string += self._modify_element_type(behavior_data)
                    axial_modification_string += self._modify_section_type(behavior_data)
                    axial_modification_string += self._modify_section_data(behavior_data)
                    axial_modification_string += 'allsel\n'
                else:
                    axial_modification_string += f"\n! Warning: the connector section "
                    f"'{section}' does not have behavior associated with it. "
                    f"these elements are not processed\n"
        return axial_modification_string

    def _modify_element_type(self, behavior_data):
        et_string = ''
        et_string += '*GET,type_id,ELEM,eid,ATTR,TYPE\n'
        et_string += 'ET,type_id,184\n'
        et_string += 'KEYOPT,type_id,1,16\n'
        et_string += 'KEYOPT,type_id,4,1\n'
        return et_string

    def _modify_section_type(self, behavior_data):
        sec_string = ''
        sec_string += '*GET,sec_id,ELEM,eid,ATTR,SECN\n'
        sec_string += 'SECTYPE,sec_id,JOINT,GENE\n'
        sec_string += 'SECJOINT,LSYS,IJX\n'
        sec_string += 'SECJOINT,RDOF,\n'
        return sec_string

    def _modify_section_data(self, behavior_data):
        secdata_string = ''
        if "CONNECTOR CONSTITUTIVE REFERENCE" in behavior_data:
            secdata_string += self._modify_section_type(behavior_data)
            joint_a_processor = _JointMaterialProcessor(
                self._model, self._connector_behavior, self._enable_hm_comments
            )
            ref_lens = joint_a_processor._precess_ref_length(
                behavior_data["CONNECTOR CONSTITUTIVE REFERENCE"]
            )
            secdata_string += 'SECDATA'
            for ref_len in ref_lens:
                secdata_string += f',{ref_len}'
            secdata_string += '\n'
        return secdata_string


def get_modified_component_name(name: str, set_type: str = None, sim_data=None) -> str:
    """
    Modify a component name to meet specific criteria.

    This function replaces any non-alphanumeric characters with underscores
    and adds the prefix "COMP_" if the name starts with a digit or underscore.

    Parameters
    ----------
    name : str
        The original component name.

    set_type : str
        The type of component (NSET, ELSET, SURFACE), used if there is a potential name conflict.

    sim_data
        The simulation data of the part in json format, used if there is a potential name conflict.

    Returns
    -------
    str
        The modified component name.

    Notes
    -----
    This function is designed to sanitize component names for specific use cases
    where restrictions might exist on allowed characters and initial characters.
    """
    modified_name = re.sub(r"[^\w]", "_", name)

    if set_type == 'NSET':
        has_surface = 'Surface' in sim_data and name in sim_data['Surface']
        has_nset = 'Nset' in sim_data and name in sim_data['Nset']
        has_elset = 'Elset' in sim_data and name in sim_data['Elset']
        has_element = 'Element' in sim_data and name in sim_data['Element']

        count = has_nset + (has_surface or has_elset or has_element)

        if count > 1:
            modified_name = set_type + "_" + modified_name

    if modified_name and (modified_name[0].isdigit() or modified_name[0] == "_"):
        modified_name = "COMP_" + modified_name

    return modified_name


def generate_mapdl_commands(
    model: prime.Model, simulation_data: str, params: ExportMapdlCdbParams
) -> Tuple[str, str]:
    """Generate the additional MAPDL commands to be added to the CDB export file.

    Parameters
    ----------
        model : prime.Model
            Model that the methods are to work on.
        simulation_data : str
            The simulation data of the part in json format.
        params : ExportMapdlCdbParams
            Parameters to export a CDB file.

    Returns
    -------
        Tuple[str, str]
            Two strings containing material settings and analysis settings respectively.

    Notes
    -----
    **This is a beta API**. **The behavior and implementation may change in future**.
    """
    all_mat_cmds = ''
    analysis_settings = ''
    json_simulation_data = json.loads(simulation_data)
    if json_simulation_data is None:
        if not simulation_data == 'null':
            model.python_logger.warning("Simulation data is empty")
        return all_mat_cmds, analysis_settings
    if "Materials" in json_simulation_data and json_simulation_data["Materials"] is not None:
        mp = _MaterialProcessor(
            model,
            json_simulation_data["Materials"],
            json_simulation_data["Zones"],
            params.write_separate_blocks,
            params.skip_comments,
        )
        mat_cmds = mp.get_all_material_commands()
        all_mat_cmds = mat_cmds
    if (
        "ConnectorBehavior" in json_simulation_data
        and json_simulation_data["ConnectorBehavior"] is not None
    ):
        jmp = _JointMaterialProcessor(
            model,
            json_simulation_data["ConnectorBehavior"],
            params.write_separate_blocks,
            params.skip_comments,
        )
        joint_all_mat_cmds = jmp.get_all_material_commands()
        all_mat_cmds += joint_all_mat_cmds
    general_contact_cmds = ''
    # if "Contact" in json_simulation_data and json_simulation_data["Contact"] is not None:
    #     surf_interaction = None
    #     if "SurfaceInteraction" in json_simulation_data:
    #         surf_interaction = json_simulation_data["SurfaceInteraction"]
    #     general_contact_processor = _GeneralContactProcessing(
    # model, json_simulation_data["Contact"], surf_interaction)
    #     general_contact_cmds += \
    # general_contact_processor.get_all_general_contact_commands()
    ampl_cmds = ''
    # if "Amplitude" in json_simulation_data:
    #     ampl_cmds += '/PREP7\n'
    if "TimePoint" in json_simulation_data:
        timepoint_processor = _TimePointsProcessor(model, json_simulation_data["TimePoint"])
        ampl_cmds += timepoint_processor.get_all_timepoints_commands()
    if "TimePoints" in json_simulation_data:
        timepoints_processor = _TimePointsProcessor(model, json_simulation_data["TimePoints"])
        ampl_cmds += timepoints_processor.get_all_timepoints_commands()
    pre_step_boun_cmds = ''
    boundary_ampl_cmds = ''
    if "Boundary" in json_simulation_data:
        boundary_processor = _BoundaryProcessor(
            model, json_simulation_data["Boundary"], sim_data=json_simulation_data
        )
        pre_step_boun_cmds = boundary_processor.get_all_boundary_commands()
        boundary_ampl_cmds = boundary_processor.get_ampl_commands()
    step_settings = ''
    ninterval_mapdl_commands = ''
    cload_ampl_commands = ''
    step_boundary_ampl_commands = ''
    connector_motion_ampl_commands = ''
    base_motion_ampl_commands = ''
    if "Step" in json_simulation_data:
        steps_data = _StepProcessor(
            model,
            json_simulation_data["Step"],
            sim_data=json_simulation_data,
            model_application=params.analysis_type,
        )
        step_settings = steps_data.get_all_steps()
        ninterval_mapdl_commands = steps_data.get_ninterval_mapdl_commands()
        cload_ampl_commands = steps_data.get_cload_ampl_commands()
        step_boundary_ampl_commands = steps_data.get_boundary_ampl_commands()
        connector_motion_ampl_commands = steps_data.get_connector_motion_ampl_commands()
        base_motion_ampl_commands = steps_data.get_base_motion_ampl_commands()

    all_mat_cmds += boundary_ampl_cmds
    all_mat_cmds += ninterval_mapdl_commands
    all_mat_cmds += cload_ampl_commands
    all_mat_cmds += step_boundary_ampl_commands
    all_mat_cmds += connector_motion_ampl_commands
    all_mat_cmds += base_motion_ampl_commands
    all_mat_cmds += ampl_cmds
    all_mat_cmds += 'allsel\n'

    # analysis_settings += '!--------------------------------------------------\n'
    # analysis_settings += '!--- Check Cohesive Materials in material file   --\n'
    # analysis_settings += '!--- Updates element SHELLs SOLIDs keyopts if any -\n'
    # analysis_settings += '!--- Update below settings in appropriate places --\n'
    # analysis_settings += '!--------------------------------------------------\n'
    # analysis_settings += '!NLGEOM, ON\n'
    # analysis_settings += '!dmpopt, rst, yes \n'
    # analysis_settings += '!dmpopt, esav, no \n'
    # analysis_settings += '!dmpopt, emat, no \n'
    # analysis_settings += '!dmpopt, full, no \n'
    # analysis_settings += '!dmpopt, mode, no \n'
    # analysis_settings += '!dmpopt, mlv, no \n'
    # analysis_settings += '!\n'
    # analysis_settings += '!! Compress contact printout\n'
    # analysis_settings += '!CNTR,OUT,yes\n'
    # analysis_settings += '!\n'
    # analysis_settings += '!! Compress element type printout\n'
    # analysis_settings += '!OUTPR,ETYP,COMP\n'
    # analysis_settings += '!\n'
    # analysis_settings += '!cnch,conv\n'
    # analysis_settings += '!-------------------------------------------------\n'
    # analysis_settings += '\n'
    analysis_settings += '\nALLSEL\n'
    if general_contact_cmds:
        analysis_settings += general_contact_cmds
        analysis_settings += '!-------------------------------------------------\n'
    if params.pre_solution_settings != None:
        analysis_settings += params.pre_solution_settings
        analysis_settings += '\n'
    analysis_settings += pre_step_boun_cmds
    # analysis_settings += '\n!CNCH,TRIM,,,,MPC\n'
    analysis_settings += '\nFINISH\n'
    analysis_settings += '\n/SOLU\n'
    # analysis_settings += 'ANTYPE,STATIC\n'
    # analysis_settings += '!-------------------------------------------------\n'
    # analysis_settings += '!--- Check Analysis Type                         -\n'
    # analysis_settings += '!-------------------------------------------------\n'
    # analysis_settings += 'f{pre_step_boun_cmds}\n'
    analysis_settings += step_settings
    analysis_settings += '\nFINISH\n'
    if params.analysis_settings != None:
        analysis_settings += params.analysis_settings
        analysis_settings += (
            '!--------------------------------------------------------------------------\n'
        )
        # analysis_settings += '/copy,file0,err,,errfile,tmp\n'
        # analysis_settings += '\n'
        analysis_settings += '/delete,,cnm,,1\n'
        analysis_settings += '/delete,,DSP,,\n'
        analysis_settings += '/delete,,mcf,,\n'
        analysis_settings += '/delete,,rfrq,,1\n'
        analysis_settings += '/delete,,log,,1\n'
        analysis_settings += '/delete,,emat,,1\n'
        analysis_settings += '/delete,,esav,,1\n'
        analysis_settings += '/delete,,err,,1\n'
        analysis_settings += '/delete,,full,,1\n'
        analysis_settings += '/delete,,mlv,,1\n'
        analysis_settings += '/delete,,mode,,1\n'
        # analysis_settings += '/delete,,rfrq,,1\n'
        analysis_settings += '/delete,,out,,1\n'
        # analysis_settings += '/delete,harmonic,rst,,1\n'
        analysis_settings += '!/delete,,mntr,,\n'
        analysis_settings += '/delete,,ldhi,,\n'
        analysis_settings += '/delete,,r001,,1\n'
        analysis_settings += '/delete,,rst,,1\n'
        analysis_settings += '/delete,,stat,,1\n'
        analysis_settings += '/delete,,db,,\n'
        analysis_settings += '/delete,,rdb,,\n'
        # analysis_settings += '\n'
        # analysis_settings += '/rename,errfile,tmp,,file,err\n'
        if "Step" in json_simulation_data:
            for an_name in steps_data._assign_analysis:
                analysis_settings += f'/delete,{an_name},rst,,1\n'
        analysis_settings += '/exit,nosave\n'
    return all_mat_cmds, analysis_settings
