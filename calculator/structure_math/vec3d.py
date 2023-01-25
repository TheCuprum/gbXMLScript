from math import sqrt


class Vec3D():
    def __init__(self, x: float, y: float, z: float) -> None:
        self.x: float = x
        self.y: float = y
        self.z: float = z

    def __neg__(self):
        return self.invert()

    def __add__(self, other) -> 'Vec3D':
        if not isinstance(other, Vec3D):
            return NotImplemented
        return Vec3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __iadd__(self, other):
        if not isinstance(other, Vec3D):
            return NotImplemented
        return self.offset(other.x, other.y, other.z)

    def __sub__(self, other) -> 'Vec3D':
        if not isinstance(other, Vec3D):
            return NotImplemented
        return Vec3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __isub__(self, other):
        if not isinstance(other, Vec3D):
            return NotImplemented
        return self.offset(-other.x, -other.y, -other.z)

    def __mul__(self, other) -> float:
        if not isinstance(other, Vec3D):
            return NotImplemented
        return self.x * other.x + self.y * other.y + self.z * other.z

    def __rmul__(self, other) -> 'Vec3D':
        if isinstance(other, (float, int)):
            return Vec3D(self.x * other, self.y * other, self.z * other)
        return NotImplemented

    @staticmethod
    def offset_new(vec1: 'Vec3D', dx: float, dy: float, dz: float) -> 'Vec3D':
        return Vec3D(vec1.x + dx, vec1.y + dy, vec1.z + dz)

    @staticmethod
    def invert_new(vec1: 'Vec3D') -> 'Vec3D':
        return Vec3D(-vec1.x, -vec1.y, -vec1.z)

    @staticmethod
    def normalize_new(vec1: 'Vec3D') -> 'Vec3D':
        length = vec1.length()
        return Vec3D(vec1.x / length, vec1.y / length, vec1.z / length)

    def offset(self, x: float, y: float, z: float) -> 'Vec3D':
        self.x += x
        self.y += y
        self.z += z
        return self

    def invert(self, invert_x = True, invert_y = True, invert_z = True) -> 'Vec3D':
        self.x = -self.x if invert_x else self.x
        self.y = -self.y if invert_y else self.y
        self.z = -self.z if invert_z else self.z
        return self

    def length(self) -> float:
        return sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def normalize(self) -> 'Vec3D':
        length = self.length()
        self.x /= length
        self.y /= length
        self.z /= length
        return self

    def __str__(self) -> str:
        return f'<{self.x},{self.y},{self.z}>'


ZERO = Vec3D(0.0, 0.0, 0.0)
