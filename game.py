import pygame
import pytmx
import pyscroll
from pytmx.util_pygame import load_pygame


class Game:
    def __init__(self):
        # créer la fenêtre du jeu
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("My Game")

        # charger la carte (tmx)
        tmx_data = load_pygame("D:/projects/MyGame/carte.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())

        # dessiner le groupe de calque
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)

    def run(self):
        # boucle du jeu
        running = True

        while running:
            self.group.draw(self.screen)
            pygame.display.flip
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()
