""" Auto-generated file. DO NOT MODIFY """
# Copyright 2023 ANSYS, Inc.
# Unauthorized use, distribution, or duplication is prohibited.
from __future__ import annotations
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from typing import List, Any

class CoreObject(object):
    """

    """

    __isfrozen = False

    def __setattr__(self, key, value) :
        """ __setattr__(CoreObject self, key, value)"""
        if self.__isfrozen and not hasattr(self, key) :
           raise TypeError("%r is an invalid attribute" % key)
        object.__setattr__(self, key, value)

    def _freeze(self) :
        """ _freeze(CoreObject self)"""
        self.__isfrozen = True

    def _unfreeze(self) :
        """ _freeze(CoreObject self)"""
        self.__isfrozen = False
