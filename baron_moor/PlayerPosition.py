#!/usr/bin/env python3

import random
from GameBoard import *
from CalculatePosition import *

class PlayerPosition():

    x = 0
    y = 0

    gb = GameBoard()

    def getColumns(self):
        return GameBoard.columns

    def getRows(self):
        return GameBoard.rows

    def calculateXPosition(self):
        x = random.randint(0,self.gb.getRows())
        return x

    def calculateYPosition(self):
        y = random.randint(0,self.gb.getColumns())
        return y


