from typing import List


from calculator.structure_math.vec3d import Vec3D


def set_vertex_coords(gb_point, coords: Vec3D) -> None:
    point_coords = gb_point.Coordinates
    point_coords[0].text = str(coords.x)
    point_coords[1].text = str(coords.y)
    point_coords[2].text = str(coords.z)

def set_surface_vertex(gb_surface, vertices: List[Vec3D]) -> None:
    points = gb_surface.PlanarGeometry.PolyLoop.CartesianPoints
    for i in range(len(vertices)):
        set_vertex_coords(points[i], vertices[i])

def set_ploy_loop(gb_ploy_loop, vertices: List[Vec3D]) -> None:
    points = gb_ploy_loop.CartesianPoints
    for i in range(len(vertices)):
        set_vertex_coords(points[i], vertices[i])

def set_polyloop_and_surface(gb_ployloop, gb_surface, vertices: List[Vec3D]) -> None:
    set_ploy_loop(gb_ployloop, vertices)
    set_surface_vertex(gb_surface, vertices)