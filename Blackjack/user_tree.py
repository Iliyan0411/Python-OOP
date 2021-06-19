from player import Player


class Node:
    def __init__(self):
        self.data = None
        self.end_of_word = False
        self.children = {}
        

class UserTree:
    def __init__(self) -> None:
        self.root = Node()


    def add(self, user: Player):
        self._add(self.root, 0, user)


    def _add(self, curr_node: Node, i, user: Player):
        name = user.username

        if not name[i] in curr_node.children:
            curr_node.children[name[i]] = Node()
        
        if i == len(name) - 1:
            curr_node.children[name[i]].end_of_word = True
            curr_node.children[name[i]].data = user
            return

        self._add(curr_node.children[name[i]], i+1, user)


    def print(self):
        self._print(self.root)

    def _print(self, curr_node: Node):
        if curr_node.data != None:
            print(curr_node.data.username)

        for child in curr_node.children:
            self._print(curr_node.children[child])



# p1 = Player("Iliyan", 20, "dth")
# p2 = Player("Ivan", 20, "dth")
# p3 = Player("Niki", 20, "dth")
# p4 = Player("Spasi", 20, "dth")
# p5 = Player("Lusi", 20, "dth")
# p6 = Player("Asen", 20, "dth")

# ut = UserTree()

# ut.add(p1)
# ut.add(p2)
# ut.add(p3)
# ut.add(p4)
# ut.add(p5)
# ut.add(p6)

# ut.print()