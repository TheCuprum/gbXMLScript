from .vec2d import Vec2D
from .vec3d import Vec3D
from .math_util import MappingError

# 001 -> x, 010 -> y, 100 -> z
# every 2d coord -> map -> 3d coord
# def from_2d(vec2D:Vec2D, zValue: float = 0.0, xMap:int = 1, yMap:int = 2) -> Vec3D:
def from_2d(v2d:Vec2D, z_value: float = 0.0, x_map:int = 0b001, y_map:int = 0b010) -> Vec3D:
    flags = [False, False, False]
    coords = [0.0, 0.0, 0.0]
    for i in range(3):
        if (x_map >> i & 0b1) == 0b1:
            if not flags[i]:
                coords[i] = v2d.x
                flags[i] = True
            else:
                raise MappingError("info")

        if (y_map >> i & 0b1) == 0b1:
            if not flags[i]:
                coords[i] = v2d.y
                flags[i] = True
            else:
                raise MappingError()

        if not flags[i]:
            coords[i] = z_value

    return  Vec3D(coords[0], coords[1], coords[2])

# 01 -> x, 10 -> y
# def from_3d(v3d: 'Vec3D', x__map:int = 1, y_map:int = 2, z_map:int = 0) -> 'Vec2D':
def from_3d(v3d: Vec3D, x_map:int = 0b01, y_map:int = 0b10, z_map:int = 0b00) -> 'Vec2D':
    flags = [False, False]
    coords = [0.0, 0.0]
    for i in range(2):
        if (x_map >> i & 0b1) == 0b1:
            if not flags[i]:
                coords[i] = v3d.x
                flags[i] = True
            else:
                raise MappingError("info")

        if (y_map >> i & 0b1) == 0b1:
            if not flags[i]:
                coords[i] = v3d.y
                flags[i] = True
            else:
                raise MappingError("info")
            
        if (z_map >> i & 0b1) == 0b1:
            if not flags[i]:
                coords[i] = v3d.Z
                flags[i] = True
            else:
                raise MappingError("info")
    
    return Vec2D(coords[0], coords[1])
    