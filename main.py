import pickle
from os import mkdir, listdir
from os.path import isdir
from threading import Thread
from time import sleep, time
from typing import Optional

from map import Map
from player import Player

FLAGS = 0
DATA = None


class Data:
    player: Player
    map: Map

    def __init__(self, player: Player, map: Optional[Map] = None):
        self.player = player
        self.map = map or Map()


class Flags:
    kill = 1


def run_loop():
    while not FLAGS & Flags.kill:
        s = time()
        for tile in DATA.map.tiles:
            if tile.station:
                pass
        s = 1/20 - (time() - s)
        if s > 0:
            sleep(s)


def get_imput(command_list):
    for i, c in enumerate(command_list):
        print(f'{i + 1})', c)
    i = input('\nWhich option would you like [#]? ')
    while not i.isdigit() or not (0 < int(i) <= len(command_list)):
        i = input(f'{"That was not a number. Please type in a number." if not i.isdigit() else "Please type in a valid option."}\nWhich command would you like [#]? ')
    return command_list[int(i) - 1]


def cli_menu():
    global FLAGS, DATA
    command_list = ['New Game', 'Load Game', 'Exit']
    if not isdir('saves'):
        command_list.remove('Load Game')
    while not FLAGS & Flags.kill:
        c = get_imput(command_list)
        if c == 'Exit':
            FLAGS |= Flags.kill
        elif c == 'New Game':
            name = input('What is the name of your player? ').strip()
            while not name:
                name = input('That was empty.\nWhat is the name of your player? ').strip()
            DATA = Data(Player(name))
            game()
        elif c == 'Load Game':
            saves = [s.rsplit('.', 1)[0] for s in listdir('saves') if s.endswith('.dat')]
            s = get_imput(saves)
            with open(f'saves/{s}.dat', 'r') as s:
                DATA = pickle.load(s)
            game()
        print()


def game():
    Thread(target=run_loop, daemon=True).start()
    commands = ['View Map', 'View Inventory', 'Move Character', 'Inspect Tile', 'Save', 'Quit']
    while not FLAGS & Flags.kill:
        c = get_imput(commands)
        if c == 'Save':
            if not isdir('saves'):
                mkdir('saves')
            with open(f'saves/{DATA.player.username}.dat', 'rb') as s:
                pickle.dump(s, DATA)


if __name__ == '__main__':
    try:
        cli_menu()
    except KeyboardInterrupt:
        FLAGS &= Flags.kill
