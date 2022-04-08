import visualise


class Transfer(object):
    def __init__(self, start, end: list, cond):  # 这里传入State类型
        self.start = start
        self.end = end
        self.cond = cond

    def __str__(self):
        return str(self.start) + "---" + str(self.cond) + "-->" + str(self.end)


class FA(object):
    def __init__(self):
        self.states = []
        self.trans = []
        self.startstates = []
        self.endstates = []
        self.inputs = []

    # 构造 NFA
    def construct(self, ipt):
        self.addstate(ipt[ipt.index('States:')+1])
        self.addinput(ipt[ipt.index('Inputs:')+1])
        self.addstartstate(ipt[ipt.index('StartState:')+1])
        self.addendstate(ipt[ipt.index('EndState:')+1])
        self.addtrans(ipt[ipt.index('Transfer:')+1:])

    def addstate(self, states):
        states = states.split(' ')
        for state in states:
            self.states.append([state])

    def addtrans(self, transList):  # 传入Transfer类型
        splt = [i for i, x in enumerate(transList) if x == '-']
        for i in range(len(splt)-1):
            transfer = transList[splt[i]+1:splt[i+1]]
            start = transfer[0]
            for i in range(1, len(transfer)):
                tmp = transfer[i].split('-')
                cond = tmp[0]
                end = tmp[1:]
                self.trans.append(Transfer(start, end, cond))

    def addstartstate(self, start):
        self.startstates.append([start])

    def addendstate(self, end):
        self.endstates = end.split(' ')

    def addinput(self, inputs):
        self.inputs = inputs.split(' ')

    def __str__(self):
        s = ""
        s += '开始状态:\n'+str(self.startstates[0][0])+'\n'
        s += '接收状态:\n'+str(self.endstates).replace('\'', '')+'\n'
        s += '输入字符:\n'+str(self.inputs).replace('\'', '')+'\n'
        s += '状态转移:\n'
        for i in self.trans:
            s += str(i).replace('\'', '') + "\n"
        return s


def toDFA(nfa: FA) -> FA:
    # DFA 的 初始状态和输入与 NFA 相同
    dfa = FA()
    dfa.startstates = nfa.startstates
    dfa.inputs = nfa.inputs
    tmp = dfa.startstates.copy()
    # 每次更新 tmp，直到 tmp 不再变化（与 DFA 的 states 相同）
    index = 0
    while tmp != dfa.states:
        dfa.states = tmp.copy()
        state = tmp[index]
        # 对每个state，求对于所有输入符ipt的状态转移 nfa.δ(state,ipt)
        for ipt in dfa.inputs:
            end = []
            # nfa.δ(state,ipt) = state中每一个状态 element 的转移 δ(element,ipt) 的并集
            for element in state:
                sub_end = [t.end for _, t in enumerate(nfa.trans)
                           if t.start == element and ipt == t.cond][0]
                for sub_element in sub_end:
                    # 不加入重复元素，同时将'NoS'替换为'Ø'
                    if sub_element not in end:
                        if sub_element == 'NoS':
                            end.append('Ø')
                        else:
                            end.append(sub_element)
            # 保证 state 内部按字典序排列，便于检验重复的state
            end = sorted(end)
            # 删除非空转移中的'Ø'
            while 'Ø' in end and len(end) != 1:
                del end[end.index('Ø')]
            # 加入DFA状态转移表
            dfa.trans.append(Transfer(state, end, ipt))
            # 若转移后状态不为空且不存在于 tmp 中，将状态加入 tmp
            if end not in tmp and 'Ø' not in end:
                tmp.append(end)
        # 继续遍历 tmp
        index += 1
    # 将包含NFA终态的状态加入DFA的终态中
    for state in dfa.states:
        for end in nfa.endstates:
            if end in state and state not in dfa.endstates:
                dfa.endstates.append(state)
    return dfa


def main():
    nfa_in = open('_nfa.in', 'r').read().split('\n')
    NFA = FA()
    NFA.construct(nfa_in)
    DFA = toDFA(NFA)
    print(DFA, end='')
    visualise.visualiseN(NFA)
    visualise.visualiseD(DFA)


if __name__ == '__main__':
    main()
