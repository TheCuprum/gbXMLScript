import xgbxml
from lxml import etree

from calculator.cuboid_calculator import CuboidCalculator
from calculator.structure_math.vec3d import ZERO as Vec3D_ZERO
from calculator.structure_math.vec3d import Vec3D
from gb_tool import set_polyloop_and_surface

def edit_xml() -> None:
    block = CuboidCalculator(Vec3D_ZERO, Vec3D(10, 10, 6))
    cubiod_surfaces = block.generate_surfaces()
    # print(cubiod_surfaces)


    parser = xgbxml.get_parser('0.37')

    tree = etree.parse('xml/block-10-10-6.xml', parser)
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
    edit_xml()