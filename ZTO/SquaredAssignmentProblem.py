import random
from docplex.mp.model import Model
import matplotlib.pyplot as plt
import time

def generate_randomVals(seedValue, nVal):
    random.seed(seedValue)
    n = nVal
    circlesLoc = []
    flow_matrix = {}
    # For loop to calculate ai, bi, and ri
    for i in range(n):
        ai = random.uniform(5, 35)
        bi = random.uniform(5, 35)
        ri = random.uniform(1, 7)
        circlesLoc.append((ai, bi, ri))
        for j in range(n):
            flow_matrix[i, j] = random.uniform(1, 20)
    return n, circlesLoc, flow_matrix


def solveSquaredAssignmentProblem(seed, nValue):
    n, circles, flow_matrix = generate_randomVals(seed, nValue)
    # Create the CPLEX model
    model = Model('SquaredAssignmentProblem')

    # Create decision variables
    x = [model.continuous_var(lb=circles[i][0]-circles[i][2], ub=circles[i][0]+circles[i][2], name='x_{}'.format(i))
         for i in range(n)]
    y = [model.continuous_var(lb=circles[i][1]-circles[i][2], ub=circles[i][1]+circles[i][2],  name='y_{}'.format(i))
         for i in range(n)]

    #manhattan distance
    distance_matrix = {}
    for i in range(n):
        for j in range(n):
            distance_matrix[i, j] = model.abs(x[j] - x[i]) + model.abs(y[j] - y[i])


    # Add constraint
    # The point (xi, yi) must be inside (or on the edge of) the i-th circle
    for i in range(n):
        model.add_constraint((x[i]-circles[i][0]) ** 2 + (y[i] - circles[i][1]) ** 2 <= circles[i][2] ** 2)

    model.minimize(model.sum(distance_matrix[i, j]*flow_matrix[i, j] for i in range(n) for j in range(n)))


    # Solve the model
    model.solve()
    print(model.lp_string)
    model.print_solution()
    model.print_information()

    # Print the solution
    print("Optimal Solution:")
    for i in range(n):
        print("x{},y{}: ({},{})".format(i, i, x[i].solution_value, y[i].solution_value))


    # Get the solution values
    x_values = [x[i].solution_value for i in range(n)]
    y_values = [y[i].solution_value for i in range(n)]



    # Create plot
    fig, ax = plt.subplots(figsize=(8, 8))

    # Plot circles
    for i in range(n):
        circle = plt.Circle((circles[i][0], circles[i][1]), circles[i][2], color='blue', fill=False)
        ax.add_artist(circle)
        ax.text(circles[i][0], circles[i][1], f"C{i}", ha='center', va='center', fontsize=12)

    arrows = []
    legend_labels = []
    for i in range(n):
        for j in range(n):
            if i != j and flow_matrix[i, j] > 0:
                x1, y1 = x_values[i], y_values[i]
                x2, y2 = x_values[j], y_values[j]
                flow_value = flow_matrix[i, j]
                arrow = ax.arrow(x1, y1, x2-x1, y2-y1, length_includes_head=True, head_width=0.3, head_length=0.5,
                                 color='green', linewidth=0.5, alpha=0.8 if flow_value > 10 else 0.3, linestyle='--')
                arrows.append(arrow)
                legend_labels.append(f'C{i} -> C{j}: {flow_value:.2f}')

    # Add legend
    legend = ax.legend(handles=arrows, labels=legend_labels, bbox_to_anchor=(1.05, 1), loc='upper left', title='Flow Values')
    # add points to the plot
    ax.scatter(x, y, color='red', marker='o')

    # Set plot limits
    plt.xlim(min([c[0]-c[2] for c in circles])-1, max([c[0]+c[2] for c in circles])+1)
    plt.ylim(min([c[1]-c[2] for c in circles])-1, max([c[1]+c[2] for c in circles])+1)

    # Add title and axis labels
    ax.set_title("Squared Assignment Problem")
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    # Adjust plot layout
    plt.subplots_adjust(right=0.7)
    plt.show()


# Define the range of nVal values
nVal_range = [5, 6, 7, 8, 9, 10]

times =[]
# Iterate over the nVal values and plot the solution over time
for nVal in nVal_range:
    start_time = time.time()

    # Solve the problem
    solveSquaredAssignmentProblem(0, nVal)

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
nVal_range = [5, 6, 7, 8, 9, 10]
num_iterations = 10
times = []

for nVal in nVal_range:
    elapsed_times = []
    for i in range(num_iterations):
        start_time = time.time()
         solveSquaredAssignmentProblem(0, nVal)
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
"""