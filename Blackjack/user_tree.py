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


    def locate(self, username):
        curr_node = self.root

        for s in username:
            if not s in curr_node.children:
                return None
            curr_node = curr_node.children[s]

        return curr_node.data
    
    
    def exist(self, username, password):
        temp = self.locate(username)
        return temp != None and temp.password == password 


    def remove(self, username):
        curr_node = self.root

        last = len(username)-1
        for i in range(0, last):
            curr_node = curr_node.children[username[i]]
        
        if len(curr_node.children[username[last]].children) == 0:
            curr_node.children.pop(username[last])
        else:
            curr_node.children[username[last]].data = None



    # def print(self):
    #     self._print(self.root)


    # def _print(self, curr_node: Node):
    #     if curr_node.data != None:
    #         print(curr_node.data.username)

    #     for child in curr_node.children:
    #         self._print(curr_node.children[child])


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


# tree.remove("Kiril")
# tree.remove("Iliyan")
# tree.print()