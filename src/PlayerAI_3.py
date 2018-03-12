from BaseAI_3 import BaseAI
from Grid_3       import Grid
from ComputerAI_3 import ComputerAI
from Displayer_3  import Displayer
from random       import randint
import time

class PlayerAI(BaseAI):

    def getMove(self, grid):

        moves = grid.getAvailableMoves()
        return moves[randint(0, len(moves) - 1)] if moves else None
