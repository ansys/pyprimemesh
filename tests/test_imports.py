from ansys.meshing.prime import __symbols, __all__

def test_imports():
    """Test that all symbols in __all__ are imported from __symbols__."""
    symbols = list(__symbols.keys())
    for symbol in __all__:
        assert symbol in symbols, f"{symbol} is not in __symbols__"
       
    