class State(object):
    def __init__(self):
        self.state = []
    def __str__(self):
        return str(self.state)


class transfer(object):
    def __init__(self, start, end, cond):  # 这里传入State类型
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
    def addstate(self):
        pass
    def addtrans(self):#传入Transfer类型
        pass
    def addstartstate(self):
        pass
    def addendstate(self):
        pass
    def __str__(self):
        str = ""
        for i in self.trans:
            str += i.str + "\n"
        return str


def BFS():
    pass

def main():
    NFA = FA()
    NFA.addstate()
    NFA.addstartstate()
    NFA.addendstate()
    NFA.addtrans()
    # 不设计`get`和`set`方法，可以先得到列表再调用对应的构造函数，可以参考着实现一个
    DFA = FA()
    BFS()
    print(DFA)

if __name__ == '__main__':
    main()