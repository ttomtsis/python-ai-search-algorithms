"""
This file contains the best first search algorithm
along with the evaluation functions it uses, it serves
as the basis of the project's execution. It creates
a graph after taking user input and performs a series of
search algorithms.
"""

import node
import graph
import operator

max_weight: int  # Maximum Edge Cost
n: int  # Graph dimensions ( n x n )
p: int  # Percent of edges to be removed

nodesList: graph  # Graph will be stored here

# Data Structures used
priority_queue = []  # Expanded nodes stay here and await sorting
visited = []  # Visited nodes will be stored here
results = []  # Results will be stored here, we consider a valid result
# the occasion when we reach a node that is an end state. Check bfs() for more details

node_counter = 1  # Counts nodes of search tree, starts with 1 to include start-state
done = False  # Will be used to mark the end of a search process. Is manipulated by evaluation functions.

"""
Below are the 3 evaluation functions used,
the logic behind their implementation is as follows.
Priority_queue is sorted according to a criteria, eg path-cost.
Then depending on the algorithm a condition is checked to consider
if the algorithm has reached the end of the searching process or not
"""


#  PATH-COST Evaluation function
#  sorts queue according to total_cost node value
#  Must check whole graph, hence len(priority_queue) == 0
def path_cost():
    global priority_queue, done

    priority_queue.sort(key=operator.attrgetter('total_cost'))

    if len(priority_queue) == 0:
        print("Queue size = 0, im done")
        done = True


#  Minimum Manhattan Distance
#  In a similar fashion, sorts queue by manhattan value
#  Does NOT check whole graph, if it finds a path to an end node
#  AND that path exists ( hence the while loop, we iterate all the way
#  to the first parent node, if that parent is the start state, then we
# have found a valid path )
def min_distance():
    global priority_queue, results, done

    priority_queue.sort(key=operator.attrgetter('manhattan'))

    if len(results) != 0:  # Check if Path exists
        # Iterate all the way up the tree
        ni: node = results[0]
        while ni.parent is not None:
            ni = ni.parent
        if ni.name == nodesList.start_state.name:
            done = True
        else:
            results.remove(ni)


#  Minimum sum of manhattan distance and path cost
#  Sorts priority queue by aforementioned sum ( a_star_cost )
#  Checks whole graph for paths before ending
def min_distance_and_path_cost():
    global priority_queue, results, done

    priority_queue.sort(key=operator.attrgetter('a_star_cost'))

    if len(priority_queue) == 0:
        done = True


#  Best First Search function
#  Searches for a valid path to an end node, according
#  to an evaluation function. eval_function chooses
#  best path from a set of possible paths, hence the name "best-first search"
def bfs(eval_function):
    global results, visited, priority_queue
    global node_counter, done

    # Start by adding start state to the queue
    priority_queue.append(nodesList.start_state)

    # Loop until eval_function decides to end
    while not done:

        # Choose first node of priority queue, since queue is sorted
        ni: node = priority_queue[0]

        # Check if node is visited
        in_visited = False
        for x in range(0, len(visited)):
            qi: node = visited[x]
            if ni.name == qi.name:
                in_visited = True

        # If visited, pass
        if in_visited:
            print("Node " + ni.name + " already visited")
            pass

        # If node is an end state, add to results and expand
        elif ni.end_state and not in_visited:
            print("--- Node " + ni.name + " is end state, adding to results")  # Des apo to biblio thn shmeiosh
            print("Route of node is: " + ni.route)
            print("Cost of node is: " + str(ni.total_cost))
            results.append(ni)

            # After expanding, the results are stored in the expansion lists
            expansion: [] = ni.expand(ni, visited, priority_queue)

            # Add results to queue
            priority_queue.extend(expansion)

            # Increment Counter
            node_counter += len(expansion)
            print("Adding " + ni.name + " to visited list")

            # Add expanded node to visited list
            visited.append(ni)

        # If node is not an end state, simply expand
        # Logic followed is similar to above case
        else:
            print("Node " + ni.name + " is normal CASE")
            expansion: [] = ni.expand(ni, visited, priority_queue)
            priority_queue.extend(expansion)
            node_counter += len(expansion)
            print("Adding " + ni.name + " to visited list")
            visited.append(ni)

        # Remove expanded node from priority queue
        print("Removing from queue")
        priority_queue.remove(ni)

        # Choose next node and decide if search is done
        eval_function()


#  Prints Best Result
def print_result():
    global results

    if len(results) == 0:
        print("Search cannot reach end state")
    else:
        results.sort(key=operator.attrgetter('total_cost'))
        # print("Results are: ")
        # print_graph(results)
        nu: node = results[0]
        print("\nBest result is: " + nu.name)
        nu.print()
        print("Total nodes created: " + str(node_counter))
        print("\n")


#  Ask user for parameters
print("Enter Graph Parameters")

cont = True
while cont:
    n = int(input("Enter n: "))
    p: int = int(input("Enter p: "))
    max_weight = int(input("Enter max: "))
    if n <= 0:
        print("n must be > 0")
    if p < 0:
        print("p must be >= 0")
    if max_weight <= 0:
        print("max must be > 0")
    if n > 0 and p >= 0 and max_weight > 0:
        cont = False

# Create graph
nodesList = graph.Graph(n, p, max_weight)

print("\nStart State: " + nodesList.start_state.name)
print("End State 1: " + nodesList.end_state_1.name)
print("End State 2: " + nodesList.end_state_2.name + "\n")

# Basic Menu
cont = True
while cont:
    print("=====|  WELCOME  |=====")
    print("1 - Uniform Cost Search")
    print("2 - Greedy Best First Search")
    print("3 - A* Search")
    print("4 - Print Graph")
    print("5 - Show States")
    print("6 - Exit")
    choice = input("\nEnter choice: ")

    if choice == "1":
        nodesList.reset(nodesList)
        bfs(path_cost)
        print_result()
    elif choice == "2":
        nodesList.reset(nodesList)
        bfs(min_distance)
        print_result()
    elif choice == "3":
        nodesList.reset(nodesList)
        bfs(min_distance_and_path_cost)
        print_result()
    elif choice == "4":
        nodesList.print_graph()
    elif choice == "5":
        print("\nStart State: " + nodesList.start_state.name)
        print("End State 1: " + nodesList.end_state_1.name)
        print("End State 2: " + nodesList.end_state_2.name + "\n")
    elif choice == "6":
        cont = False
    else:
        print("\n---Invalid Input---\n")
