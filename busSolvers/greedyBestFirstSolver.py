from . import GreedySolver
import numpy as np


class GreedyBestFirstSolver(GreedySolver):
    def __init__(self, roads, astar, scorer):
        super().__init__(roads, astar, scorer)

    # Find the next state to develop
    def _getNextState(self, problem, currState):
        successors = list(problem.expand(currState))
        if successors:
            nextState = successors[0]
            min = self._scorer.compute(currState, nextState)
            for s in successors:
                if self._scorer.compute(currState, s) < min:
                    min =self._scorer.compute(currState, s)
                    nextState = s
        return nextState
        # TODO : Return the next state
        raise NotImplementedError

        bestIdx = None
        return successors[bestIdx]
