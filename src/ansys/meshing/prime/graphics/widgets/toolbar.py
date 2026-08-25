# Copyright (C) 2024 - 2026 ANSYS, Inc. and/or its affiliates.
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

"""Module for shared behavior of the PyPrimeMesh toolbar buttons."""

from typing import Tuple

#: Side of every PyPrimeMesh toolbar button, in pixels.
BUTTON_SIZE = 30

#: Width of the border drawn around every PyPrimeMesh toolbar button, in pixels.
BUTTON_BORDER = 3


class ToolbarButton:
    """Placement and hover geometry shared by the PyPrimeMesh buttons.

    A button representation is a 2D prop, and VTK resolves what is under the cursor
    by picking, which only ever reports 3D props. Each button therefore records
    where it was placed so that hovering can be answered from its rectangle.
    """

    def _add_button(self, position: Tuple[int, int], **options):
        """Place the button on the toolbar and remember where it sits.

        Parameters
        ----------
        position : Tuple[int, int]
            Lower left corner of the button, in display coordinates.
        **options : dict
            Further arguments for the underlying checkbox button.

        Returns
        -------
        vtkButtonWidget
            Button that was added to the scene.
        """
        self._button_position = position
        return self.prime_plotter._backend.pv_interface.scene.add_checkbox_button_widget(
            self.callback,
            position=position,
            size=BUTTON_SIZE,
            border_size=BUTTON_BORDER,
            **options,
        )

    def contains(self, x: int, y: int) -> bool:
        """Return whether a display position lies over this button.

        Parameters
        ----------
        x : int
            Horizontal display coordinate.
        y : int
            Vertical display coordinate, measured from the bottom of the window.

        Returns
        -------
        bool
            ``True`` when the position is within the button.
        """
        left, bottom = self._button_position
        return left <= x <= left + BUTTON_SIZE and bottom <= y <= bottom + BUTTON_SIZE
