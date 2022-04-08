from graphviz import Digraph


def visualiseD(DFA):
    f = Digraph('DFA', filename='DFA.gv')

    f.attr(rankdir='LR', size='8,5')

    f.attr('node', shape='doublecircle')
    for i in DFA.endstates:
        f.node(str(i).replace('\'', ''))

    f.attr('node', shape='circle')
    for i in DFA.trans:
        f.edge(str(i.start).replace('\'', ''), str(i.end).replace('\'', ''), label=str(i.cond))
    f.attr('node', shape='none')
    for i in DFA.startstates:
        f.edge('', str(i).replace('\'', ''))

    f.view()


def visualiseN(NFA):
    f = Digraph('NFA', filename='NFA.gv')

    f.attr(rankdir='LR', size='8,5')

    f.attr('node', shape='doublecircle')
    for i in NFA.endstates:
        f.node(str(i).replace('\'', ''))

    f.attr('node', shape='circle')
    for i in NFA.trans:
        for j in i.end:
            if(j != 'NoS'):
                f.edge(str(i.start).replace('\'', ''), str(j).replace('\'', ''), label=str(i.cond))
    f.attr('node', shape='none')
    for i in NFA.startstates:
        f.edge('', str(i[0]).replace('\'', ''))

    f.view()
