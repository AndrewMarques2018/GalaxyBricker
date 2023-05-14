from scripts.models.Element import Element
from scripts.utils.Vector import Vector

bolinha = Element()

bolinha.speed = Vector(10, 0)
bolinha.acceleration = Vector(-5, 0)

cont = 10
while cont > 0:
    cont -= 1
    bolinha.update_locale()

print(bolinha)

