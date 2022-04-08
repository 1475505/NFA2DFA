from graphviz import Digraph


def visualise(DFA):
    f = Digraph('finite_state_machine', filename='fsm.gv')

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
