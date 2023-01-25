from typing import List, Tuple
import sys

sys.path.insert(1, "..")
from .structure_math import convert as converter
from .structure_math import math_util
from .base_calculator import BaseCalculator
from .structure_math.vec2d import Vec2D
from .structure_math.vec3d import Vec3D


class Segment3Calculator(BaseCalculator):
    def __init__(self, left_length: float, left_width: float, middle_length: float, middle_width: float,
                 right_length: float, right_width: float, height: float, left_angle: float, right_angle: float) -> None:
        self.left_length = left_length
        self.left_width = left_width
        self.middle_length = middle_length
        self.middle_width = middle_width
        self.right_length = right_length
        self.right_width = right_width
        self.height = height
        self.left_angle = left_angle
        self.right_angle = right_angle

    # vertex order
    # LB ABCD
    # RB ABCD
    # LT ABCD
    # RT ABCD
    #
    # DesignBuilder coord:
    # north = positive Y
    # east = positive X
    # _north: positive X ?
    # _east: positive Y ?

    def generate_surfaces_rect(self) -> List[Tuple[Vec3D, Vec3D, Vec3D, Vec3D]]:
        '''
        order:
            roof_west, roof_middle, roof_east,
            floor_west, floor_middle, floor_east,
            wall_east, wall_west, wall_north, wall_north_east, wall_north_west, wall_south, wall_south_east, wall_south_west
        '''
        tuple_lb = self.__calc_one_side_relative(
            self.left_length, self.left_width, self.middle_width, self.left_angle)
        tuple_rb = self.__calc_one_side_relative(
            self.right_length, self.right_width, self.middle_width, self.right_angle)
        A1 = converter.from_2d(tuple_lb[0], z_value=0.0)
        B1 = converter.from_2d(tuple_lb[1], z_value=0.0)
        C1 = converter.from_2d(tuple_lb[2], z_value=0.0)
        D1 = converter.from_2d(tuple_lb[3], z_value=0.0)
        A2 = converter.from_2d(tuple_rb[0], z_value=0.0) \
            .invert(invert_x=True, invert_y=False, invert_z=False) \
            .offset(self.middle_length, 0.0, 0.0)
        B2 = converter.from_2d(tuple_rb[1], z_value=0.0) \
            .invert(invert_x=True, invert_y=False, invert_z=False) \
            .offset(self.middle_length, 0.0, 0.0)
        C2 = converter.from_2d(tuple_rb[2], z_value=0.0) \
            .invert(invert_x=True, invert_y=False, invert_z=False) \
            .offset(self.middle_length, 0.0, 0.0)
        D2 = converter.from_2d(tuple_rb[3], z_value=0.0) \
            .invert(invert_x=True, invert_y=False, invert_z=False) \
            .offset(self.middle_length, 0.0, 0.0)
        A3 = Vec3D.offset_new(A1, 0.0, 0.0, self.height)
        B3 = Vec3D.offset_new(B1, 0.0, 0.0, self.height)
        C3 = Vec3D.offset_new(C1, 0.0, 0.0, self.height)
        D3 = Vec3D.offset_new(D1, 0.0, 0.0, self.height)
        A4 = Vec3D.offset_new(A2, 0.0, 0.0, self.height)
        B4 = Vec3D.offset_new(B2, 0.0, 0.0, self.height)
        C4 = Vec3D.offset_new(C2, 0.0, 0.0, self.height)
        D4 = Vec3D.offset_new(D2, 0.0, 0.0, self.height)

        floor_west = (A1, B1, C1, D1)
        floor_middle = (A2, A1, D1, D2)
        floor_east = (D2, C2, B2, A2)

        roof_west = (D3, C3, B3, A3)
        roof_middle = (A3, A4, D4, D3)
        roof_east = (A4, B4, C4, D4)

        wall_east = (C3, C1, B1, B3)
        wall_west = (B4, B2, C2, C4)
        wall_north = (D4, D2, D1, D3)
        wall_north_east = (D3, D1, C1, C3)
        wall_north_west = (C4, C2, D2, D4)
        wall_south = (A3, A1, A2, A4)
        wall_south_east = (B3, B1, A1, A3)
        wall_south_west = (A4, A2, B2, B4)

        return [
            roof_west, roof_middle, roof_east,
            floor_west, floor_middle, floor_east,
            wall_east, wall_west, wall_north, wall_north_east, wall_north_west, wall_south, wall_south_east, wall_south_west
        ]

    def generate_surfaces(self) -> List[Tuple[Vec3D, Vec3D, Vec3D, Vec3D]]:
        '''
        order:
            roof, floor,
            wall_east, wall_west, 
            wall_north, wall_north_east, wall_north_west, 
            wall_south, wall_south_east, wall_south_west
        '''
        tuple_lb = self.__calc_one_side_relative(
            self.left_length, self.left_width, self.middle_width, self.left_angle)
        tuple_rb = self.__calc_one_side_relative(
            self.right_length, self.right_width, self.middle_width, self.right_angle)
        A1 = converter.from_2d(tuple_lb[0], z_value=0.0)
        B1 = converter.from_2d(tuple_lb[1], z_value=0.0)
        C1 = converter.from_2d(tuple_lb[2], z_value=0.0)
        D1 = converter.from_2d(tuple_lb[3], z_value=0.0)
        A2 = converter.from_2d(tuple_rb[0], z_value=0.0) \
            .invert(invert_x=True, invert_y=False, invert_z=False) \
            .offset(self.middle_length, 0.0, 0.0)
        B2 = converter.from_2d(tuple_rb[1], z_value=0.0) \
            .invert(invert_x=True, invert_y=False, invert_z=False) \
            .offset(self.middle_length, 0.0, 0.0)
        C2 = converter.from_2d(tuple_rb[2], z_value=0.0) \
            .invert(invert_x=True, invert_y=False, invert_z=False) \
            .offset(self.middle_length, 0.0, 0.0)
        D2 = converter.from_2d(tuple_rb[3], z_value=0.0) \
            .invert(invert_x=True, invert_y=False, invert_z=False) \
            .offset(self.middle_length, 0.0, 0.0)
        A3 = Vec3D.offset_new(A1, 0.0, 0.0, self.height)
        B3 = Vec3D.offset_new(B1, 0.0, 0.0, self.height)
        C3 = Vec3D.offset_new(C1, 0.0, 0.0, self.height)
        D3 = Vec3D.offset_new(D1, 0.0, 0.0, self.height)
        A4 = Vec3D.offset_new(A2, 0.0, 0.0, self.height)
        B4 = Vec3D.offset_new(B2, 0.0, 0.0, self.height)
        C4 = Vec3D.offset_new(C2, 0.0, 0.0, self.height)
        D4 = Vec3D.offset_new(D2, 0.0, 0.0, self.height)

        roof = (A4, B4, C4, D4, D3, C3, B3, A3)
        floor = (A1, B1, C1, D1, D2, C2, B2, A2)

        wall_east = (C3, C1, B1, B3)
        wall_west = (B4, B2, C2, C4)
        wall_north = (D4, D2, D1, D3)
        wall_north_east = (D3, D1, C1, C3)
        wall_north_west = (C4, C2, D2, D4)
        wall_south = (A3, A1, A2, A4)
        wall_south_east = (B3, B1, A1, A3)
        wall_south_west = (A4, A2, B2, B4)

        return [
            roof, floor, 
            wall_east, wall_west, 
            wall_north, wall_north_east, wall_north_west, 
            wall_south, wall_south_east, wall_south_west
        ]


    def __calc_one_side_relative(self, sideLength: float, sideWidth: float, middleWidth: float, angle: float) -> Tuple[Vec2D, Vec2D, Vec2D, Vec2D]:
        sinA = math_util.round_sin(angle)
        cosA = math_util.round_cos(angle)
        tanA = math_util.round_tan(angle)

        # angle = 0 -> a line, 180 -> overlap
        pointA = Vec2D(0, 0)
        pointB = Vec2D((-1) * sideLength * cosA, sideLength * sinA)
        pointC = Vec2D(sideWidth * sinA - sideLength * cosA,
                       sideLength * sinA + sideWidth * cosA)
        pointD = Vec2D(sideWidth / sinA - middleWidth / tanA, middleWidth)

        # angle = 90 -> overlap, 0 -> L
        # pointA = Vec2D(0, 0)
        # pointB = Vec2D(sideLength * sinA, sideLength * cosA)
        # pointC = Vec2D(sideLength * sinA + sideWidth * cosA,
        #                sideLength * cosA - sideWidth * sinA)
        # pointD = Vec2D(middleWidth * tanA + sideWidth / cosA, middleWidth)

        return (pointA, pointB, pointC, pointD)
