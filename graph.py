"""
This file contains the graph class,
used to construct a graph of size n x n
alongside with the appropriate methods to handle it.
The graph is a simple "2-D list" containing the nodes
"""

import random
import node


class Graph:

    # Constructor takes as parameter dimensions, percent of
    # edges to be removed and max edge cost
    def __init__(self, n_dimension, percent, max):
        self.max_weight = max
        self.n = n_dimension
        self.p = percent
        self.start_state = None
        self.end_state_1 = None
        self.end_state_2 = None
        self.nodesList = []  # Nodes are stored here, this is the "graph"

        # Create the graph
        self.create_graph()
        self.remove_edges()
        self.set_states()
        self.create_heuristics()
        self.print_graph()

    # Prints the graph
    def print_graph(self):

        for x in range(0, self.n):
            for y in range(0, self.n):
                ni: node.MyNode = self.nodesList[x][y]
                ni.print()
        print("\n")

    # Support function, used by create_Graph.
    # Returns a random number from 0 to maximum cost of the edges
    def rand_weight(self):
        return int(random.randrange(1, self.max_weight))

    # Creates the 2-D list that contains the nodes
    def create_graph(self):
        print("Creating Graph")
        print("Size will be: " + str(self.n) + " X " + str(self.n))
        counter = 1

        # Create node objects
        # place them in lists
        for x in range(0, self.n):
            cols = []
            for y in range(0, self.n):
                ni = node.MyNode(str(counter))
                ni.x = x
                ni.y = y
                cols.append(ni)
                counter += 1
            self.nodesList.append(cols)

        # Create Edges
        for x in range(0, self.n):

            for y in range(0, self.n):

                temp: node.MyNode = self.nodesList[x][y]

                # If x is 0, a.k.a the first line in a 2-D array,
                # then the nodes cannot have a neighbour upwards
                if x == 0:

                    # If y is 0, a.k.a. the first column in a 2-D array,
                    # then the nodes cannot have a neighbour on the left
                    # so to sum it up this is the case where the nodes
                    # only have a neighbour down and on the right
                    if y == 0:
                        temp.right = self.nodesList[x][y + 1]
                        temp.weight_right = self.rand_weight()
                        temp.down = self.nodesList[x + 1][y]
                        temp.weight_down = self.rand_weight()

                    # In similar fashion, cannot have edges upwards and to the right
                    elif y == self.n - 1:
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

                # If x = n-1, a.k.a the last line of a 2-D array,
                # then the edges cannot be downwards
                elif x == self.n - 1:

                    # In similar fashion we check the columns
                    # and adjust the edges accordingly
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

                # General case, nodes can have edges on any direction.
                # however, column conditions still apply, as shown below
                else:
                    if y == self.n - 1:
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
                        temp.right = self.nodesList[x][y + 1]
                        temp.weight_right = self.rand_weight()
                        temp.down = self.nodesList[x + 1][y]
                        temp.weight_down = self.rand_weight()
                        temp.left = self.nodesList[x][y - 1]
                        temp.weight_left = self.rand_weight()
                        temp.up = self.nodesList[x - 1][y]
                        temp.weight_up = self.rand_weight()

        print("Graph Created")

    # Removes a percentage of edges from the graph
    # edges to be removed from each node, as well as
    # how many edges per node are to be removed is random.
    # See remove_Edge() in node.py for more information,
    # This function simply chooses a random node, the rest
    # is handled by the node class's inherent method
    def remove_edges(self):

        print("Removing Edges")
        total = 2 * 2 * self.n * (self.n - 1)  # Total edges of the graph
        print("Total Edges : " + str(total))
        to_remove = int((self.p * total) / 100)  # Final number of removed edges
        print("Will remove : " + str(to_remove))

        # Loop to_remove times, each time a random edge, from a random node
        # is removed.
        i = 0
        while i < to_remove:

            # Choose a random node
            random_node = random.randrange(1, (self.n * self.n) + 1)

            # Find node inside graph, remove edges then continue
            # to next node. found boolean and if conditions below
            # are used strictly to improve performance and do not
            # affect the logic described above
            found = False
            for x in range(0, self.n):
                for y in range(0, self.n):

                    ni: node.MyNode = self.nodesList[x][y]

                    if ni.name == str(random_node):
                        result = int(ni.remove_edge())
                        if result == 1:
                            i += 1
                            found = True
                            break
                if found:
                    break
        print("Edges removed")

    def set_states(self):

        print("Setting States")
        start = random.randrange(1, (self.n * self.n) + 1)

        done = False
        while not done:
            end_1 = random.randrange(1, (self.n * self.n) + 1)
            end_2 = random.randrange(1, (self.n * self.n) + 1)
            if end_1 != start and end_2 != start:
                if end_1 != end_2:
                    done = True

        for x in range(0, self.n):
            for y in range(0, self.n):
                ni: node.MyNode = self.nodesList[x][y]
                if ni.name == str(start):
                    ni.start_state = True
                    self.start_state = ni

                elif ni.name == str(end_1):
                    ni.end_state = True
                    self.end_state_1 = ni

                elif ni.name == str(end_2):
                    ni.end_state = True
                    self.end_state_2 = ni

        print("States Set")

    # Supporting method, used by create_heuristics() below
    # calculates manhattan distance, based on the location
    # of 2 nodes on the graph
    def calc_distance(self, x1, x2, y1, y2):
        x = x1 - x2
        if x < 0:
            x = x * (-1)
        y = y1 - y2
        if y < 0:
            y = y * (-1)
        return x + y

    # Creates the Heuristics used by A* and greedy BFS algorithms
    # Chooses the SMALLEST manhattan distance between the 2 end states
    # then sets the A* cost as equal to the manhattan distance
    # ( A* cost is calculated during expansion either way )
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

    # Resets the nodes of the graph
    # so that a new search algorithm can be applied.
    # this happens since during search numerous class fields
    # are altered and cannot be re-used for another search
    def reset(self):

        for x in range(0, self.n):
            for y in range(0, self.n):
                ni: node = self.nodesList[x][y]
                ni.reset()

