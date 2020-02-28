#!/usr/bin/env python3

import abc

class CalculatePosition(abc.ABC):
    @abc.abstractmethod
    def calculateXPosition(self):
        pass

    @abc.abstractmethod
    def calculateYPosition(self):
        pass

