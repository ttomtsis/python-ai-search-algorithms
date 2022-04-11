import operator
import node
import random
import copy

max_weight = 10
n = 3
p = 20

start_state = -1
end_state_1 = -1
end_state_2 = -1

node_counter = 0


def rand_weight():
    return int(random.randrange(1, max_weight))


def create_graph(n):
    print("Creating Graph")
    print("Size will be: " + str(n) + " X " + str(n))
    counter = 1
    nodes = []

    # Dhmiourgia antikeimenon
    # topothetisi se "pinaka"
    for x in range(0, n):
        cols = []
        for y in range(0, n):
            cols.append(node.MyNode(str(counter)))
            counter += 1
        nodes.append(cols)
    # ni: node.MyNode = nodes[1][0]
    # print(ni.name)

    # Set connections
    for x in range(0, n):

        for y in range(0, n):

            temp: node.MyNode = nodes[x][y]
            # print("x: " + str(x) + " y: " + str(y))
            # print("Setting : " + temp.name)

            # Does not go up
            if x == 0:

                # Does not go left AND does not go up
                if y == 0:
                    # print("x==0 Does not go left AND does not go up")
                    temp.right = nodes[x][y + 1]
                    temp.weight_right = rand_weight()
                    temp.down = nodes[x + 1][y]
                    temp.weight_down = rand_weight()

                # Does not go right AND does not go up
                elif y == n - 1:
                    # print("x==0 Does not go right AND does not go up")
                    temp.down = nodes[x + 1][y]
                    temp.weight_down = rand_weight()
                    temp.left = nodes[x][y - 1]
                    temp.weight_left = rand_weight()

                # General case, Does not go up AND goes left AND right
                else:
                    # print("x==0 General case, Does not go up AND goes left AND right")
                    temp.right = nodes[x][y + 1]
                    temp.weight_right = rand_weight()
                    temp.down = nodes[x + 1][y]
                    temp.weight_down = rand_weight()
                    temp.left = nodes[x][y - 1]
                    temp.weight_left = rand_weight()

            # Does not go down
            elif x == n - 1:

                if y == n - 1:
                    temp.left = nodes[x][y - 1]
                    temp.weight_left = rand_weight()
                    temp.up = nodes[x - 1][y]
                    temp.weight_up = rand_weight()
                elif y == 0:
                    temp.up = nodes[x - 1][y]
                    temp.weight_up = rand_weight()
                    temp.right = nodes[x][y + 1]
                    temp.weight_right = rand_weight()
                else:
                    temp.right = nodes[x][y + 1]
                    temp.weight_right = rand_weight()
                    temp.left = nodes[x][y - 1]
                    temp.weight_left = rand_weight()
                    temp.up = nodes[x - 1][y]
                    temp.weight_up = rand_weight()

            # General case
            else:
                if y == n - 1:
                    # print("General - Does not go right AND does not go up")
                    temp.down = nodes[x + 1][y]
                    temp.weight_down = rand_weight()
                    temp.up = nodes[x - 1][y]
                    temp.weight_up = rand_weight()
                    temp.left = nodes[x][y - 1]
                    temp.weight_left = rand_weight()
                elif y == 0:
                    temp.down = nodes[x + 1][y]
                    temp.weight_down = rand_weight()
                    temp.up = nodes[x - 1][y]
                    temp.weight_up = rand_weight()
                    temp.right = nodes[x][y + 1]
                    temp.weight_right = rand_weight()
                else:
                    # print("General - General case")
                    temp.right = nodes[x][y + 1]
                    temp.weight_right = rand_weight()
                    temp.down = nodes[x + 1][y]
                    temp.weight_down = rand_weight()
                    temp.left = nodes[x][y - 1]
                    temp.weight_left = rand_weight()
                    temp.up = nodes[x - 1][y]
                    temp.weight_up = rand_weight()

    print("Graph Created")
    return nodes


def remove_edges(percent, node_list):
    print("Removing Edges")
    total = 2 * 2 * n * (n - 1)  # Afou einai amfidromo tote prepei na einai *2 o typos tou fyladiou
    print("Total Edges : " + str(total))
    to_remove = int((p * total) / 100)
    print("Will remove : " + str(to_remove))

    i = 0
    while i < to_remove:
        random_node = random.randrange(1, (n * n) + 1)
        # print("Random Node: " + str(random_node))
        found = False
        for x in range(0, n):
            for y in range(0, n):

                ni: node.MyNode = node_list[x][y]

                if ni.name == str(random_node):
                    result = int(ni.remove_edge())
                    if result == 1:
                        # print("Edge removed from " + ni.name)
                        # ni.print()
                        i += 1
                        found = True
                        break
            if found:
                # print("Breaking, since found")
                break
    print("Edges removed")


def print_graph(node_list):
    for x in range(0, n):
        for y in range(0, n):
            ni: node.MyNode = node_list[x][y]
            ni.print()


def set_states(node_list):
    global start_state
    global end_state_1
    global end_state_2
    print("---------------")
    print("Setting States")
    start = random.randrange(1, (n * n) + 1)

    done = False
    while not done:
        end_1 = random.randrange(1, (n * n) + 1)
        end_2 = random.randrange(1, (n * n) + 1)
        if end_1 != start and end_2 != start:
            if end_1 != end_2:
                done = True
                print("Values changed")

    for x in range(0, n):
        for y in range(0, n):
            ni: node.MyNode = node_list[x][y]
            if ni.name == str(start):
                start_state = ni

            elif ni.name == str(end_1):
                ni.end_state = True
                end_state_1 = ni

            elif ni.name == str(end_2):
                ni.end_state = True
                end_state_2 = ni

    print("States Set")
    print("---------------")


def calc_distance(x, y):
    print("Calculating Manhattan Distance")


# giati priority queue kai visited san orisma ?
def expand(my_node, visited, queue):
    expansion = []
    visited: []
    queue: []
    in_queue = False
    in_visited = False
    ni: node = my_node
    print("Expanding node: " + ni.name)

    if type(ni.up) == node.MyNode:
        print("up")
        in_queue = False
        in_visited = False
        # Yparxei sto queue ?
        for x in range(0, len(queue)):
            qi: node = queue[x]
            if ni.up.name == qi.name:
                in_queue = True
                pos = x
        # Yparxei sto visited ?
        for x in range(0, len(visited)):
            qi: node = visited[x]
            if ni.up.name == qi.name:
                in_visited = True

        if in_visited:
            print("Already visited")
            pass

        # Periptosh diplotypou me diaforetiko kostos
        if in_queue and not in_visited:
            # Clone object, new object has new cost :)
            print("Clone")
            pi: node = queue[pos]
            clone = copy.deepcopy(pi)
            clone.total_cost = ni.total_cost + ni.weight_up
            clone.route = ni.route + " + " + clone.name  # prone to fuck up ?
            expansion.append(clone)

        if not in_queue and not in_visited:
            print("normie")
            ni.up.total_cost = ni.total_cost + ni.weight_up
            ni.up.route = ni.route + " + " + ni.up.name
            expansion.append(ni.up)
    if type(ni.down) == node.MyNode:
        print("down")
        in_queue = False
        in_visited = False
        # Yparxei sto queue ?
        for x in range(0, len(queue)):
            qi: node = queue[x]
            if ni.down.name == qi.name:
                in_queue = True
                pos = x

        # Yparxei sto visited ?
        for x in range(0, len(visited)):
            qi: node = visited[x]
            if ni.down.name == qi.name:
                in_visited = True

        if in_visited:
            print("Already visited")
            pass

        # Periptosh diplotypou me diaforetiko kostos
        if in_queue and not in_visited:
            # Clone object, new object has new cost :)
            print("Clone")
            pi: node = queue[pos]
            clone = copy.deepcopy(pi)
            clone.total_cost = ni.total_cost + ni.weight_down
            clone.route = ni.route + " + " + clone.name  # prone to fuck up ?
            expansion.append(clone)

        if not in_queue and not in_visited:
            print("normie")
            ni.down.total_cost = ni.total_cost + ni.weight_down
            ni.down.route = ni.route + " + " + ni.down.name
            expansion.append(ni.down)
    if type(ni.left) == node.MyNode:
        print("left")
        in_queue = False
        in_visited = False
        # Yparxei sto queue ?
        for x in range(0,len(queue)):
            qi : node = queue[x]
            if ni.left.name == qi.name:
                in_queue = True
                pos = x

        # Yparxei sto visited ?
        for x in range(0,len(visited)):
            qi : node = visited[x]
            if ni.left.name == qi.name:
                in_visited = True

        if in_visited:
            print("Already visited")
            pass

        # Periptosh diplotypou me diaforetiko kostos
        if in_queue and not in_visited:
            # Clone object, new object has new cost :)
            print("Clone")
            pi: node = queue[pos]
            clone = copy.deepcopy(pi)
            clone.total_cost = ni.total_cost + ni.weight_left
            clone.route = ni.route + " + " + clone.name  # prone to fuck up ?
            expansion.append(clone)

        if not in_queue and not in_visited:
            print("normie")
            ni.left.total_cost = ni.total_cost + ni.weight_left
            ni.left.route = ni.route + " + " + ni.left.name
            expansion.append(ni.left)
    if type(ni.right) == node.MyNode:
        print("right")
        in_queue = False
        in_visited = False
        # Yparxei sto queue ?
        for x in range(0, len(queue)):
            qi: node = queue[x]
            if ni.right.name == qi.name:
                in_queue = True
                pos = x

        # Yparxei sto visited ?
        for x in range(0, len(visited)):
            qi: node = visited[x]
            if ni.right.name == qi.name:
                in_visited = True

        if in_visited:
            print("Already visited")
            pass

        # Periptosh diplotypou me diaforetiko kostos
        if in_queue and not in_visited:
            # Clone object, new object has new cost :)
            print("Clone")
            pi: node = queue[pos]
            clone = copy.deepcopy(pi)
            clone.total_cost = ni.total_cost + ni.weight_right
            clone.route = ni.route + " + " + clone.name  # prone to fuck up ?
            expansion.append(clone)

        if not in_queue and not in_visited:
            print("normie")
            ni.right.total_cost = ni.total_cost + ni.weight_right
            ni.right.route = ni.route + " + " + ni.right.name
            expansion.append(ni.right)

    for x in range(0, len(expansion)):
        zi: node = expansion[x]
        print("Expansion: " + zi.name + " COST: " + str(zi.total_cost))
    return expansion


def ucs(start_state):
    print("\nPerforming Unified Cost Search on Graph")
    global node_counter
    priority_queue = []
    visited = []
    in_visited = False
    results = []  # Edo mpainoun oi diadromes pou katalhgoun se kapoio end_State

    priority_queue.append(start_state)

    while len(priority_queue) != 0:
        ni: node = priority_queue[0]

        print("QUEUE:")
        for x in range(0, len(priority_queue)):
            pp: node = priority_queue[x]
            print(pp.name)

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
            expansion: [] = expand(ni, visited, priority_queue)
            priority_queue.extend(expansion)
            node_counter += len(expansion)
            print("Adding " + ni.name + " to visited list")
            visited.append(ni)
        else:
            print("Node " + ni.name + " is normal")
            expansion: [] = expand(ni, visited, priority_queue)
            priority_queue.extend(expansion)
            node_counter += len(expansion)
            print("Adding " + ni.name + " to visited list")
            visited.append(ni)
        print("Removing from queue")
        priority_queue.remove(ni)
        priority_queue.sort(key=operator.attrgetter('total_cost'))
    if len(results) == 0:
        print("UCS Search cannot reach end state")
    else:
        results.sort(key=operator.attrgetter('total_cost'))
        # print("Results are: ")
        # print_graph(results)
        nu: node = results[0]
        print("Best result is: " + nu.name)
        nu.print()
        print("Total nodes created: " + str(node_counter))
        return results


# n = int(input("Enter n: "))
# p: int = int(input("Enter p: "))
# max_weight = int(input("Enter max: "))

nodesList = create_graph(n)
remove_edges(p, nodesList)
set_states(nodesList)
print_graph(nodesList)

start_state = nodesList[0][0]  # 1

ni: node.MyNode = start_state
print("\nStart State: " + ni.name)
ni: node.MyNode = end_state_1
print("End State 1: " + ni.name)
ni: node.MyNode = end_state_2
print("End State 2: " + ni.name)
ucs(start_state)

'''
# Prints expansion
v = []
q = []
e = expand(start_state, v, q)
for x in range(0, len(e)):
    ni: node = e[x]
    print("Name: " + ni.name + ": " + "Route: " + ni.route)
'''
