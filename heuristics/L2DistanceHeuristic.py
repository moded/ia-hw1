from . import Heuristic
import ways.tools
import problems

# Use the L2 aerial distance (in meters)
class L2DistanceHeuristic(Heuristic):
    def estimate(self, problem, state):
        # TODO : Return the correct distance
        # raise NotImplementedError
        coord1 = state.coordinates
        coord2 = problem.target.coordinates
        #coord1 = problems.MapProblem._roads[problems.MapProblem.target]
        #coord2 = problems.MapProblem._roads[state.junctionIdx]
        return ways.tools.compute_distance(coord1, coord2)
