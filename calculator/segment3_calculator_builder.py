from typing import Union

from .segment3_calculator import Segment3Calculator


class Segment3CalculatorBuilder():
    def __init__(self) -> None:
        self.left_length = -1.0
        self.left_width = -1.0
        self.middle_length = -1.0
        self.middle_width = -1.0
        self.right_length = -1.0
        self.right_width = -1.0

        self.height: Union[float, None] = None

        self.left_angle: Union[float, None] = None
        self.right_angle: Union[float, None] = None

    def set_value(self, left_length=-1.0, left_width=-1.0,
                    middle_length=-1.0, middle_width=-1.0,
                    right_length=-1.0, right_width=-1.0,
                    height=None,
                    left_angle=None, right_angle=None) -> 'Segment3CalculatorBuilder':
        if (left_length > 0):
            self.left_length = left_length
        if (left_width > 0):
            self.left_width = left_width
        if (middle_length > 0):
            self.middle_length = middle_length
        if (middle_width > 0):
            self.middle_width = middle_width
        if (right_length > 0):
            self.right_length = right_length
        if (right_width > 0):
            self.right_width = right_width

        if height is not None:
            self.height = height

        if left_angle is not None:
            self.left_angle = left_angle
        if right_angle is not None:
            self.right_angle = right_angle

        return self

    def same_width(self, width: float) -> 'Segment3CalculatorBuilder':
        self.left_width = width
        self.middle_width = width
        self.right_width = width
        return self

    def same_width_lr(self, width: float) -> 'Segment3CalculatorBuilder':
        self.left_width = width
        self.right_width = width
        return self

    def same_length(self, length: float) -> 'Segment3CalculatorBuilder':
        self.left_length = length
        self.middle_length = length
        self.right_length = length
        return self

    def same_length_lr(self, length: float) -> 'Segment3CalculatorBuilder':
        self.left_length = length
        self.right_length = length
        return self

    def same_angle(self, angle: float) -> 'Segment3CalculatorBuilder':
        '''
        unit: radian
        '''
        self.left_angle = angle
        self.right_angle = angle
        return self

    def build_calculator(self) -> Segment3Calculator:
        if ((self.left_length > 0) and (self.left_width > 0)
            and (self.middle_length > 0) and (self.middle_width > 0)
            and (self.right_length > 0) and (self.right_width > 0)
            and (self.height is not None) and (self.left_angle is not None) and (self.right_angle is not None)):
            return Segment3Calculator(
                self.left_length, self.left_width, self.middle_length, self.middle_width,
                self.right_length, self.right_width, self.height,
                self.left_angle, self.right_angle)
        return None