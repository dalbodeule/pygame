import pygame

class Bullet:
    def __init__(self, x, y, toX, toY):
        self.__pos = [x, y]
        self.__to = [toX, toY]
        self.__radius = 7
        self.__color = (190, 0, 0)

    def get_pos(self):
        return self.__pos

    def update_and_draw(self, dt, screen):
        width, height = screen.get_size()
        self.__pos[0] = (self.__pos[0] + dt*self.__to[0]) % width
        self.__pos[1] = (self.__pos[1] + dt*self.__to[1]) % height

        pos_int = (int(self.__pos[0]), int(self.__pos[1]))

        pygame.draw.circle(screen, self.__color, pos_int, self.__radius)
