from player import Player


class Node:
    def __init__(self):
        self.data = None
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
            curr_node.children[name[i]].data = user
            return

        self._add(curr_node.children[name[i]], i+1, user)


    def exist(self, username, password):
        curr_node = self.root

        for s in username:
            if not s in curr_node.children:
                return False

            curr_node = curr_node.children[s]

        return curr_node.data != None and curr_node.data.password == password


    def locate(self):
        pass


    def remove(self):
        pass



# tree = UserTree()
# tree.add(Player("Iliyan", 20, "shfdt"))
# tree.add(Player("Spasi", 20, "shfdt"))
# tree.add(Player("Aneta", 20, "shfdt"))
# tree.add(Player("Dimitar", 20, "shfdt"))
# tree.add(Player("Kiril", 20, "shfdt"))
# tree.add(Player("Mihail", 20, "shfdt"))

# print(tree.exist("Iliyan", "shfdt"))
# print(tree.exist("Spasi", "shfdt"))
# print(tree.exist("Aneta", "shfdt"))
# print(tree.exist("Dimitar", "shfdt"))
# print(tree.exist("Kiril", "shfdt"))
# print(tree.exist("Mihail", "shfdt"))

# print(tree.exist("Asen", "shfdt"))
# print(tree.exist("Il", "shfdt"))
# print(tree.exist("yan", "shfdt"))
# print(tree.exist(" ", "shfdt"))
# print(tree.exist("", "shfdt"))
# print(tree.exist("Mihail", "wrong"))