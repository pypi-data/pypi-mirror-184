"""Classes and utilities for working with KLayout technology files (.lyp, .lyt).

This module enables conversion between gdsfactory settings and KLayout technology.
"""

import os
import pathlib
import re
import xml.dom.minidom
import xml.etree.ElementTree as ET
from typing import Dict, List, Optional, Set, Tuple, Union
from xml.dom.minidom import Node

from pydantic import BaseModel, Field, validator

from gdsfactory.config import PATH

Layer = Tuple[int, int]
ConductorViaConductorName = Tuple[str, str, str]


def append_file_extension(filename: Union[str, pathlib.Path], extension: str) -> str:
    """Try appending extension to file."""
    # Handle whether given with '.'
    if "." not in extension:
        extension = f".{extension}"

    if isinstance(filename, str) and not filename.endswith(extension):
        filename += extension

    if isinstance(filename, pathlib.Path) and not str(filename).endswith(extension):
        filename = filename.with_suffix(extension)
    return filename


def _strip_xml(node):
    """Strip XML of excess whitespace.

    Source: https://stackoverflow.com/a/16919069
    """
    for x in node.childNodes:
        if x.nodeType == Node.TEXT_NODE:
            if x.nodeValue:
                x.nodeValue = x.nodeValue.strip()
        elif x.nodeType == Node.ELEMENT_NODE:
            _strip_xml(x)


def make_pretty_xml(root: ET.Element) -> bytes:
    xml_doc = xml.dom.minidom.parseString(ET.tostring(root))

    _strip_xml(xml_doc)
    xml_doc.normalize()

    return xml_doc.toprettyxml(indent=" ", newl="\n", encoding="utf-8")


class LayerView(BaseModel):
    """KLayout layer properties.

    Docstrings copied from KLayout documentation (with some modifications):
    https://www.klayout.de/lyp_format.html

    Attributes:
        layer: GDSII layer.
        layer_in_name: Whether to display the name as 'name layer/datatype' rather than just the layer.
        width: This is the line width of the frame in pixels (or empty for the default which is 1).
        line_style: This is the number of the line style used to draw the shape boundaries.
            An empty string is "solid line". The values are "Ix" for one of the built-in styles
            where "I0" is "solid", "I1" is "dotted" etc.
        dither_pattern: This is the number of the dither pattern used to fill the shapes.
            The values are "Ix" for one of the built-in pattern where "I0" is "solid" and "I1" is "clear".
        frame_color: The color of the frames.
        fill_color: The color of the fill pattern inside the shapes.
        animation: This is a value indicating the animation mode.
            0 is "none", 1 is "scrolling", 2 is "blinking" and 3 is "inverse blinking".
        fill_brightness: This value modifies the brightness of the fill color. See "frame-brightness".
        frame_brightness: This value modifies the brightness of the frame color.
            0 is unmodified, -100 roughly adds 50% black to the color which +100 roughly adds 50% white.
        xfill: Whether boxes are drawn with a diagonal cross.
        marked: Whether the entry is marked (drawn with small crosses).
        transparent: Whether the entry is transparent.
        visible: Whether the entry is visible.
        valid: Whether the entry is valid. Invalid layers are drawn but you can't select shapes on those layers.
        group_members: Add a list of group members to the LayerView.
    """

    layer: Optional[Layer] = None
    layer_in_name: bool = False
    frame_color: Optional[str] = None
    fill_color: Optional[str] = None
    frame_brightness: Optional[int] = 0
    fill_brightness: Optional[int] = 0
    dither_pattern: Optional[str] = None
    line_style: Optional[str] = None
    valid: bool = True
    visible: bool = True
    transparent: bool = False
    width: Optional[int] = None
    marked: bool = False
    xfill: bool = False
    animation: int = 0
    group_members: Optional[Dict[str, "LayerView"]] = None

    def __init__(self, **data):
        """Initialize LayerView object."""
        super().__init__(**data)

        # Iterate through all items, adding group members as needed
        for name, field in self.__fields__.items():
            default = field.get_default()
            if isinstance(default, LayerView):
                self.group_members[name] = default

    @validator("frame_color", "fill_color")
    def check_color(cls, color):
        if color is None:
            return None

        from matplotlib.colors import CSS4_COLORS, is_color_like, to_hex

        if not is_color_like(color):
            raise ValueError(
                "LayerView 'color' must be a valid CSS4 color. "
                "For more info, see: https://www.w3schools.com/colors/colors_names.asp"
            )

        # Color given by name
        if isinstance(color, str) and color[0] != "#":
            return CSS4_COLORS[color.lower()]

        # Color either an RGBA tuple or a hex string
        else:
            return to_hex(color)

    def __str__(self):
        """Returns a formatted view of properties and their values."""
        return "LayerView:\n\t" + "\n\t".join(
            [f"{k}: {v}" for k, v in self.dict().items()]
        )

    def __repr__(self):
        """Returns a formatted view of properties and their values."""
        return self.__str__()

    def _get_xml_element(self, tag: str, name: str) -> ET.Element:
        """Get XML Element from attributes."""
        prop_keys = [
            "frame-color",
            "fill-color",
            "frame-brightness",
            "fill-brightness",
            "dither-pattern",
            "line-style",
            "valid",
            "visible",
            "transparent",
            "width",
            "marked",
            "xfill",
            "animation",
            "name",
            "source",
        ]
        el = ET.Element(tag)
        for prop_name in prop_keys:
            if prop_name == "source":
                layer = self.layer
                prop_val = f"{layer[0]}/{layer[1]}@1" if layer else "*/*@*"
            elif prop_name == "name":
                prop_val = name
                if self.layer_in_name:
                    prop_val += f" {self.layer[0]}/{self.layer[1]}"
            else:
                prop_val = getattr(self, "_".join(prop_name.split("-")), None)
                if isinstance(prop_val, bool):
                    prop_val = f"{prop_val}".lower()
            subel = ET.SubElement(el, prop_name)
            if prop_val is not None:
                subel.text = str(prop_val)
        return el

    def to_xml(self, name: str) -> ET.Element:
        """Return an XML representation of the LayerView."""
        props = self._get_xml_element("properties", name=name)
        for member_name, member in self.group_members.items():
            props.append(member._get_xml_element("group-members", name=member_name))
        return props


class CustomDitherPattern(BaseModel):
    """Custom dither pattern. See KLayout documentation for more info.

    Attributes:
        order: Order of pattern.
        pattern: Pattern to use.
    """

    order: int
    pattern: str

    def to_xml(self, name: str) -> ET.Element:
        el = ET.Element("custom-dither-pattern")

        subel = ET.SubElement(el, "pattern")
        lines = self.pattern.split("\n")
        if len(lines) == 1:
            subel.text = lines[0]
        else:
            for line in lines:
                ET.SubElement(subel, "line").text = line

        ET.SubElement(el, "order").text = str(self.order)
        ET.SubElement(el, "name").text = name
        return el


class CustomLineStyle(BaseModel):
    """Custom line style. See KLayout documentation for more info.

    Attributes:
        order: Order of pattern.
        pattern: Pattern to use.
    """

    order: int
    pattern: str

    def to_xml(self, name: str) -> ET.Element:
        el = ET.Element("custom-line-pattern")

        ET.SubElement(el, "pattern").text = self.pattern
        ET.SubElement(el, "order").text = str(self.order)
        ET.SubElement(el, "name").text = name
        return el


class CustomPatterns(BaseModel):
    dither_patterns: Dict[str, CustomDitherPattern] = Field(default_factory=dict)
    line_styles: Dict[str, CustomLineStyle] = Field(default_factory=dict)

    def to_yaml(self, filename: str) -> None:
        """Export custom patterns to a yaml file.

        Args:
            filename: Name of output file.
        """
        import yaml

        def _str_presenter(dumper: yaml.Dumper, data: str) -> yaml.ScalarNode:
            if "\n" in data:  # check for multiline string
                return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")
            return dumper.represent_scalar("tag:yaml.org,2002:str", data)

        append_file_extension(filename, ".yml")

        yaml.add_representer(str, _str_presenter)
        yaml.representer.SafeRepresenter.add_representer(str, _str_presenter)

        with open(filename, "w") as file:
            file.write(yaml.safe_dump_all([self.dict()], indent=2, sort_keys=False))

    @staticmethod
    def from_yaml(filename: str) -> "CustomPatterns":
        """Import a CustomPatterns object from a yaml file.

        Args:
            filename: Name of output file.
        """
        from omegaconf import OmegaConf

        with open(filename) as file:
            loaded_yml = OmegaConf.to_container(OmegaConf.load(file))
        if not (
            "dither_patterns" in loaded_yml.keys() or "line_styles" in loaded_yml.keys()
        ):
            raise KeyError("The yaml file is not properly formatted.")
        return CustomPatterns(**loaded_yml)

    def __str__(self):
        """Prints the number of each type of custom pattern."""
        return f"CustomPatterns: {len(self.dither_patterns)} dither patterns, {len(self.line_styles)} line styles"


def _process_name(
    name: str, layer_pattern: Union[str, re.Pattern]
) -> Optional[Tuple[str, bool]]:
    """Strip layer info from name if it exists.

    Args:
        name: XML-formatted name entry.
        layer_pattern: Regex pattern to match layers with.
    """
    if not name:
        return None
    layer_in_name = False
    match = re.search(layer_pattern, name)
    if match:
        name = name[: match.start()].strip()
        layer_in_name = True
    return name, layer_in_name


def _process_layer(
    layer: str, layer_pattern: Union[str, re.Pattern]
) -> Optional[Layer]:
    """Convert .lyp XML layer entry to a Layer.

    Args:
        layer: XML-formatted layer entry.
        layer_pattern: Regex pattern to match layers with.
    """
    match = re.search(layer_pattern, layer)
    if not match:
        raise OSError(f"Could not read layer {layer}!")
    v = match.group().split("/")
    return None if v == ["*", "*"] else (int(v[0]), int(v[1]))


def _properties_to_layerview(
    element: ET.Element, layer_pattern: Union[str, re.Pattern]
) -> Optional[Tuple[str, LayerView]]:
    """Read properties from .lyp XML and generate LayerViews from them.

    Args:
        element: XML Element to iterate over.
        layer_pattern: Regex pattern to match layers with.
    """
    prop_dict = {"layer_in_name": False}
    name = ""

    for property_element in element:
        tag = property_element.tag

        if tag == "name":
            name = _process_name(property_element.text, layer_pattern)
            if name is None:
                return None
            name, layer_in_name = name
            prop_dict["layer_in_name"] = layer_in_name
            continue
        elif tag == "source":
            val = _process_layer(property_element.text, layer_pattern)
            tag = "layer"
        elif tag == "group-members":
            continue
        else:
            val = property_element.text
        tag = "_".join(tag.split("-"))
        prop_dict[tag] = val

    prop_dict["group_members"] = {}
    for member in element.iterfind("group-members"):
        member_name, member_lv = _properties_to_layerview(member, layer_pattern)
        prop_dict["group_members"][member_name] = member_lv

    return name, LayerView(**prop_dict)


class LayerDisplayProperties(BaseModel):
    """A container for layer properties for KLayout layer property (.lyp) files.

    Attributes:
        layer_views: Dictionary of LayerViews describing how to display gds layers.
        custom_patterns: CustomPatterns object containing custom dither patterns and line styles.
    """

    layer_views: Dict[str, LayerView] = Field(default_factory=dict)
    custom_patterns: Optional[CustomPatterns] = None

    def __init__(self, **data):
        """Initialize LayerDisplayProperties object."""
        super().__init__(**data)

        for field in self.dict():
            val = getattr(self, field)
            if isinstance(val, LayerView):
                self.add_layer_view(name=field, layer_view=val)

    def add_layer_view(self, name: str, layer_view: Optional[LayerView]) -> None:
        """Adds a layer to LayerDisplayProperties.

        Args:
            name: Name of the LayerView.
            layer_view: LayerView to add.
        """
        if name in self.layer_views:
            raise ValueError(
                f"Adding {name!r} already defined {list(self.layer_views.keys())}"
            )
        else:
            self.layer_views[name] = layer_view

    def get_layer_views(self, exclude_groups: bool = False) -> Dict[str, LayerView]:
        """Return all LayerViews.

        Args:
            exclude_groups: Whether to exclude LayerViews that contain other LayerViews.
        """
        layers = {}
        for name, view in self.layer_views.items():
            if view.group_members and not exclude_groups:
                for member_name, member in view.group_members.items():
                    layers[member_name] = member
                continue
            layers[name] = view
        return layers

    def get_layer_view_groups(self) -> Dict[str, LayerView]:
        """Return the LayerViews that contain other LayerViews."""
        return {name: lv for name, lv in self.layer_views.items() if lv.group_members}

    def __str__(self) -> str:
        """Prints the number of LayerView objects in the LayerDisplayProperties object."""
        lvs = self.get_layer_views()
        groups = self.get_layer_view_groups()
        return (
            f"LayerDisplayProperties: {len(lvs)} layers ({len(groups)} groups)\n"
            f"\t{self.custom_patterns}"
        )

    def get(self, name: str) -> LayerView:
        """Returns Layer from name.

        Args:
            name: Name of layer.
        """
        if name not in self.layer_views:
            raise ValueError(f"Layer {name!r} not in {list(self.layer_views.keys())}")
        else:
            return self.layer_views[name]

    def __getitem__(self, val: str):
        """Allows accessing to the layer names like ls['gold2'].

        Args:
            val: Layer name to access within the LayerDisplayProperties.

        Returns:
            self.layers[val]: LayerView in the LayerDisplayProperties.

        """
        try:
            return self.layer_views[val]
        except Exception as error:
            raise ValueError(
                f"LayerView {val!r} not in LayerDisplayProperties {list(self.layer_views.keys())}"
            ) from error

    def get_from_tuple(self, layer_tuple: Layer) -> LayerView:
        """Returns LayerView from layer tuple.

        Args:
            layer_tuple: Tuple of (gds_layer, gds_datatype).

        Returns:
            LayerView
        """
        tuple_to_name = {v.layer: k for k, v in self.layer_views.items()}
        if layer_tuple not in tuple_to_name:
            raise ValueError(
                f"LayerView {layer_tuple} not in {list(tuple_to_name.keys())}"
            )

        name = tuple_to_name[layer_tuple]
        return self.layer_views[name]

    def get_layer_tuples(self) -> Set[Layer]:
        """Returns a tuple for each layer."""
        return {layer.layer for layer in self.get_layer_views().values()}

    def to_lyp(
        self, filepath: Union[str, pathlib.Path], overwrite: bool = True
    ) -> None:
        """Write all layer properties to a KLayout .lyp file.

        Args:
            filepath: to write the .lyp file to (appends .lyp extension if not present).
            overwrite: Whether to overwrite an existing file located at the filepath.
        """
        filepath = pathlib.Path(filepath)
        filepath = append_file_extension(filepath, ".lyp")

        if os.path.exists(filepath) and not overwrite:
            raise OSError("File exists, cannot write.")

        root = ET.Element("layer-properties")

        for name, lv in self.layer_views.items():
            root.append(lv.to_xml(name))

        if self.custom_patterns is not None:
            for name, dp in self.custom_patterns.dither_patterns.items():
                root.append(dp.to_xml(name))

            for name, ls in self.custom_patterns.line_styles.items():
                root.append(ls.to_xml(name))

        with open(filepath, "wb") as file:
            # Write lyt to file
            file.write(make_pretty_xml(root))

    @staticmethod
    def from_lyp(
        filepath: str, layer_pattern: Optional[Union[str, re.Pattern]] = None
    ) -> "LayerDisplayProperties":
        r"""Write all layer properties to a KLayout .lyp file.

        Args:
            filepath: to write the .lyp file to (appends .lyp extension if not present).
            layer_pattern: Regex pattern to match layers with. Defaults to r'(\d+|\*)/(\d+|\*)'.
        """
        layer_pattern = re.compile(layer_pattern or r"(\d+|\*)/(\d+|\*)")

        filepath = append_file_extension(filepath, ".lyp")

        if not os.path.exists(filepath):
            raise OSError("File not found!")

        tree = ET.parse(filepath)
        root = tree.getroot()
        if root.tag != "layer-properties":
            raise OSError("Layer properties file incorrectly formatted, cannot read.")

        layer_views = {}
        for properties_element in root.iter("properties"):
            name, lv = _properties_to_layerview(
                properties_element, layer_pattern=layer_pattern
            )
            if lv:
                layer_views[name] = lv

        custom_dither_patterns = {}
        for dither_block in root.iter("custom-dither-pattern"):
            name = dither_block.find("name").text
            order = dither_block.find("order").text

            if name is None or order is None:
                continue

            custom_dither_patterns[name] = CustomDitherPattern(
                order=int(order),
                pattern="\n".join(
                    [line.text for line in dither_block.find("pattern").iter()]
                ),
            )
        custom_line_styles = {}
        for line_block in root.iter("custom-line-style"):
            name = line_block.find("name").text
            order = line_block.find("order").text

            if name is None or order is None:
                continue

            custom_line_styles[name] = CustomLineStyle(
                order=int(order),
                pattern=line_block.find("pattern").text,
            )
        custom_patterns = CustomPatterns(
            dither_patterns=custom_dither_patterns, line_styles=custom_line_styles
        )

        return LayerDisplayProperties(
            layer_views=layer_views, custom_patterns=custom_patterns
        )

    def to_yaml(self, layer_file: str, pattern_file: Optional[str] = None) -> None:
        """Export layer properties to two yaml files.

        Args:
            layer_file: Name of the file to write LayerViews to.
            pattern_file: Name of the file to write custom dither patterns and line styles to.
        """
        import yaml

        append_file_extension(layer_file, ".yml")
        lvs = {name: lv.dict() for name, lv in self.layer_views.items()}
        with open(layer_file, "w") as lf:
            lf.write(yaml.safe_dump_all([lvs], indent=2, sort_keys=False))

        if pattern_file:
            append_file_extension(pattern_file, ".yml")
            self.custom_patterns.to_yaml(pattern_file)

    @staticmethod
    def from_yaml(
        layer_file: str = None, pattern_file: Optional[str] = None
    ) -> "LayerDisplayProperties":
        """Import layer properties from two yaml files.

        Args:
            layer_file: Name of the file to read LayerViews from.
            pattern_file: Name of the file to read custom dither patterns and line styles from.
        """
        from omegaconf import OmegaConf

        append_file_extension(layer_file, ".yml")

        with open(layer_file) as lf:
            layers = OmegaConf.to_container(OmegaConf.load(lf))
        props = LayerDisplayProperties(
            layer_views={name: LayerView(**lv) for name, lv in layers.items()}
        )
        if pattern_file:
            append_file_extension(pattern_file, ".yml")
            props.custom_patterns = CustomPatterns.from_yaml(pattern_file)
        return props


class KLayoutTechnology(BaseModel):
    """A container for working with KLayout technologies (requires KLayout Python package).

    Useful for importing/exporting Layer Properties (.lyp) and Technology (.lyt) files.

    Properties:
        layer_properties: Defines all the layer display properties needed for a .lyp file from LayerView objects.
        technology: KLayout Technology object from the KLayout API. Set name, dbu, etc.
        connectivity: List of layer names connectivity for netlist tracing.
    """

    # TODO: Add import method
    import klayout.db as db

    name: str
    layer_properties: Optional[LayerDisplayProperties] = None
    technology: db.Technology = Field(default_factory=db.Technology)
    connectivity: Optional[List[ConductorViaConductorName]] = None

    def export_technology_files(
        self,
        tech_dir: str,
        lyp_filename: str = "layers",
        lyt_filename: str = "tech",
        d25_filename: str = "generic",
        layer_stack: Optional = None,
        mebes_config: Optional[dict] = None,
    ) -> None:
        """Write technology files into 'tech_dir'.

        Args:
            tech_dir: Where to write the technology files to.
            lyp_filename: Name of the layer properties file.
            lyt_filename: Name of the layer technology file.
            d25_filename: Name of the 2.5D stack file (only works on KLayout >= 0.28)
            layer_stack: If specified, write a 2.5D section in the technology file based on the LayerStack.
            mebes_config: A dictionary specifying the KLayout mebes reader config.
        """
        # Format file names if necessary
        tech_path = pathlib.Path(tech_dir)
        lyp_path = tech_path / append_file_extension(lyp_filename, ".lyp")
        lyt_path = tech_path / append_file_extension(lyt_filename, ".lyt")
        d25_path = tech_path / "d25" / append_file_extension(d25_filename, ".lyd25")

        if not self.technology.name:
            self.technology.name = self.name

        self.technology.layer_properties_file = lyp_path.name
        # TODO: Also interop with xs scripts?

        # Write lyp to file
        self.layer_properties.to_lyp(lyp_path)

        root = ET.XML(self.technology.to_xml().encode("utf-8"))

        # KLayout tech doesn't include mebes config, so add it after lefdef config:
        if not mebes_config:
            mebes_config = {
                "invert": False,
                "subresolution": True,
                "produce-boundary": True,
                "num-stripes-per-cell": 64,
                "num-shapes-per-cell": 0,
                "data-layer": 1,
                "data-datatype": 0,
                "data-name": "DATA",
                "boundary-layer": 0,
                "boundary-datatype": 0,
                "boundary-name": "BORDER",
                "layer-map": "layer_map()",
                "create-other-layers": True,
            }
        mebes = ET.Element("mebes")
        for k, v in mebes_config.items():
            v = str(v).lower() if isinstance(v, bool) else str(v)
            ET.SubElement(mebes, k).text = v

        reader_opts = root.find("reader-options")
        lefdef_idx = list(reader_opts).index(reader_opts.find("lefdef"))
        reader_opts.insert(lefdef_idx + 1, mebes)

        if layer_stack is not None:
            # KLayout 0.27.x won't have a way to read/write the 2.5D info for technologies, so add manually to xml
            d25_element = root.find("d25")

            # Would be nice to have a klayout.__version__ to check
            klayout28 = d25_element is None

            dbu = len(str(self.technology.dbu).split(".")[-1])

            d25_script = layer_stack.get_klayout_3d_script(
                klayout28=klayout28,
                layer_display_properties=self.layer_properties,
                dbu=dbu,
            )

            if klayout28:
                d25_script = f'# "{self.name}" 2.5D script generated by GDSFactory\n\n{d25_script}'
                d25_path.write_bytes(d25_script.encode("utf-8"))
            else:
                src_element = d25_element.find("src")
                src_element.text = d25_script

        # root['connectivity']['connection']= '41/0,44/0,45/0'
        if self.connectivity is not None:
            src_element = [e for e in list(root) if e.tag == "connectivity"]
            if len(src_element) != 1:
                raise KeyError("Could not get a single index for the src element.")
            src_element = src_element[0]
            for layer_name_c1, layer_name_via, layer_name_c2 in self.connectivity:
                layer_c1 = self.layer_properties.layer_views[layer_name_c1].layer
                layer_via = self.layer_properties.layer_views[layer_name_via].layer
                layer_c2 = self.layer_properties.layer_views[layer_name_c2].layer
                connection = ",".join(
                    [
                        f"{layer[0]}/{layer[1]}"
                        for layer in [layer_c1, layer_via, layer_c2]
                    ]
                )

                ET.SubElement(src_element, "connection").text = connection

        # Write lyt to file
        lyt_path.write_bytes(make_pretty_xml(root))

    class Config:
        """Allow db.Technology type."""

        arbitrary_types_allowed = True


LAYER_PROPERTIES = LayerDisplayProperties.from_lyp(str(PATH.klayout_lyp))


def yaml_test():
    tech_dir = PATH.repo / "extra" / "test_tech"

    # Load from existing layer properties file
    lyp = LayerDisplayProperties.from_lyp(str(PATH.klayout_lyp))
    print("Loaded from .lyp", lyp)

    # Export layer properties to yaml files
    layer_yaml = str(tech_dir / "layers.yml")
    pattern_yaml = str(tech_dir / "patterns.yml")
    lyp.to_yaml(layer_yaml, pattern_yaml)

    # Load layer properties from yaml files and check that they're the same
    lyp_loaded = LayerDisplayProperties.from_yaml(layer_yaml, pattern_yaml)
    print("Loaded from .yaml", lyp_loaded)

    assert lyp_loaded == lyp


if __name__ == "__main__":
    from gdsfactory.tech import LAYER_STACK

    lyp = LayerDisplayProperties.from_lyp(str(PATH.klayout_lyp))

    # str_xml = open(PATH.klayout_tech / "tech.lyt").read()
    # new_tech = db.Technology.technology_from_xml(str_xml)
    # generic_tech = KLayoutTechnology(layer_properties=lyp)
    #
    connectivity = [("M1", "VIA1", "M2"), ("M2", "VIA2", "M3")]

    c = generic_tech = KLayoutTechnology(
        name="test_tech", layer_properties=lyp, connectivity=connectivity
    )
    tech_dir = PATH.repo / "extra" / "test_tech"
    # tech_dir = pathlib.Path("/home/jmatres/.klayout/salt/gdsfactory/tech/")
    tech_dir.mkdir(exist_ok=True, parents=True)

    generic_tech.export_technology_files(tech_dir=tech_dir, layer_stack=LAYER_STACK)

    yaml_test()
