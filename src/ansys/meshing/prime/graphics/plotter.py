from ansys.visualizer import PlotterInterface
from beartype.typing import Any, Dict, List, Optional, Union


class PrimePlotter(PlotterInterface):
    def __init__(
        self, use_trame: Optional[bool] = None, allow_picking: Optional[bool] = False
    ) -> None:
        super().init(use_trame, allow_picking)
