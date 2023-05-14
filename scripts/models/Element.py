from scripts.utils.Dimension import Dimension
from scripts.utils.Vector import Vector


class Element:
    position = Vector()
    dimension = Dimension()
    speed = Vector()
    acceleration = Vector()
    speed_max = 0
    speed_min = 0
    image = None

    def __str__(self):
        return f"Element: [ " \
               f"position={self.position} " \
               f"dimension={self.dimension} " \
               f"image={self.image} " \
               f"speed={self.speed} " \
               f"speed_max={self.speed_max} " \
               f"acceleration={self.acceleration} ]"

    def set_position(self, position: Vector):
        self.position = position

    def set_dimension(self, dimension: Vector):
        self.dimension = dimension

    def update_position(self):
        if self.acceleration != 0:
            self.speed += self.acceleration

        if self.speed != 0:
            self.position += self.speed
