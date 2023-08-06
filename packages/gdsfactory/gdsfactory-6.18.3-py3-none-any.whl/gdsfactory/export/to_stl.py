from __future__ import annotations

import pathlib
from typing import Optional, Tuple

from gdsfactory.component import Component
from gdsfactory.layers import LayerColors
from gdsfactory.tech import LAYER_STACK, LayerStack
from gdsfactory.types import Layer


def to_stl(
    component: Component,
    filepath: str,
    layer_colors: LayerColors,
    layer_stack: LayerStack = LAYER_STACK,
    exclude_layers: Optional[Tuple[Layer, ...]] = None,
) -> None:
    """Exports a Component into STL.

    Args:
        component: to export.
        filepath: to write STL to.
        layer_colors: layer colors from Klayout Layer Properties file.
        layer_stack: contains thickness and zmin for each layer.
        exclude_layers: layers to exclude.

    """
    import matplotlib.colors
    import shapely
    from trimesh.creation import extrude_polygon

    layer_to_thickness = layer_stack.get_layer_to_thickness()
    layer_to_zmin = layer_stack.get_layer_to_zmin()
    filepath = pathlib.Path(filepath)
    exclude_layers = exclude_layers or []

    for layer, polygons in component.get_polygons(by_spec=True).items():
        if (
            layer not in exclude_layers
            and layer in layer_to_thickness
            and layer in layer_to_zmin
        ):
            height = layer_to_thickness[layer]
            zmin = layer_to_zmin[layer]
            color_hex = layer_colors.get_from_tuple(layer).color
            color_rgb = matplotlib.colors.to_rgb(color_hex)
            filepath_layer = (
                filepath.parent
                / f"{filepath.stem}_{layer[0]}_{layer[1]}{filepath.suffix}"
            )
            for polygon in polygons:
                p = shapely.geometry.Polygon(polygon)
                mesh = extrude_polygon(p, height=height)
                mesh.apply_translation((0, 0, zmin))
                mesh.visual.face_colors = (*color_rgb, 0.5)
                mesh.export(filepath_layer)


if __name__ == "__main__":
    import gdsfactory as gf

    c = gf.components.taper_strip_to_ridge()
    to_stl(c, layer_colors=gf.layers.LAYER_COLORS, filepath="a.stl")
