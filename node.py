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

    def print(self):
        print("----- " + self.name + " -----")
        print("Up: " + str(self.up) + " - " + str(self.weight_up))
        print("Down: " + str(self.down) + " - " + str(self.weight_down))
        print("Left: " + str(self.left) + " - " + str(self.weight_left))
        print("Right: " + str(self.right) + " - " + str(self.weight_right))

