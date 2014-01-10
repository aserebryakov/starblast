import pygame

class Animation:

    def __init__(self, frames_list):
        self.frames = []
        self.length = 0
        self.current_index = 0
        for frame in frames_list:
            new_frame = pygame.image.load(frame)
            self.frames.append(new_frame)
            self.length += 1

    def get_frame(self):
        assert len(self.frames) > 0

        frame = self.frames[self.current_index]
        self.current_index += 1

        if self.current_index >= self.length:
            self.current_index = 0

        return frame
