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


    # def viz(self):
    #     viz_file = open("viz.dot", "w")
    #     viz_file.write("digraph G\n{\n")

    #     self._viz(self.root, viz_file)

    #     viz_file.write("\n}")
    #     viz_file.close()

    # def _viz(self, curr_node: Node, viz_file):
    #     for child in curr_node.children:
    #         viz_file.write('{0}[label="{1}"]\n'.format(id(curr_node), curr_node.key))
    #         viz_file.write('{0}[label="{1}"\n]'.format(id(curr_node.children[child]), curr_node.children[child].key))
    #         viz_file.write("{0}->{1}\n".format(id(curr_node), id(curr_node.children[child])))

    #     for child in curr_node.children:
    #         self._viz(curr_node.children[child], viz_file)



p1 = Player("Iliyan", 20, "dth")
p2 = Player("Ivan", 20, "dth")
p3 = Player("Niki", 20, "dth")
p4 = Player("Spasi", 20, "dth")
p5 = Player("Lusi", 20, "dth")
p6 = Player("Asen", 20, "dth")
p7 = Player("Spasimira", 20, "dth")

ut = UserTree()

ut.add(p1)
ut.add(p2)
ut.add(p3)
ut.add(p4)
ut.add(p5)
ut.add(p6)
ut.add(p7)

ut.viz()