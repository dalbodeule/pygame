import pygame

class Player:
    def __init__(self, x, y):
        self.__image = pygame.image.load('Resources/player.png')
        self.__image = pygame.transform.scale(self.__image, (128, 128))
        self.__pos = [x, y]
        self.__to = [0, 0]
        self.__angle = 0

    def get_pos(self):
        return self.__pos

    def draw(self, screen):

        if self.__to == [-1, -1]: self.__angle = 45
        elif self.__to == [-1, 0]: self.__angle = 90
        elif self.__to == [-1, 1]: self.__angle = 135
        elif self.__to == [0, 1]: self.__angle = 180
        elif self.__to == [1, 1]: self.__angle = -135
        elif self.__to == [1, 0]: self.__angle = -90
        elif self.__to == [1, -1]: self.__angle = -45
        elif self.__to == [0, -1]: self.__angle = 0


        rotated = pygame.transform.rotate(self.__image, self.__angle)

        calib_pos = [0, 0]
        calib_pos[0] = self.__pos[0] - rotated.get_width()/2
        calib_pos[1] = self.__pos[1] - rotated.get_height()/2

        screen.blit(rotated, calib_pos)

    def goto(self, x, y):
        self.__to[0] += x
        self.__to[1] += y

    def update(self, dt, screen):
        width, height = screen.get_size()
        self.__pos[0] = self.__pos[0] + dt*self.__to[0] * 0.7
        self.__pos[1] = self.__pos[1] + dt*self.__to[1] * 0.7

        self.__pos[0] = min(max(self.__pos[0], 32), width-32)
        self.__pos[1] = min(max(self.__pos[1], 32), height-32)

    def is_out_of_screen(self, screen):
        width, height = screen.get_size()

        return bool(self.__pos[0] < 32 or self.__pos[0] > width - 32 or self.__pos[1] < 32 or self.__pos[1] > height - 32)
