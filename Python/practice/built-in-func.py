# a = 1
# b = -1

# print(a)
# print(b)
# print(abs(a))
# print(abs(b))

# mylist = [True, True, True]
# x = all(mylist)
# print(x)

# mylist = (True, False, 0)
# x = all(mylist)
# print(x)


# mylist = [False, True, False]
# x = any(mylist)

# mytuple = (0, 1, False)
# y = any(mytuple)

# myset = {0, 1, 0}
# z = any(myset)

# print(x, y, z)

# mylist = []
# x = any(mylist)
# print(x)

# cat_name = 'tama'
# print(f"my cat name is {cat_name}")


# seed = 1

# def sample():
#     print(seed)
#     if seed == 1:
#         print("yes")
#     else:
#         print("no")
#         seed = 0

# sample()


# import dis

# dis.dis("a + b * c")

import ast
import dis
import IPython
from graphviz import Digraph
import circular

def visit(node, nodes, pindex, g):
    name = str(type(node).__name__)
    index = len(nodes)
    nodes.append(index)
    g.node(str(index), name)
    if index != pindex:
        g.edge(str(pindex), str(index))
    for n in ast.iter_child_nodes(node):
        visit(n, nodes, index, g)

def show_ast(src):
    graph = Digraph(format="png")
    tree = ast.parse(src)
    visit(tree, [], 0, graph)
    img = graph.render("test.png")
    return IPython.display.Image(img)


src="""
3 + 4
"""
show_ast(src)