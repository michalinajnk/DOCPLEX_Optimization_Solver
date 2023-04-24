import random
from docplex.mp.model import Model
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import time
def generate_randomVals(seedValue, nVal):
    random.seed(seedValue)
    nLoc = nVal
    TLoc = random.randint(-50 * nLoc, 50 * nLoc)
    SLoc = []

    for i in range(nLoc):
        SLoc.append(random.randint(-100, 100))
    return nLoc, SLoc, TLoc


def SolveSSP(seed, nValue):
    n, S, T = generate_randomVals(seed, nValue)
    # Create the CPLEX model
    model = Model('SSP')

    # Create decision variables
    x = [model.binary_var(name='x_{}'.format(i))
         for i in range(n)]

    objective_function = model.abs(T - model.sum(S[i]*x[i] for i in range(n)))
    model.minimize(objective_function)


    # Solve the model
    model.solve()
    print(model.lp_string)
    model.print_solution()
    model.print_information()

    # Print the solution
    print("Optimal Solution:")
    sum= 0
    for i in range(n):
        sum+= S[i]*x[i]
        print("x{}: {} - value of elem: {}".format(i, x[i].solution_value, S[i]))
    print("T value {0}".format(T))
    print("Sum of subset's elements {}".format(sum))

#DRAWING A CHART FOR SOLUTION REPRESENTATION
"""
    ## Create a list of colors for the bars
    colors = ['b' if x.solution_value == 1 else 'r' for x in x]
    # Create a list of colors and labels for the legend
    legend_colors = ['b', 'r']
    legend_labels = ['Selected', 'Not Selected']

    # Create a list of patch objects with the specified colors and labels
    legend_patches = [Patch(color=color, label=label) for color, label in zip(legend_colors, legend_labels)]

    # Create a bar chart with the specified colors
    plt.bar(range(n), S, color=colors)

    # Add the legend to the plot
    plt.legend(handles=legend_patches)

    # Set the x-labels
    plt.xticks(range(n), [str(i) for i in range(n)])

    # Add a title
    plt.title("Solution for SSP Problem (T={})".format(T))
    plt.xlabel('number index')
    plt.ylabel('value')
    # Display the plot
    plt.show()
"""

nVal_range = [5, 6, 7, 8, 9, 995]
num_iterations = 10
times = []

for nVal in nVal_range:
    elapsed_times = []
    for i in range(num_iterations):
        start_time = time.time()
        SolveSSP(0, nVal)
        elapsed_time = time.time() - start_time
        elapsed_times.append(elapsed_time)
    average_time = sum(elapsed_times) / num_iterations
    times.append(average_time)
    print("Average time for nVal = {}: {:.2f}s".format(nVal, average_time))

plt.plot(nVal_range, times, 'o-', label='Average time over {} iterations'.format(num_iterations))
plt.title('Solution over time for different n values')
plt.xlabel('n value')
plt.ylabel('time')
plt.legend()
plt.show()