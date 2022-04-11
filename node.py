import random


class MyNode:

    def __init__(self, n):
        self.name = str(n)
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.weight_up = 0
        self.weight_down = 0
        self.weight_left = 0
        self.weight_right = 0
        self.end_state = False

        # UCS
        self.total_cost = 0
        self.route = self.name

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

        print("Route: " + self.route)

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
