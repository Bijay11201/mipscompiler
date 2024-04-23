__author__ = "dd"
__filename__ = "dot.py"
__description__ = "Generates graph of Parser Automaton."

import pydot
BLACK = "#000000"
SHAPE = "circle"

line_nonterminal = "Nonterminals,"
line_terminal = "Terminals,"
line_parsing = "Parsing"


def generate_LR_automata(filename):
    graph = pydot.Dot(graph_type="digraph")
    try:
        file = open("src/parser.out", "r")
    except:
        pass
    try:
        file = open("parser.out", "r")
    except:
        pass
    Lines = file.readlines()

    count = 0
    node = {}
    terminals = []
    nonterminals = []
    cc = 0
    header = 0
    for line in Lines:
        tokens = line.split()

        if len(tokens) > 0 and tokens[0] == line_terminal:
            header = 1
            continue

        if len(tokens) > 0 and tokens[0] == line_nonterminal:
            header = 2
            continue

        if len(tokens) > 0 and tokens[0] == line_parsing:
            header = 3
            continue

        if len(tokens) > 0 and header == 1:
            terminals.append(tokens[0])

        if len(tokens) > 0 and header == 2:
            nonterminals.append(tokens[0])

        if len(tokens) > 0 and tokens[0] == "state":
            count += 1
            name = "I" + tokens[len(tokens) - 1]
            n = pydot.Node(name, shape=SHAPE, color=BLACK)
            node[name] = n


    for i in node.values():
        graph.add_node(i)

    curr_state = ""
    for line in Lines:
        tokens = line.split()

        cc += 1

        if len(tokens) > 0 and tokens[0] == "state":
            curr_state = "I" + tokens[1]


        if len(tokens) > 0 and "shift and go to state" in line and tokens[0] != "!":
            col = BLACK

            graph.add_edge(
                pydot.Edge(
                    node[curr_state],
                    node["I" + tokens[len(tokens) - 1]],
                    label=tokens[0],
                    fontcolor=col,
                    fontsize="10.0",
                    color=col,
                )
            )

    print("Entered LR automata")
    print(filename)
    graph.write_raw(filename)
    print("Exit LR automata")