import pygame
from GameSettings import GameSettings

class Animation:

    def __init__(self, frames_list, fps, cyclic):
        self.frames = []
        self.length = 0
        self.current_index = 0
        self.gameframe = 0
        self.fps = fps
        self.cyclic = cyclic
        self.ended = False

        for frame in frames_list:
            new_frame = pygame.image.load(frame)
            self.frames.append(new_frame)
            self.length += 1

    def get_frame(self):
        assert len(self.frames) > 0

        if self.ended == True or self.length == 1:
            return self.frames[self.length - 1]

        self.gameframe += 1
        if self.gameframe >= GameSettings.FPS:
            self.gameframe = 0

        self.current_index = int(self.gameframe/self.fps)%self.length
        frame = self.frames[self.current_index]

        if self.current_index >= self.length and self.cyclic == False:
            self.ended = True

        return frame
