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
