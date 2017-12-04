from heuristics import Heuristic
import numpy as np
import ways.tools


# TODO : Implement as explained in the instructions
class TSPCustomHeuristic(Heuristic):
    _distMat = None
    _junctionToMatIdx = None

    # TODO : You can add parameters if you need them
    def __init__(self, roads, initialState):
        self._roads = roads
        super().__init__()

    # Estimate heuristically the minimal cost from the given state to the problem's goal
    def estimate(self, problem, state):
        waitingsVector = list()  # np.array(self._junctionToMatIdx)
        for sOrigin, sTarget in state.waitingOrders:
            coord1 = self._roads[sOrigin].coordinates
            coord2 = self._roads[sTarget].coordinates
            waitingsVector.append(ways.tools.compute_distance(coord1, coord2))
        if waitingsVector:
            # print(waitingsVector)
           return max(waitingsVector)
        else:
           # print("Went through return 0")
            return 0

# raise NotImplementedError
