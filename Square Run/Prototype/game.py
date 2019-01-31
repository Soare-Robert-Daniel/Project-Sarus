import sys
import pygame
from game_object import GameObject
from wall import Wall
from player import Player
from bot import Bot
from observer import Observer
import settings

pygame.init()
clock = pygame.time.Clock()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)


class Game:
    def __init__(self, width=300, height=400):
        """
        :param width: Width of the window
        :param height: Height of the window
        """
        self.win_width = width
        self.win_height = height
        self.stop = False
        self.objects = []
        self.player = None
        self.display_surf = pygame.display.set_mode((self.win_height, self.win_width),
                                                    pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.env = None

        self.round = 1
        self.sessions = 1

        self.start_game = False

    def update(self, delta_time):
        """
            Call the update for all objects
        :return:
        """
        for game_obj in self.objects:
            game_obj.update(delta_time)

        if self.player:
            self.player.update(delta_time)

    def start(self):
        while not self.stop:
            # Check the events
            for event in pygame.event.get():
                self.check_events(event)
            # Get the time between the frames
            delta_time = clock.tick(settings.FPS) / 1000
            # Update the positions if the game has started
            if self.start_game:
                self.update(delta_time)
            self.display()

            pygame.display.update()

    def display(self):
        """
            Draw all objects to the screen
        :return:
        """
        self.display_surf.fill(white)  # Make the background white

        # Draw the objects
        for game_obj in self.objects:
            game_obj.draw(self.display_surf)

        if self.player:
            self.player.draw(self.display_surf)

        # Show the Round and Session on the screen
        round_label = settings.SMALL_TEXT.render("Round %d/%d" % (self.round, settings.MAX_ROUND), 1, black)
        sessions_label = settings.SMALL_TEXT.render("Session %d" % self.sessions, 1, black)

        self.display_surf.blit(round_label, (10, 25))
        self.display_surf.blit(sessions_label, (10, 10))

        if not self.start_game:
            info_label = settings.SMALL_TEXT.render("Press 'TAB' to start", 1, red)
            self.display_surf.blit(info_label, (150, 200))

    def check_events(self, event):
        """
            Check what event is and run the corresponding's commands
        :param event:
        :return:
        """
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                self.stop = True
            elif event.key == pygame.K_SPACE:
                if self.player:
                    self.player.jump(settings.HEIGHT_JUMP_LIMIT_MAX)
            elif event.key == pygame.K_TAB:
                self.start_game = True

    def add_object(self, obj):
        """
            Add a new object to the game
        :param obj:
        :return:
        """
        self.objects.append(obj)

    def end_round(self):
        self.round += 1
        for obs in self.env.observers:
            obs.check_score()
        if self.round > settings.MAX_ROUND:
            self.end_final_round()
            self.sessions += 1
            print("+-------------------------- Start Sessions %d --------------------------------+" % self.sessions)

    def end_final_round(self):
        if self.env:
            self.env.create_new_generation()
        self.round = 1

