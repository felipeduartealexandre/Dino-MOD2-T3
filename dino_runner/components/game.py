import pygame

 

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE

from dino_runner.components.dinosaur import Dinosaur

from dino_runner.components.obstacles.obstacle_manager import ObstacleManager

from dino_runner.utils.text_utils import draw_message_component

from dino_runner.components.powerups.power_up_manager import PowerUpManager

class Game:
    def _init_(self):
        pygame.init()
        pygame.display.set_caption()