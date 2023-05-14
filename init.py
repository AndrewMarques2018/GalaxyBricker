from scripts.GameEngine import GameEngine
from scripts.utils.Dimension import Dimension


def init():
    dimension = Dimension(700, 780)
    game_engine = GameEngine("Galaxy Bricker", False, dimension)
    game_engine.dimensionGeometry()
    game_engine.createWindow()


init()
