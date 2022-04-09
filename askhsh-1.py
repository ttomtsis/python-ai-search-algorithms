import node
import random

max_weight = 10
n = 3
p = 20

start_state = -1
end_state_1 = -1
end_state_2 = -1


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


def ucs(nodes_list):
    pass


# n = int(input("Enter n: "))
# p: int = int(input("Enter p: "))
# max_weight = int(input("Enter max: "))

nodesList = create_graph(n)
remove_edges(p, nodesList)
set_states(nodesList)
print_graph(nodesList)

start_state = nodesList[0][0]  # 1

ni: node.MyNode = start_state
print("Start State: " + ni.name)
ni: node.MyNode = end_state_1
print("End State 1: " + ni.name)
ni: node.MyNode = end_state_2
print("End State 2: " + ni.name)
