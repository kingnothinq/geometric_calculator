from abc import ABC, abstractmethod
import math


# Abstractions
class Figure(ABC):
    __counter = 0

    @abstractmethod
    def calc_area(self) -> float:
        pass


class FlatFigure(Figure):
    def __init__(self, side_a):
        self.side_a = side_a

    @abstractmethod
    def calc_perimeter(self) -> float:
        pass


class RoundFigure(Figure):
    def __init__(self, radius):
        self.radius = radius

    @abstractmethod
    def calc_diameter(self) -> float:
        pass


class SolidFigure(Figure):

    @abstractmethod
    def calc_volume(self) -> float:
        pass


# Trilateral
class Triangle(FlatFigure):
    _name = "Triangle"

    def __init__(self, side_a, side_b, side_c):
        super().__init__(side_a)
        self.side_b = side_b
        self.side_c = side_c

    def calc_perimeter(self) -> float:
        return self.side_a + self.side_b + self.side_c

    def calc_area(self) -> float:
        p = self.calc_perimeter() / 2
        return math.sqrt(p*(p-self.side_a)*(p-self.side_b)*(p-self.side_c))

    def calc_height(self) -> float:
        return 2 * self.calc_area() / self.side_a


# Quadrilateral
class Parallelogram(FlatFigure):
    _name = "Parallelogram"

    def __init__(self, side_a, side_b, height):
        super().__init__(side_a)
        self.side_b = side_b
        self.height = height

    def calc_perimeter(self) -> float:
        return 2 * (self.side_a + self.side_b)

    def calc_area(self) -> float:
        return self.side_a * self.height

    def calc_angle(self) -> float:
        return (2 * self.height + self.side_a) / self.calc_perimeter()


class Square(Parallelogram):
    _name = "Square"

    def __init__(self, side_a):
        self.side_a = side_a
        self.side_b = side_a

    def calc_area(self) -> float:
        return self.side_a**2

    def calc_incircle_radius(self) -> float:
        return self.side_a / 2


class Rhombus(Parallelogram):
    _name = "Rhombus"

    def __init__(self, side_a, height):
        self.side_a = side_a
        self.side_b = side_a
        self.height = height

    def calc_incircle_radius(self) -> float:
        return self.calc_area() / (2 * self.side_a)


class Rectangle(Parallelogram):
    _name = "Rectangle"

    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def calc_area(self) -> float:
        return self.side_a * self.side_b

    def calc_diag_len(self) -> float:
        return math.sqrt(self.side_a**2 + self.side_b**2)


class Trapezium(Parallelogram):
    _name = "Trapezium"

    def __init__(self, side_a, side_b, side_c, side_d):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.side_d = side_d

    def calc_perimeter(self) -> float:
        return self.side_a + self.side_b + self.side_c + self.side_d

    def calc_area(self) -> float:
        return ((self.side_a + self.side_c) / 2) * \
            math.sqrt(self.side_b**2 -
                      ((self.side_c - self.side_a)**2 + self.side_b**2 - self.side_d**2) / 2 *
                      (self.side_c - self.side_a))

    def calc_height(self) -> float:
        return (2 * self.calc_area()) / (self.side_a + self.side_c)


# Round
class Circle(RoundFigure):
    _name = "Circle"

    def __init__(self, radius, angle):
        self.radius = radius
        self.angle = angle

    def calc_area(self) -> float:
        return math.pi * self.radius**2

    def calc_diameter(self) -> float:
        return 2 * self.radius

    def calc_arc_len(self):
        return (math.pi * self.radius * math.degrees(self.angle)) / math.degrees(180)


# Third-dimensional
class Pyramid(SolidFigure):
    _name = "Pyramid"

    def __init__(self, side_a, height):
        self.side_a = side_a
        self.height = height

    def calc_area(self) -> float:
        p = self.side_a / (2 * math.tan(math.radians(60)))
        return (3 * self.side_a) / 2 * (p + math.sqrt(self.height**2 + p**2))

    def calc_volume(self) -> float:
        return (self.height * self.side_a**2) / (4 * math.sqrt(3))

    def calc_insphere_radius(self) -> float:
        return (self.side_a * self.height) / (self.side_a + math.sqrt(self.side_a**2 + 12 * self.height**2))


class Cone(SolidFigure):
    _name = "Cone"

    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def calc_area(self) -> float:
        return math.pi * self.radius * (self.radius + math.sqrt(self.radius**2 + self.height**2))

    def calc_volume(self) -> float:
        return (1 / 3) * (math.pi * self.radius**2 * self.height)

    def calc_slant(self) -> float:
        return math.sqrt(self.height**2 + self.radius**2)


class Parallelepiped(SolidFigure):
    _name = "Parallelepiped"

    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def calc_area(self) -> float:
        return 2 * (self.side_a * self.side_b + self.side_b * self.side_c + self.side_a * self.side_c)

    def calc_volume(self) -> float:
        return self.side_a * self.side_b * self.side_c

    def calc_diag_len(self) -> float:
        return math.sqrt(self.side_a**2 + self.side_b**2 + self.side_c**2)


class Cube(Parallelepiped):
    _name = "Cube"

    def __init__(self, side_a):
        self.side_a = side_a
        self.side_b = side_a
        self.side_c = side_a

    def calc_diag_len(self) -> float:
        return self.side_a * math.sqrt(3)


class Sphere(SolidFigure):
    _name = "Sphere"

    def __init__(self, radius):
        self.radius = radius

    def calc_area(self) -> float:
        return 4 * math.pi * self.radius**2

    def calc_volume(self) -> float:
        return (4 / 3) * (math.pi * self.radius**3)

    def calc_diameter(self) -> float:
        return self.radius * 2


class Cylinder(SolidFigure):
    _name = "Sphere"

    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def calc_area(self) -> float:
        return 2 * math.pi * self.radius * (self.height + self.radius)

    def calc_volume(self) -> float:
        return math.pi * self.radius**2 * self.height

    def calc_side_area(self) -> float:
        return 2 * math.pi * self.radius * self.height
