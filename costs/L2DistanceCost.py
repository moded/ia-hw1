from . import Cost
import ways.tools


class L2DistanceCost(Cost):
    roads = None

    def __init__(self, roads):
        self.roads = roads

    # Returns the L2 aerial distance between two states
    def compute(self, fromState, toState):
        coord1 = self.roads[fromState.junctionIdx].coordinates
        coord2 = self.roads[toState.junctionIdx].coordinates
        return  ways.tools.compute_distance(coord1, coord2)
        # TODO : Return the correct value (call the suitable function from ways.tools)
        # raise NotImplementedError
