from typing import List, Tuple

from .base_calculator import BaseCalculator
from .structure_math.vec3d import Vec3D


class CuboidCalculator(BaseCalculator):
    def __init__(self, origin: Vec3D, delta: Vec3D) -> None:
        super().__init__()
        self.origin: Vec3D = origin
        self.delta: Vec3D = delta

    def generate_surfaces(self) -> List[Tuple[Vec3D, Vec3D, Vec3D, Vec3D]]:
        '''
        Order:
        U, D, N, S, W, E
        '''
        A1 = self.origin
        B1 = Vec3D.offset_new(A1, self.delta.x, 0.0, 0.0)
        C1 = Vec3D.offset_new(A1, self.delta.x, self.delta.y, 0.0)
        D1 = Vec3D.offset_new(A1, 0.0, self.delta.y, 0.0)
        A2 = Vec3D.offset_new(A1, 0.0, 0.0, self.delta.z)
        B2 = Vec3D.offset_new(B1, 0.0, 0.0, self.delta.z)
        C2 = Vec3D.offset_new(C1, 0.0, 0.0, self.delta.z)
        D2 = Vec3D.offset_new(D1, 0.0, 0.0, self.delta.z)

        U = (A2, B2, C2, D2)
        D = (A1, D1, C1, B1)
        N = (C2, C1, D1, D2)
        S = (A2, A1, B1, B2)
        W = (D2, D1, A1, A2)
        E = (B2, B1, C1, C2)

        return [U, D, N, S, W, E]