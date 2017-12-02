from . import GreedySolver
import numpy as np

class GreedyStochasticSolver(GreedySolver):
    _TEMPERATURE_DECAY_FACTOR = None
    _INITIAL_TEMPERATURE = None
    _N = None

    def __init__(self, roads, astar, scorer, initialTemperature, temperatureDecayFactor, topNumToConsider):
        super().__init__(roads, astar, scorer)

        self._INITIAL_TEMPERATURE = initialTemperature
        self._TEMPERATURE_DECAY_FACTOR = temperatureDecayFactor
        self._N = topNumToConsider

    def _getSuccessorsProbabilities(self, currState, successors):
        # Get the scores
        X = np.array([self._scorer.compute(currState, target) for target in successors])
        alpha = X.min()
        # Initialize an all-zeros vector for the distribution
        P = np.zeros((len(successors),))
        # Preduced = []
        Xcopy = X.copy()
        NIdxs = []
        numOfPoints = self._N if successors.__len__() >= 5 else successors.__len__()
        for i in range(numOfPoints):
            minIdx = Xcopy.argmin(0)
            NIdxs.append(minIdx)
            Xcopy[minIdx] = Xcopy.max() + 1.0
            # Xcopy = np.delete(Xcopy, maxIdx)
        P_N_sum_prob = 0.0
        for i in NIdxs:
            P_N_sum_prob += (X[i]/alpha)**(-1/self.T)
        for i in NIdxs:
            P[i] = ((X[i]/alpha)**(-1/self.T))/P_N_sum_prob
            # Preduced.append(P[i])
        # print(X,P,NIdxs)
        # TODO: Fill the distribution in P as explained in the instructions.
        # TODO : No changes in the rest of the code are needed
        # raise NotImplementedError
        Psum = np.sum(P)
        # Update the temperature
        # self.T *= self._TEMPERATURE_DECAY_FACTOR

        return P

    # Find the next state to develop
    def _getNextState(self, problem, currState):
        successors = list(problem.expand(currState))
        P = self._getSuccessorsProbabilities(currState, successors)
        # np.random.choice(successors,1,False,P)
        Psum = np.sum(P)
        # TODO : Choose the next state stochastically according to the calculated distribution.
        # You should look for a suitable function in numpy.random.
        nextIdx = np.random.choice(successors,1,False,P)

        return nextIdx[0]

    # Override the base solve method to initialize the temperature
    def solve(self, initialState):
        self.T = self._INITIAL_TEMPERATURE
        return super().solve(initialState)