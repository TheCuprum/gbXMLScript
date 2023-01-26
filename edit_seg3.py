from math import pi as PI

import xgbxml
from lxml import etree

from calculator.segment3_calculator_builder import Segment3CalculatorBuilder
from gb_tool import set_polyloop_and_surface

def edit_xml(seg3_builder: Segment3CalculatorBuilder):
    model = seg3_builder.build_calculator()
    cubiod_surfaces = model.generate_surfaces()
    # print(cubiod_surfaces)

    parser = xgbxml.get_parser('0.37')

    tree = etree.parse('xml/seg3_solid.xml', parser)
    gbxml = tree.getroot()

    surfaces = gbxml.Campus.Surfaces
    poly_loops = gbxml.Campus.Building.Space.ShellGeometry.ClosedShell.PolyLoops

    counter = 0
    handler_func_map = {
        'UndergroundSlab': lambda p, s: set_polyloop_and_surface(p, s, cubiod_surfaces[1]),
        'Roof':lambda p, s: set_polyloop_and_surface(p, s, cubiod_surfaces[0]),
        'ExteriorWall': lambda p, s: set_polyloop_and_surface(p, s, cubiod_surfaces[counter + 2])
    }
    for i in range(len(surfaces)):
        surf = surfaces[i]
        poly = poly_loops[i]
        handler_func_map.get(surf.surfaceType)(poly, surf)
        if surf.surfaceType == 'ExteriorWall':
            counter += 1

    # save the edited file
    tree.write('xml/edited_gbxml_file.xml', pretty_print=True)


if __name__ == '__main__':
    builder = Segment3CalculatorBuilder()
    builder.same_angle(0.5 * PI)
    builder.same_length_lr(8.0)
    builder.same_width(2.0)
    builder.set_value(middle_length=16.0, height=5.0)

    # builder.left_length
    # builder.left_width
    # builder.middle_length
    # builder.middle_width
    # builder.right_length
    # builder.right_width
    # builder.height
    # builder.left_angle
    # builder.right_angle
    edit_xml(builder)