from typing import Any

# isort: split
from ansys.meshing.prime.autogen.part import Part as _Part

# isort: split
from ansys.meshing.prime.autogen.commonstructs import SetNameResults as SetNameResults
from ansys.meshing.prime.autogen.partstructs import PartSummaryParams


class Part(_Part):
    __doc__ = _Part.__doc__

    def __init__(self, model, id: int, object_id: int, name: str):
        """Initialize Part

        Parameters
        ----------
        model: ansys.meshing.prime.Model
            Model in which part is created
        id: int
            Id of the part provided by server
        object_id: int
            Object id provided by the server
        name: str
            Part name
        """
        self._model = model
        self._print_mesh = False
        self._print_id = False
        _Part.__init__(self, model, id, object_id, name)

    def __call__(self, *args: Any, **kwds: Any) -> str:
        """Callable interface of the Part.

        Gets summary of the part using supported keyword arguments as given below.

        Parameters
        ----------
        print_mesh : bool, optional
            Passing True will get the mesh summary along with part summary.
            The default is False.
        peint_id : bool, optional
            Passing True will get id's of topo entities/zonelets along with part summary.
            The default is False.

        Returns
        -------
        str
            Returns the summary of part.

        Examples
        --------
        >>> from ansys.meshing.prime import Model
        >>> model = client.model
        >>> part = model.get_part_by_name("Part.1")
        >>> print(part(print_mesh=True, print_id=True))
        """
        params = PartSummaryParams(
            model=self._model, print_id=self._print_id, print_mesh=self._print_mesh
        )
        for key, value in kwds.items():
            setattr(params, key, value)
            if key == 'print_mesh':
                params.print_mesh = value
            if key == 'print_id':
                params.print_id = value
        result = _Part.get_summary(self, params)
        return result.message

    def __str__(self) -> str:
        """Prints the summary of a part.

        Uses print_mesh and print_id properties to control the the summary of a part.

        Returns
        -------
        str
            Returns the summary of a part.

        Examples
        --------
        >>> from ansys.meshing.prime import Model
        >>> model = client.model
        >>> part = model.get_part_by_name("Part.1")
        >>> print(part)
        """
        params = PartSummaryParams(model=self._model)
        params.print_mesh = self._print_mesh
        params.print_id = self._print_id
        result = _Part.get_summary(self, params)
        return result.message

    def set_suggested_name(self, name: str) -> SetNameResults:
        """Sets the unique name for the part based on the given suggested name.


        Parameters
        ----------
        name : str
            Suggested name for the part.

        Returns
        -------
        SetNameResults
            Returns the results with assigned name of the part.


        Examples
        --------
        >>> part.set_suggested_name("part1")

        """
        result = _Part.set_suggested_name(self, name)
        self._name = result.assigned_name
        return result

    @property
    def print_mesh(self) -> bool:
        """When True, prints the mesh summary along with part summary. The default is False."""
        return self._print_mesh

    @print_mesh.setter
    def print_mesh(self, value: bool):
        self._print_mesh = value

    @property
    def print_id(self) -> bool:
        """When True, prints the id's of topoentities or zonelets along with part summary.
        The default is False.
        """
        return self._print_id

    @print_id.setter
    def print_id(self, value: bool):
        self._print_id = value
