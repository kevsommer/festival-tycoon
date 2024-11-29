import pytest
from .ViewportTransformer import ViewportTransformer

class TestViewportTransformer:
    @pytest.fixture
    def viewport_transformer(self):
        return ViewportTransformer()

    def test_zoom_in(self, viewport_transformer):
        viewport_transformer.zoom_in()
        assert viewport_transformer.zoom == 1.1
        viewport_transformer.zoom_in()
        assert viewport_transformer.zoom == 1.2

    def test_zoom_out(self, viewport_transformer):
        viewport_transformer.zoom_out()
        assert viewport_transformer.zoom == 0.9
        viewport_transformer.zoom_out()
        assert viewport_transformer.zoom == 0.8

    def test_move(self, viewport_transformer):
        viewport_transformer.move(10, 10)
        assert viewport_transformer.translate_x == 10
        assert viewport_transformer.translate_y == 10

    def test_transform_to_screen_coords(self, viewport_transformer):
        viewport_transformer.move(10, 20)
        assert viewport_transformer.transform_to_screen_coords((50, 32)) == (1020, 592)
        viewport_transformer.zoom_in()
        assert viewport_transformer.transform_to_screen_coords((50, 32)) == (1025, 595)

    def test_transform_to_world_coords(self, viewport_transformer):
        viewport_transformer.move(10, 20)
        assert viewport_transformer.transform_to_world_coords((1020, 592)) == (50, 32)
        viewport_transformer.zoom_in()
        assert viewport_transformer.transform_to_world_coords((1025, 595)) == (50, 32)
