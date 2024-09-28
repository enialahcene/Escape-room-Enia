import sys
import os
sys.path.append("/Users/carmona/Desktop/enia_ironhack/week2")
# Añadir el directorio raíz al PYTHONPATH
from parameters import object_relations, INIT_GAME_STATE
from function import start_game

game_state = INIT_GAME_STATE.copy()

def main():
    start_game(game_state)


if __name__== "__main__":
    main()