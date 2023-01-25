from math import sqrt


class Vec2D():
    def __init__(self, x: float, y: float) -> None:
        self.x: float = x
        self.y: float = y

    def __neg__(self):
        return self.invert()

    def __add__(self, other) -> 'Vec2D':
        if not isinstance(other, Vec2D):
            return NotImplemented
        return Vec2D(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        if not isinstance(other, Vec2D):
            return NotImplemented
        return self.offset(other.x, other.y)

    def __sub__(self, other) -> 'Vec2D':
        if not isinstance(other, Vec2D):
            return NotImplemented
        return Vec2D(self.x - other.x, self.y - other.y)

    def __isub__(self, other):
        if not isinstance(other, Vec2D):
            return NotImplemented
        return self.offset(-other.x, -other.y)

    def __mul__(self, other) -> float:
        if not isinstance(other, Vec2D):
            return NotImplemented
        return self.x * other.x + self.y * other.y

    def __rmul__(self, other) -> 'Vec2D':
        if isinstance(other, (float, int)):
            return Vec2D(self.x * other, self.y * other)
        else:
            return NotImplemented

    @staticmethod
    def offset_new(vec1: 'Vec2D', dx: float, dy: float) -> 'Vec2D':
        return Vec2D(vec1.x + dx, vec1.y + dy)

    @staticmethod
    def invert_new(vec1: 'Vec2D') -> 'Vec2D':
        return Vec2D(-vec1.x, -vec1.y)

    @staticmethod
    def normalize_new(vec1: 'Vec2D') -> 'Vec2D':
        length = vec1.length()
        return Vec2D(vec1.x / length, vec1.y / length)

    def offset(self, x: float, y: float) -> 'Vec2D':
        self.x += x
        self.y += y
        return self

    def invert(self, invert_x = True, invert_y = True) -> 'Vec2D':
        self.x = -self.x if invert_x else self.x
        self.y = -self.y if invert_y else self.y
        return self

    def length(self) -> float:
        return sqrt(self.x * self.x + self.y * self.y)

    def normalize(self) -> 'Vec2D':
        length = self.length()
        self.x /= length
        self.y /= length
        return self

    def __str__(self) -> str:
        return f'<{self.x},{self.y}>'


ZERO = Vec2D(0.0, 0.0)
