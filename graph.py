import random
import node


class Graph:

    def __init__(self, nodes, percent, max):
        self.max_weight = max
        self.n = nodes
        self.p = percent
        self.start_state = None
        self.end_state_1 = None
        self.end_state_2 = None
        self.nodesList = []
        self.create_graph()
        self.remove_edges()
        self.set_states()
        self.create_heuristics()
        self.print_graph()

    def print_graph(self):

        for x in range(0, self.n):
            for y in range(0, self.n):
                ni: node.MyNode = self.nodesList[x][y]
                ni.print()

    def rand_weight(self):
        return int(random.randrange(1, self.max_weight))

    def create_graph(self):
        print("Creating Graph")
        print("Size will be: " + str(self.n) + " X " + str(self.n))
        counter = 1

        # Dhmiourgia antikeimenon
        # topothetisi se "pinaka"
        for x in range(0, self.n):
            cols = []
            for y in range(0, self.n):
                ni = node.MyNode(str(counter))
                ni.x = x
                ni.y = y
                cols.append(ni)
                counter += 1
            self.nodesList.append(cols)
        # ni: node.MyNode = nodes[1][0]
        # print(ni.name)

        # Set connections
        for x in range(0, self.n):

            for y in range(0, self.n):

                temp: node.MyNode = self.nodesList[x][y]
                # print("x: " + str(x) + " y: " + str(y))
                # print("Setting : " + temp.name)

                # Does not go up
                if x == 0:

                    # Does not go left AND does not go up
                    if y == 0:
                        # print("x==0 Does not go left AND does not go up")
                        temp.right = self.nodesList[x][y + 1]
                        temp.weight_right = self.rand_weight()
                        temp.down = self.nodesList[x + 1][y]
                        temp.weight_down = self.rand_weight()

                    # Does not go right AND does not go up
                    elif y == self.n - 1:
                        # print("x==0 Does not go right AND does not go up")
                        temp.down = self.nodesList[x + 1][y]
                        temp.weight_down = self.rand_weight()
                        temp.left = self.nodesList[x][y - 1]
                        temp.weight_left = self.rand_weight()

                    # General case, Does not go up AND goes left AND right
                    else:
                        # print("x==0 General case, Does not go up AND goes left AND right")
                        temp.right = self.nodesList[x][y + 1]
                        temp.weight_right = self.rand_weight()
                        temp.down = self.nodesList[x + 1][y]
                        temp.weight_down = self.rand_weight()
                        temp.left = self.nodesList[x][y - 1]
                        temp.weight_left = self.rand_weight()

                # Does not go down
                elif x == self.n - 1:

                    if y == self.n - 1:
                        temp.left = self.nodesList[x][y - 1]
                        temp.weight_left = self.rand_weight()
                        temp.up = self.nodesList[x - 1][y]
                        temp.weight_up = self.rand_weight()
                    elif y == 0:
                        temp.up = self.nodesList[x - 1][y]
                        temp.weight_up = self.rand_weight()
                        temp.right = self.nodesList[x][y + 1]
                        temp.weight_right = self.rand_weight()
                    else:
                        temp.right = self.nodesList[x][y + 1]
                        temp.weight_right = self.rand_weight()
                        temp.left = self.nodesList[x][y - 1]
                        temp.weight_left = self.rand_weight()
                        temp.up = self.nodesList[x - 1][y]
                        temp.weight_up = self.rand_weight()

                # General case
                else:
                    if y == self.n - 1:
                        # print("General - Does not go right AND does not go up")
                        temp.down = self.nodesList[x + 1][y]
                        temp.weight_down = self.rand_weight()
                        temp.up = self.nodesList[x - 1][y]
                        temp.weight_up = self.rand_weight()
                        temp.left = self.nodesList[x][y - 1]
                        temp.weight_left = self.rand_weight()
                    elif y == 0:
                        temp.down = self.nodesList[x + 1][y]
                        temp.weight_down = self.rand_weight()
                        temp.up = self.nodesList[x - 1][y]
                        temp.weight_up = self.rand_weight()
                        temp.right = self.nodesList[x][y + 1]
                        temp.weight_right = self.rand_weight()
                    else:
                        # print("General - General case")
                        temp.right = self.nodesList[x][y + 1]
                        temp.weight_right = self.rand_weight()
                        temp.down = self.nodesList[x + 1][y]
                        temp.weight_down = self.rand_weight()
                        temp.left = self.nodesList[x][y - 1]
                        temp.weight_left = self.rand_weight()
                        temp.up = self.nodesList[x - 1][y]
                        temp.weight_up = self.rand_weight()

        print("Graph Created")

    def remove_edges(self):

        print("Removing Edges")
        total = 2 * 2 * self.n * (self.n - 1)  # Afou einai amfidromo tote prepei na einai *2 o typos tou fyladiou
        print("Total Edges : " + str(total))
        to_remove = int((self.p * total) / 100)
        print("Will remove : " + str(to_remove))

        i = 0
        while i < to_remove:
            random_node = random.randrange(1, (self.n * self.n) + 1)
            # print("Random Node: " + str(random_node))
            found = False
            for x in range(0, self.n):
                for y in range(0, self.n):

                    ni: node.MyNode = self.nodesList[x][y]

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

    def set_states(self):

        print("---------------")
        print("Setting States")
        start = random.randrange(1, (self.n * self.n) + 1)

        done = False
        while not done:
            end_1 = random.randrange(1, (self.n * self.n) + 1)
            end_2 = random.randrange(1, (self.n * self.n) + 1)
            if end_1 != start and end_2 != start:
                if end_1 != end_2:
                    done = True
                    print("Values changed")

        for x in range(0, self.n):
            for y in range(0, self.n):
                ni: node.MyNode = self.nodesList[x][y]
                if ni.name == str(start):
                    self.start_state = ni

                elif ni.name == str(end_1):
                    ni.end_state = True
                    self.end_state_1 = ni

                elif ni.name == str(end_2):
                    ni.end_state = True
                    self.end_state_2 = ni

        print("States Set")
        print("---------------")

    def calc_distance(self, x1, x2, y1, y2):
        x = x1 - x2
        if x < 0:
            x = x * (-1)
        y = y1 - y2
        if y < 0:
            y = y * (-1)
        return x + y

    def create_heuristics(self):
        print("Creating Heuristic Table")

        for x in range(0, self.n):
            for y in range(0, self.n):
                ni: node.MyNode = self.nodesList[x][y]
                dist_1 = self.calc_distance(ni.x, self.end_state_1.x, ni.y, self.end_state_1.y)
                dist_2 = self.calc_distance(ni.x, self.end_state_2.x, ni.y, self.end_state_2.y)
                if dist_1 < dist_2:
                    ni.manhattan = dist_1
                else:
                    ni.manhattan = dist_2
                ni.a_star_cost = ni.manhattan

    def reset(self):

        for x in range(0, self.n):
            for y in range(0, self.n):
                ni: node = self.nodesList[x][y]
                ni.reset()

