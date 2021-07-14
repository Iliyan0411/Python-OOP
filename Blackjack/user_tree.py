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
        
        if i == len(name) - 1 and curr_node.children[name[i]].data == None:
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
        user = self.locate(username)
        return user != None and user.password == password 


    def remove(self, username):
        curr_node = self.root

        last = len(username) - 1
        for i in range(0, last):
            curr_node = curr_node.children[username[i]]
        
        if len(curr_node.children[username[last]].children) == 0:
            curr_node.children.pop(username[last])
        else:
            curr_node.children[username[last]].data = None


    def save(self, user: Player):
        if user.username != None:
            self._save(self.root, user, user.username, 0)


    def _save(self, curr_node: Node, user: Player, username, i):
        if i == len(username):
            curr_node.data = user
            return
        
        self._save(curr_node.children[username[i]], user, username, i+1)
