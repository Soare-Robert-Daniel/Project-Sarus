import sys
import pygame
from game import Game
from observer import Observer
from environment import Environment
import settings
from genetic.population import Population
from objects.player import Player
from objects.wall import Wall
from objects.bot import Bot


pygame.init()
clock = pygame.time.Clock()

black = (0, 0, 0)
white = (255, 255, 255)


def create_ai(population, target):
    """

    :param population: the population which the individuals will be assigned to the bots
    :param target: the obstacle which the bots must pass
    :return: two list, first with hte bots and the second with their observers
    """
    ai_list = []
    observers = []
    for index, indv in enumerate(population.get_pool()):
        new_ai = Bot(settings.AI_SKINS[0], indv.threshold, 200, 50 + index * 30, 290, "Ai %d" % index)
        new_obs = Observer(new_ai, [target])

        new_obs.ai = indv
        new_ai.set_target(target)
        new_ai.obs = new_obs

        observers.append(new_obs)
        ai_list.append(new_ai)

    return [ai_list, observers]


def enable_bot_and_player(_game):
    player = Player(settings.PLAYER_SKINS[0], 175, 100, 290, "Player")
    bot = Bot(settings.BOT_SKINS[0], 75, 200, 300, 290, "Bot")
    obs_player = Observer(player, [wall])
    obs_bot = Observer(bot, [wall])

    player.obs = obs_player
    bot.set_target(wall)
    bot.obs = obs_bot

    _game.player = player
    _game.add_object(bot)


if __name__ == "__main__":

    pygame.display.set_caption("Smart Square")
    game = Game(400, 500)

    wall = Wall(settings.SKINS[0], -100, 500, 250, "Wall")
    wall.game = game
    game.add_object(wall)

    # ------------------------------------------------------------
    env = Environment()
    env.population = Population(10, 0.2)
    ai_list, env.observers = create_ai(env.population, target=wall)
    game.objects.extend(ai_list)
    game.env = env
    # ------------------------------------------------------------

    game.start()
