import pytest
from .Camera import Camera

class TestCamera:
    @pytest.fixture
    def camera(self):
        return Camera()

    def test_zoom_in(self, camera):
        camera.zoom_in()
        assert camera.zoom == 1.1
        camera.zoom_in()
        assert camera.zoom == 1.2

    def test_zoom_out(self, camera):
        camera.zoom_out()
        assert camera.zoom == 0.9
        camera.zoom_out()
        assert camera.zoom == 0.8

    def test_move(self, camera):
        camera.move(10, 10)
        assert camera.translate_x == 10
        assert camera.translate_y == 10

    def test_transform_to_screen_coords(self, camera):
        camera.move(10, 20)
        assert camera.transform_to_screen_coords((50, 32)) == (1020, 592)
        camera.zoom_in()
        assert camera.transform_to_screen_coords((50, 32)) == (1025, 595)

    def test_transform_to_world_coords(self, camera):
        camera.move(10, 20)
        assert camera.transform_to_world_coords((1020, 592)) == (50, 32)
        camera.zoom_in()
        assert camera.transform_to_world_coords((1025, 595)) == (50, 32)
