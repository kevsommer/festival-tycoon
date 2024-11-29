from .AxialHexCoord import AxialHexCoord

class TestAxialHexCoord:
    
    def test_pixel_to_hex(self):
        assert AxialHexCoord.pixel_to_hex((50, 0)) == (1, 0)
        assert AxialHexCoord.pixel_to_hex((60, 0)) == (1, 0)
        assert AxialHexCoord.pixel_to_hex((60, 20)) == (1, 0)
        assert AxialHexCoord.pixel_to_hex((60, 60)) == (0, 1)
        assert AxialHexCoord.pixel_to_hex((62, 182)) == (0, 2)
        assert AxialHexCoord.pixel_to_hex((-23, 184)) == (-1, 2)
        
    def test_axial_round(self):
        assert AxialHexCoord.axial_round((0.2, 0.87)) == (0, 1)
        assert AxialHexCoord.axial_round((0.7, 0.87)) == (1, 1)
        assert AxialHexCoord.axial_round((0.2, 0.13)) == (0, 0)
        assert AxialHexCoord.axial_round((-0.7, 0.13)) == (-1, 0)
        assert AxialHexCoord.axial_round((-4.2, 3.87)) == (-4, 4)
        assert AxialHexCoord.axial_round((0.5, 0.48)) == (1, 0)
