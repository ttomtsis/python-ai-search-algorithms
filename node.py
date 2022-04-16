import copy
import random


class MyNode:

    # Constructor, n is MyNode's name, eg: 1,2,3
    def __init__(self, n):
        # MyNode name
        self.name = str(n)

        # Coordinates in Graph
        self.x = -1
        self.y = -1

        # MyNode Neighbors and weights
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.weight_up = 0
        self.weight_down = 0
        self.weight_left = 0
        self.weight_right = 0
        self.end_state = False  # State

        # Total Path Cost
        self.total_cost = 0  # Path Cost

        # Manhattan distance from CLOSEST end state
        self.manhattan = -1

        # A* cost, Total path cost + Manhattan distance
        self.a_star_cost = -1

        # Route taken, to easily print ( Remove ? )
        self.route = self.name  # Parents, to view easily

        # MyNode's parent after expansion
        self.parent = None

    # Prints fields
    def print(self):
        print("\n----- " + self.name + " -----")

        ni: MyNode = self.up
        if type(ni) == bool:
            print("Up: " + str(self.up) + " - Weight: " + str(self.weight_up))
        else:
            print("Up: " + ni.name + " - Weight: " + str(self.weight_up))

        ni: MyNode = self.down
        if type(ni) == bool:
            print("Down: " + str(self.down) + " - Weight: " + str(self.weight_down))
        else:
            print("Down: " + ni.name + " - Weight: " + str(self.weight_down))

        ni: MyNode = self.left
        if type(ni) == bool:
            print("Left: " + str(self.left) + " - Weight: " + str(self.weight_left))
        else:
            print("Left: " + ni.name + " - Weight: " + str(self.weight_left))

        ni: MyNode = self.right
        if type(ni) == bool:
            print("Right: " + str(self.right) + " - Weight: " + str(self.weight_right))
        else:
            print("Right: " + ni.name + " - Weight: " + str(self.weight_right))

        ni: MyNode = self.end_state
        if ni:
            print("End State: True")
        else:
            print("End State: False")

        print("Total cost: " + str(self.total_cost))

        print("Manhattan Distance: " + str(self.manhattan))

        print("A* Cost: " + str(self.a_star_cost))

        print("Route: " + self.route)

    # Removes random MyNode edge
    def remove_edge(self):

        if (self.up == False and self.down == False
                and self.left == False and self.right == False):
            return -1

        while True:
            choice = random.randrange(1, 5)

            if choice == 1 and self.up != False:
                self.up = False
                self.weight_up = 0
                return 1
            elif choice == 2 and self.down != False:
                self.down = False
                self.weight_down = 0
                return 1
            elif choice == 3 and self.left != False:
                self.left = False
                self.weight_left = 0
                return 1
            elif choice == 4 and self.right != False:
                self.right = False
                self.weight_right = 0
                return 1

    # Resets total_cost and parent so that
    # a new search algorithm can be applied to graph
    def reset(self):
        self.parent = None
        self.total_cost = 0
        self.a_star_cost = self.manhattan
        self.route = self.name

    # giati priority queue kai visited san orisma ?
    def expand(self, my_node, visited, priority_queue):
        expansion = []
        in_queue = False
        in_visited = False
        ni: MyNode = my_node
        print("Expanding MyNode: " + ni.name)

        if type(ni.up) == MyNode:
            in_queue = False
            in_visited = False
            # Yparxei sto queue ?
            for x in range(0, len(priority_queue)):
                qi: MyNode = priority_queue[x]
                if ni.up.name == qi.name:
                    in_queue = True
                    pos = x
            # Yparxei sto visited ?
            for x in range(0, len(visited)):
                qi: MyNode = visited[x]
                if ni.up.name == qi.name:
                    in_visited = True

            if in_visited:
                pass

            # Periptosh diplotypou me diaforetiko kostos
            if in_queue and not in_visited:
                # Clone object, new object has new cost :)
                pi: MyNode = priority_queue[pos]
                clone = copy.deepcopy(pi)
                clone.total_cost = ni.total_cost + ni.weight_up
                clone.route = ni.route + " + " + clone.name
                clone.parent = ni
                clone.a_star_cost = clone.manhattan + clone.total_cost
                expansion.append(clone)

            if not in_queue and not in_visited:
                ni.up.total_cost = ni.total_cost + ni.weight_up
                ni.up.route = ni.route + " + " + ni.up.name
                ni.up.parent = ni
                ni.up.a_star_cost = ni.up.total_cost + ni.up.manhattan
                expansion.append(ni.up)
        if type(ni.down) == MyNode:
            in_queue = False
            in_visited = False
            # Yparxei sto queue ?
            for x in range(0, len(priority_queue)):
                qi: MyNode = priority_queue[x]
                if ni.down.name == qi.name:
                    in_queue = True
                    pos = x

            # Yparxei sto visited ?
            for x in range(0, len(visited)):
                qi: MyNode = visited[x]
                if ni.down.name == qi.name:
                    in_visited = True

            if in_visited:
                print("Already visited")
                pass

            # Periptosh diplotypou me diaforetiko kostos
            if in_queue and not in_visited:
                # Clone object, new object has new cost :)
                print("Clone")
                pi: MyNode = priority_queue[pos]
                clone = copy.deepcopy(pi)
                clone.total_cost = ni.total_cost + ni.weight_down
                clone.route = ni.route + " + " + clone.name
                clone.parent = ni
                clone.a_star_cost = clone.manhattan + clone.total_cost
                expansion.append(clone)

            if not in_queue and not in_visited:
                print("normie")
                ni.down.total_cost = ni.total_cost + ni.weight_down
                ni.down.route = ni.route + " + " + ni.down.name
                ni.down.parent = ni
                ni.down.a_star_cost = ni.down.total_cost + ni.down.manhattan
                expansion.append(ni.down)
        if type(ni.left) == MyNode:
            print("left")
            in_queue = False
            in_visited = False
            # Yparxei sto queue ?
            for x in range(0, len(priority_queue)):
                qi: MyNode = priority_queue[x]
                if ni.left.name == qi.name:
                    in_queue = True
                    pos = x

            # Yparxei sto visited ?
            for x in range(0, len(visited)):
                qi: MyNode = visited[x]
                if ni.left.name == qi.name:
                    in_visited = True

            if in_visited:
                print("Already visited")
                pass

            # Periptosh diplotypou me diaforetiko kostos
            if in_queue and not in_visited:
                # Clone object, new object has new cost :)
                print("Clone")
                pi: MyNode = priority_queue[pos]
                clone = copy.deepcopy(pi)
                clone.total_cost = ni.total_cost + ni.weight_left
                clone.route = ni.route + " + " + clone.name
                clone.parent = ni
                clone.a_star_cost = clone.manhattan + clone.total_cost
                expansion.append(clone)

            if not in_queue and not in_visited:
                print("normie")
                ni.left.total_cost = ni.total_cost + ni.weight_left
                ni.left.route = ni.route + " + " + ni.left.name
                ni.left.parent = ni
                ni.left.a_star_cost = ni.left.total_cost + ni.left.manhattan
                expansion.append(ni.left)
        if type(ni.right) == MyNode:
            print("right")
            in_queue = False
            in_visited = False
            # Yparxei sto queue ?
            for x in range(0, len(priority_queue)):
                qi: MyNode = priority_queue[x]
                if ni.right.name == qi.name:
                    in_queue = True
                    pos = x

            # Yparxei sto visited ?
            for x in range(0, len(visited)):
                qi: MyNode = visited[x]
                if ni.right.name == qi.name:
                    in_visited = True

            if in_visited:
                print("Already visited")
                pass

            # Periptosh diplotypou me diaforetiko kostos
            if in_queue and not in_visited:
                # Clone object, new object has new cost :)
                print("Clone")
                pi: MyNode = priority_queue[pos]
                clone = copy.deepcopy(pi)
                clone.total_cost = ni.total_cost + ni.weight_right
                clone.route = ni.route + " + " + clone.name
                clone.parent = ni
                clone.a_star_cost = clone.manhattan + clone.total_cost
                expansion.append(clone)

            if not in_queue and not in_visited:
                print("normie")
                ni.right.total_cost = ni.total_cost + ni.weight_right
                ni.right.route = ni.route + " + " + ni.right.name
                ni.right.parent = ni
                ni.right.a_star_cost = ni.right.total_cost + ni.right.manhattan
                expansion.append(ni.right)

        for x in range(0, len(expansion)):
            zi: MyNode = expansion[x]
            print("Expansion: " + zi.name + " COST: " + str(zi.total_cost))
            print("Parent: " + zi.parent.name)
        return expansion
