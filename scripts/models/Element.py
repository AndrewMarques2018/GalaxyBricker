from scripts.utils.Vector import Vector
from scripts.utils.Dimension import Dimension


class Element:
    speed_max = 0
    speed_min = 0
    speed = Vector()
    acceleration = Vector()

    def __init__(self, position=Vector(0, 0), dimension=Dimension(0, 0), image=None):
        self.position = position
        self.dimension = dimension
        self.image = image

    def __str__(self):
        return f"Element: [ " \
               f"position={self.position} " \
               f"dimension={self.dimension} " \
               f"image={self.image} " \
               f"speed={self.speed} " \
               f"speed_max={self.speed_max} " \
               f"acceleration={self.acceleration} ]"

    def update_locale(self):
        if self.acceleration != 0:
            self.speed += self.acceleration

        if self.speed != 0:
            self.position += self.speed
