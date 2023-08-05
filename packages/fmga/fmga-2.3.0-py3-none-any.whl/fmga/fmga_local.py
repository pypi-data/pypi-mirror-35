## testing the global package
import fmga

## testing the local package
from function_maximize import maximize

import math

def res():
    best_point = maximize(f, dimensions=3, mutation_probability=0.1, population_size=100, multiprocessing=True,
                          iterations=5)
    return best_point

if __name__ == '__main__':

    def f(*args):
        sum = args[0] - args[1] + args[2]
        for _ in range(10000):
            sum += _
        return sum

    best_point = res()
    print(best_point.coordinates, best_point.fitness)

