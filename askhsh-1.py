import node
import graph
import operator
import copy

max_weight = 10
n = 3
p = 20

nodesList: graph

# Data Structures
priority_queue = []
visited = []
results = []

node_counter = 0
done = False


#  PATH-COST Evaluation function
def path_cost():
    global priority_queue, done

    priority_queue.sort(key=operator.attrgetter('total_cost'))

    if len(priority_queue) == 0:
        print("Queue size = 0, im done")
        done = True


#  Minimum Manhattan Distance
def min_distance():
    global priority_queue, results,  done

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


def min_distance_and_path_cost():
    global priority_queue, results, done

    priority_queue.sort(key=operator.attrgetter('a_star_cost'))

    if len(priority_queue) == 0:
        done = True


def bfs(eval_function):
    global results, visited, priority_queue
    global node_counter, done

    in_visited = False

    priority_queue.append(nodesList.start_state)

    print("QUEUE:")
    for x in range(0, len(priority_queue)):
        pp: node = priority_queue[x]
        print(pp.name)

    while not done:

        ni: node = priority_queue[0]

        '''
        print("QUEUE:")
        for x in range(0, len(priority_queue)):
            pp: node = priority_queue[x]
            print(pp.name)
        '''

        for x in range(0, len(visited)):
            qi: node = visited[x]
            if ni.name == qi.name:
                in_visited = True

        if in_visited:
            print("Node " + ni.name + " already visited")
            pass
        elif ni.end_state and not in_visited:
            print("--- Node " + ni.name + " is end state, adding to results")  # Des apo to biblio thn shmeiosh
            print("Route of node is: " + ni.route)
            print("Cost of node is: " + str(ni.total_cost))
            results.append(ni)
            expansion: [] = ni.expand(ni, visited, priority_queue)
            priority_queue.extend(expansion)
            node_counter += len(expansion)
            print("Adding " + ni.name + " to visited list")
            visited.append(ni)
        else:
            print("Node " + ni.name + " is normal")
            expansion: [] = ni.expand(ni, visited, priority_queue)
            priority_queue.extend(expansion)
            node_counter += len(expansion)
            print("Adding " + ni.name + " to visited list")
            visited.append(ni)
        print("Removing from queue")
        priority_queue.remove(ni)
        eval_function()


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


# n = int(input("Enter n: "))
# p: int = int(input("Enter p: "))
# max_weight = int(input("Enter max: "))

nodesList = graph.Graph(n, p, max_weight)

'''
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
'''

print("\nStart State: " + nodesList.start_state.name)
print("End State 1: " + nodesList.end_state_1.name)
print("End State 2: " + nodesList.end_state_2.name + "\n")

bfs(min_distance_and_path_cost)
print_result()

'''
cont = True
while cont:
    print("=====|  WELCOME  |=====")
    print("1 - Uniform Cost Search")
    print("2 - Greedy Best First Search")
    print("3 - A* Search")
    print("4 - Show States")
    print("5 - Exit")
    choice = input("\nEnter choice: ")

    if choice == "1":
        reset(nodesList)
        bfs(path_cost)
        print_result()
    elif choice == "2":
        reset(nodesList)
        bfs(min_distance)
        print_result()
    elif choice == "3":
        reset(nodesList)
        bfs(min_distance_and_path_cost)
        print_result()
    elif choice == "4":
        print("\nStart State: " + start_state.name)
        print("End State 1: " + end_state_1.name)
        print("End State 2: " + end_state_2.name + "\n")
    elif choice == "5":
        cont = False
    else:
        print("\n---Invalid Input---\n")
'''
