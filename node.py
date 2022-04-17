"""
This class represents a node object
and contains appropriate methods to
handle it as well as initialize it
"""

import copy
import random


class MyNode:

    # Constructor. n is node's name, eg: 1,2,3
    def __init__(self, n):

        # Node name
        self.name = str(n)

        # Coordinates in Graph
        self.x = -1
        self.y = -1

        # Node Neighbors and weights
        self.up = None
        self.down = None
        self.left = None
        self.right = None
        self.weight_up = None
        self.weight_down = None
        self.weight_left = None
        self.weight_right = None

        # Is the node a start or an end state ?
        self.start_state = False
        self.end_state = False

        '''
        Total cost of path so far.
        This is the TRUE cost of the path from one node to another,
        this isn't an estimate and is calculated upon expansion of the node.
        When expanding a node, and that node is an end state, that node is added
        on the results list, the total_cost field of the nodes in the results list
        represents the true total cost of the best path.
        '''
        self.total_cost = 0  # Path Cost

        # The Manhattan distance from the CLOSEST end state
        # refer to calc_distance() for more information
        self.manhattan = -1

        # A* cost, Initialized at this point with -1
        # Is calculated later like this:
        # Total path cost + Manhattan distance
        self.a_star_cost = -1

        # Route taken, so far.
        # This field is only used to easily print node taken and
        # to debug any mistakes. Can be removed in future versions
        self.route = self.name

        # Node's parent after expansion
        self.parent = None

    # Prints node fields
    def print(self):
        print("\n----- " + self.name + " -----")

        #  Checks if neighbour exists
        if type(self.up) == MyNode:
            print("Up: " + self.up.name + " - Weight: " + str(self.weight_up))
        else:
            print("Up: None")

        if type(self.down) == MyNode:
            print("Down: " + self.down.name + " - Weight: " + str(self.weight_down))
        else:
            print("Down: None")

        if type(self.left) == MyNode:
            print("Left: " + self.left.name + " - Weight: " + str(self.weight_left))
        else:
            print("Left: None")

        if type(self.right) == MyNode:
            print("Right: " + self.right.name + " - Weight: " + str(self.weight_right))
        else:
            print("Right: None")

        if self.end_state:
            print("End State: True")
        else:
            print("End State: False")

        print("Total cost: " + str(self.total_cost))

        print("Manhattan Distance: " + str(self.manhattan))

        print("A* Cost: " + str(self.a_star_cost))

        print("Route: " + self.route)

    # Removes a random edge from node
    def remove_edge(self):
        
        # Check if node actually has any edges to remove,
        # if not return appropriate response
        if (self.up is None and self.down is None
                and self.left is None and self.right is None):
            return -1

        # Choose a random edge, loop until the random edge chosen
        # is confirmed to exist, after that set it to None and return
        while True:
            # Random edge choice is implemented here as a
            # random integer chosen, integers 1- 4 represent an edge here
            choice = random.randrange(1, 5)

            if choice == 1 and self.up is not None:
                self.up = None
                self.weight_up = 0
                return 1
            elif choice == 2 and self.down is not None:
                self.down = None
                self.weight_down = 0
                return 1
            elif choice == 3 and self.left is not None:
                self.left = None
                self.weight_left = 0
                return 1
            elif choice == 4 and self.right is not None:
                self.right = None
                self.weight_right = 0
                return 1

    # Resets total_cost and parent so that
    # a new search algorithm can be applied to graph
    # ( Since
    def reset(self):
        self.parent = None
        self.total_cost = 0
        self.a_star_cost = self.manhattan
        self.route = self.name

    '''
    Expand is responsible for expanding the node, and
    returning the result of the expansions ( the child nodes ).
    Currently this method is poorly implemented and while working,
    is very difficult to debug and maintain. This will probably be worked on
    in feature commits, provided that there is enough time on our end.
    
    The basic logic behind expand is as follows:
    
    1) Take a node
    2) Check which neighbours the node has. ( children ) eg check if node has up, down etc neighbours
    3) Check EVERY child node ( provided that it exists ) for the following:
        ( This is the purpose of the 4 if statements below, feel free to fold them at this point and only
        focus in one of them. This will make reading easier, since all 4 statements do the exact same thing )
        
        i) Has the child already been visited ? If yes then do nothing
        ii) Does the child exist already in the priority queue and has not yet been visited ?
            if so, then clone the object. This is called a "DUPLICATE NODE" case.
            More on this later
        iii) If the child has not been visited and does not exist in the priority queue
            then treat it as a normal node, expand it and return expansion.
    
        It is important to understand the DUPLICATE NODE case. It is possible
    that when expanding a node, one of it's children already exists in
    the search tree ( priority queue in our case ) but with a different
    cost ( either better or worse ). To simulate this case in python code, we 
    check the priority queue for the NAMES of the nodes ( more on this below ).
    Once we find a duplicate object in the queue, we make a copy of it,
    change the copy's cost values accordingly and THEN add it to the queue.
    
        We check the NAMES of the nodes for the following reason: 
    Suppose that node 3 is expanded into 4, node 4 is added to the queue with its cost ( eg cost = 5 ).
    Now suppose that node 7 also has node 4 as a child, we check if node 4 exists in the queue 
    (with some list method ), we will get a false negative result, since node 4 with original cost
    DOES NOT exist in the queue since it's cost has been modified by the previous expansion of node 3.
    Hence we check for the NAMES of the nodes, instead of using one of the build-in list methods.
    '''
    def expand(self, visited, priority_queue):

        expansion = []

        print("EXPANDING : " + self.name)

        if type(self.up) == MyNode:
            print("Node has neighbor UP: " + self.up.name)
            in_queue = False
            in_visited = False

            # Check if it exists in queue
            for x in range(0, len(priority_queue)):
                qi: MyNode = priority_queue[x]
                if self.up.name == qi.name:
                    in_queue = True

                    # Keep duplicate's position , so it can be copied later
                    pos = x

            # Check if it exists in visited
            for x in range(0, len(visited)):
                qi: MyNode = visited[x]
                if self.up.name == qi.name:
                    in_visited = True

            # If already visited pass
            if in_visited:
                print("UP neighbour is visited")
                pass

            # If it is a duplicate node case, deepcopy
            # duplicate node and alter copy's cost
            if in_queue and not in_visited:
                # Clone object, new object has new cost :)
                print("Node " + self.up.name + " is in queue and not in visited. will clone")

                # pi is the duplicate node
                pi: MyNode = priority_queue[pos]

                # clone is the new copy of the duplicate node ( pi )
                clone = copy.deepcopy(pi)
                # new cost will be expanding node's path cost + the new expansion cost
                clone.total_cost = self.total_cost + self.weight_up
                clone.route = self.route + " + " + clone.name
                clone.parent = self
                clone.a_star_cost = clone.manhattan + clone.total_cost
                expansion.append(clone)

            # Normal node case, simply expand
            if not in_queue and not in_visited:
                print("Node " + self.up.name + " is a normal case")

                # Calculate cost in similar manner as above
                self.up.total_cost = self.total_cost + self.weight_up
                self.up.route = self.route + " + " + self.up.name
                self.up.parent = self
                self.up.a_star_cost = self.up.total_cost + self.up.manhattan
                expansion.append(self.up)

        # The EXACT same logic is followed as above case,
        # below if statements can be considered duplicated code fragments
        if type(self.down) == MyNode:
            print("Node has neighbour DOWN: " + self.down.name)
            in_queue = False
            in_visited = False

            for x in range(0, len(priority_queue)):
                qi: MyNode = priority_queue[x]
                if self.down.name == qi.name:
                    in_queue = True
                    pos = x

            for x in range(0, len(visited)):
                qi: MyNode = visited[x]
                if self.down.name == qi.name:
                    in_visited = True

            if in_visited:
                print("Down neighbour " + self.down.name + " visited already")
                pass

            if in_queue and not in_visited:
                # Clone object, new object has new cost :)
                print("Node " + self.down.name + " is in queue and not in visited")
                pi: MyNode = priority_queue[pos]
                clone = copy.deepcopy(pi)
                clone.total_cost = self.total_cost + self.weight_down
                clone.route = self.route + " + " + clone.name
                clone.parent = self
                clone.a_star_cost = clone.manhattan + clone.total_cost
                expansion.append(clone)

            if not in_queue and not in_visited:
                print("Node " + self.down.name + " is a normal case")
                self.down.total_cost = self.total_cost + self.weight_down
                self.down.route = self.route + " + " + self.down.name
                self.down.parent = self
                self.down.a_star_cost = self.down.total_cost + self.down.manhattan
                expansion.append(self.down)
        if type(self.left) == MyNode:
            print("Node has neighbour LEFT: " + self.left.name)
            in_queue = False
            in_visited = False

            for x in range(0, len(priority_queue)):
                qi: MyNode = priority_queue[x]
                if self.left.name == qi.name:
                    in_queue = True
                    pos = x

            for x in range(0, len(visited)):
                qi: MyNode = visited[x]
                if self.left.name == qi.name:
                    in_visited = True

            if in_visited:
                print("Left neighbour" + self.left.name + "Already visited")
                pass

            if in_queue and not in_visited:
                print("Node " + self.left.name + " will be cloned")
                pi: MyNode = priority_queue[pos]
                clone = copy.deepcopy(pi)
                clone.total_cost = self.total_cost + self.weight_left
                clone.route = self.route + " + " + clone.name
                clone.parent = self
                clone.a_star_cost = clone.manhattan + clone.total_cost
                expansion.append(clone)

            if not in_queue and not in_visited:
                print("Node " + self.left.name + " is a normal case")
                self.left.total_cost = self.total_cost + self.weight_left
                self.left.route = self.route + " + " + self.left.name
                self.left.parent = self
                self.left.a_star_cost = self.left.total_cost + self.left.manhattan
                expansion.append(self.left)
        if type(self.right) == MyNode:
            print("Node has Neighbour RIGHT: " + self.right.name)
            in_queue = False
            in_visited = False

            for x in range(0, len(priority_queue)):
                qi: MyNode = priority_queue[x]
                if self.right.name == qi.name:
                    in_queue = True
                    pos = x

            for x in range(0, len(visited)):
                qi: MyNode = visited[x]
                if self.right.name == qi.name:
                    in_visited = True

            if in_visited:
                print("Right neighbour " + self.right.name + "Already visited")
                pass

            if in_queue and not in_visited:
                # Clone object, new object has new cost :)
                print("Node " + self.right.name + " will be cloned")
                pi: MyNode = priority_queue[pos]
                clone = copy.deepcopy(pi)
                clone.total_cost = self.total_cost + self.weight_right
                clone.route = self.route + " + " + clone.name
                clone.parent = self
                clone.a_star_cost = clone.manhattan + clone.total_cost
                expansion.append(clone)

            if not in_queue and not in_visited:
                print("Node " + self.right.name + " is a normal case")
                self.right.total_cost = self.total_cost + self.weight_right
                self.right.route = self.route + " + " + self.right.name
                self.right.parent = self
                self.right.a_star_cost = self.right.total_cost + self.right.manhattan
                expansion.append(self.right)

        # Print the expansion results
        for x in range(0, len(expansion)):
            zi: MyNode = expansion[x]
            print("EXPANSION: " + zi.name + " COST: " + str(zi.total_cost))
            print("Parent: " + zi.parent.name)
        return expansion
