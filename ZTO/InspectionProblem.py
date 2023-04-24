import random
from docplex.mp.model import Model
import matplotlib.pyplot as plt
import time


def generate_randomVals(seedValue, nVal):
    random.seed(seedValue)
    n = nVal
    circlesLoc = []
    # For loop to calculate ai, bi, and ri
    for i in range(1, n + 1):
        ai = random.uniform(5, 35)
        bi = random.uniform(5, 35)
        ri = random.uniform(1, 4)
        circlesLoc.append((ai, bi, ri))
    # Initialize x0 and y0
    x0Loc = random.uniform(5, 35)
    y0Loc = random.uniform(5, 35)

    return n, circlesLoc, (x0Loc, y0Loc)


def solveInspectionProblemWithoutVisualisation(seedVal, nVal):
    n, circles, (x0, y0) = generate_randomVals(seedVal, nVal)
    # Create the CPLEX model
    model = Model('Inspection_Problem')

    # Create decision variables
    x = [model.continuous_var(lb=circles[i][0]-circles[i][2], ub=circles[i][0]+circles[i][2], name='x_{}'.format(i))
         for i in range(n)]
    y = [model.continuous_var(lb=circles[i][1]-circles[i][2], ub=circles[i][1]+circles[i][2],  name='y_{}'.format(i))
         for i in range(n)]

    # Add constraint
    # The point (xi, yi) must be inside (or on the edge of) the i-th circle
    for i in range(n):
        model.add_constraint((x[i]-circles[i][0]) ** 2 + (y[i] - circles[i][1]) ** 2 <= circles[i][2] ** 2)

    # Add objective
    # The total length of the path from 0 → 1 → 2 → ... n → n → 0 must be minimized
     #manhattan distance
    model.minimize(model.sum(
       model.abs(x[i - 1] - x[i]) + model.abs(y[i - 1] - y[i]) for i in range(n))
    + model.abs(x[0] - x0) + model.abs(y[0] - y0)
    + model.abs(x[n - 1] - x0) + model.abs(y[n - 1] - y0))


    # Solve the model
    model.solve()
    print(model.lp_string)
    model.print_solution()
    model.print_information()

def solveInspectionProblem(seedVal, nVal):
    n, circles, (x0, y0) = generate_randomVals(seedVal, nVal)
    # Create the CPLEX model
    model = Model('Inspection_Problem')

    # Create decision variables
    x = [model.continuous_var(lb=circles[i][0]-circles[i][2], ub=circles[i][0]+circles[i][2], name='x_{}'.format(i))
         for i in range(n)]
    y = [model.continuous_var(lb=circles[i][1]-circles[i][2], ub=circles[i][1]+circles[i][2],  name='y_{}'.format(i))
         for i in range(n)]

    # Add constraint
    # The point (xi, yi) must be inside (or on the edge of) the i-th circle
    for i in range(n):
        model.add_constraint((x[i]-circles[i][0]) ** 2 + (y[i] - circles[i][1]) ** 2 <= circles[i][2] ** 2)

    # Add objective
    # The total length of the path from 0 → 1 → 2 → ... n → n → 0 must be minimized
     #manhattan distance
    model.minimize(model.sum(
       model.abs(x[i - 1] - x[i]) + model.abs(y[i - 1] - y[i]) for i in range(n))
    + model.abs(x[0] - x0) + model.abs(y[0] - y0)
    + model.abs(x[n - 1] - x0) + model.abs(y[n - 1] - y0))


    # Solve the model
    model.solve()
    print(model.lp_string)
    model.print_solution()
    model.print_information()

    # Print the solution
    print("Optimal Solution:")
    for i in range(n):
        print("x{}: {}".format(i, x[i].solution_value))
        print("y{}: {}".format(i, y[i].solution_value))


"""
    # Plot the circles
    fig, ax = plt.subplots()
    for i in range(n):
        circle = plt.Circle((circles[i][0], circles[i][1]), circles[i][2], fill=False)
        ax.add_artist(circle)

    # add points to the plot
    ax.scatter(x, y, color='red', marker='o')

    # Plot the path
    x_values = [x0]
    y_values = [y0]
    x_values += [x[i].solution_value for i in range(n)]
    y_values += [y[i].solution_value for i in range(n)]
    for i, (x, y) in enumerate(zip(x_values, y_values)):
        plt.text(x, y, i, fontsize=10)

    x_values.append(x0)
    y_values.append(y0)

    plt.plot(x_values, y_values, 'r-')

    # Plot the starting and ending points
    plt.plot(x0, y0, 'go')
    plt.plot(x_values[n], y_values[n], 'yo')

    # Set the x and y limits of the plot
    min_x = min([circles[i][0] - circles[i][2] for i in range(n)])
    max_x = max([circles[i][0] + circles[i][2] for i in range(n)])
    min_y = min([circles[i][1] - circles[i][2] for i in range(n)])
    max_y = max([circles[i][1] + circles[i][2] for i in range(n)])

    ax.set_xlim(min_x - 5, max_x + 5)
    ax.set_ylim(min_y - 5, max_y + 5)
    plt.show()



# Define the range of nVal values
nVal_range = [5,6,7,8,9,10]

times =[]
# Iterate over the nVal values and plot the solution over time
for nVal in nVal_range:
    start_time = time.time()

    # Solve the problem
    solveInspectionProblem(seedVal=10, nVal=nVal)

    # Calculate the elapsed time
    elapsed_time = time.time() - start_time
    times.append(elapsed_time)

plt.plot(nVal_range, times, 'o-', label='n={}, time={:.2f}s'.format(nVal, elapsed_time))

# Add labels and legend
plt.title('Solution over time for different n values')
plt.xlabel('n value')
plt.ylabel('time')
plt.legend()

# Show the plot
plt.show()
"""

# TAKING AVARAGE FOR MULTIPLE ITERATIONS

nVal_range = [5, 10, 15, 20, 25]
num_iterations = 10
times = []

for nVal in nVal_range:
    elapsed_times = []
    for i in range(num_iterations):
        start_time = time.time()
        solveInspectionProblem(0, nVal)
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
