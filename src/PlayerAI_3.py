from BaseAI_3 import BaseAI
from Grid_3       import Grid
from ComputerAI_3 import ComputerAI
from Displayer_3  import Displayer
from random       import randint
import time

class PlayerAI(BaseAI):

    def getMove(self, grid):

        moves = grid.getAvailableMoves()
        self.generateMoves(grid)
        testGrid = grid
        compMoves = self.generateComputerMoves(testGrid)
        return moves[randint(0, len(moves) - 1)] if moves else None


    def generateMoves(self,grid):
        result = []
        moves = grid.getAvailableMoves()
        for m in moves:
            newGrid = grid
            newGrid.move(m)
            result.append(newGrid)
        return result

    def generateComputerMoves(self,grid):
        result = []
        moves = grid.getAvailableCells()
        for m in moves:
            newGrid1 = grid
            newGrid2 = grid
            newGrid1.insertTile(m, 2)
            newGrid2.insertTile(m, 4)
            result.append(newGrid1)
            result.append(newGrid2)

        print("computer's moves available:", len(result))
        return result
