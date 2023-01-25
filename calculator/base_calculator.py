from typing import List, Tuple

from .structure_math.vec3d import Vec3D


class BaseCalculator():
    def __init__(self) -> None:
        pass

    def generate_surfaces(self) -> List[Tuple[Vec3D, Vec3D, Vec3D, Vec3D]]:
        return NotImplemented