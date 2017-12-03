from consts import Consts
from astar import AStar
from ways import load_map_from_csv
from busSolvers import GreedyBestFirstSolver, GreedyStochasticSolver
from problems import BusProblem
from costs import L2DistanceCost
from heuristics import L2DistanceHeuristic
import numpy as np
import scipy.stats as stt

REPEATS = 150

# Load the files
roads = load_map_from_csv(Consts.getDataFilePath("israel.csv"))
prob = BusProblem.load(Consts.getDataFilePath("HAIFA_100.in"))

mapAstar = AStar(L2DistanceHeuristic(), shouldCache=True)

scorer = L2DistanceCost(roads)

# Run the greedy solver
pickingPath = GreedyBestFirstSolver(roads, mapAstar, scorer).solve(prob)
greedyDistance = pickingPath.getDistance() / 1000
print("Greedy solution: {:.2f}km".format(greedyDistance))

# Run the stochastic solver #REPATS times
solver = GreedyStochasticSolver(roads, mapAstar, scorer,
                                Consts.STOCH_INITIAL_TEMPERATURE,
                                Consts.STOCH_TEMPERATURE_DECAY_FUNCTION,
                                Consts.STOCH_TOP_SCORES_TO_CONSIDER)
results = np.zeros((REPEATS,))
print("Stochastic repeats:")
for i in range(REPEATS):
    print("{}..".format(i+1), end=" ", flush=True)
    results[i] = solver.solve(prob).getDistance() / 1000

print("\nDone!")

# TODO : Part1 - Plot the diagram required in the instructions
from matplotlib import pyplot as plt
# raise NotImplementedError
greedyDistanceVec = []
resultsMonotonized = [results[0]]
for i in range(REPEATS):
    greedyDistanceVec.append(greedyDistance)
    if i == 0: continue
    if results[i] <= resultsMonotonized[i-1]:
        resultsMonotonized.append(results[i])
    else:
        resultsMonotonized.append(resultsMonotonized[i-1])
stochast, = plt.plot(resultsMonotonized,label='Greedy Stochastic Solver')
determ, = plt.plot(greedyDistanceVec,label='Greedy Deterministic solver')
plt.title("Quality of solution as a function of number of repetitions")
plt.legend(handles = [stochast,determ])
plt.show()

# TODO : Part2 - Remove the exit and perform the t-test
E = sum(resultsMonotonized) / resultsMonotonized.__len__()
std = np.sqrt(((resultsMonotonized[i] + E)**2)/resultsMonotonized.__len__())

mean = np.mean(resultsMonotonized)
stddev = np.std(resultsMonotonized)
print('calculated E = {}, stddev = {}'.format(E,std))
print('stock func mean = {}, stddev = {}'.format(E,std))
# assert mean == E
# assert std == stddev
p_val = stt.ttest_1samp(mean,greedyDistance)
print('P-value is: {}'.format(p_val))