import ast
import dis
import IPython
from graphviz import Digraph
from IPython.display import display, SVG

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
    # graph = Digraph(format="png")
    graph = Digraph(format="svg")
    tree = ast.parse(src)
    visit(tree, [], 0, graph)
    img = graph.render("test3")
    # return IPython.display.Image(img)
    return display(SVG(img))


src = """
a = 1
b = 1
x = a + b
print(x)
"""

show_ast(src)