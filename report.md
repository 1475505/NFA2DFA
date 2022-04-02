> 开发环境：

# 成员设定

| 姓名  | 学号         | 班级         | 分工           |
|-----|------------|------------|--------------|
| 刘亮  | 2020211318 | 2020211322 | 顶层设计         |
| 王祥龙 | 2020211415 | 2020211322 | 可视化设计        |
| 马紫薇 | 2020211392 | 2020211322 | 代码实现         |
| 金耘石 | 2019211328 | 2020211322 | 代码实现         |

# 结构设计

按照图的存储方式，存储状态机，设计类如下

- 状态：因为存在“子集”，采用列表
- 转移函数：`transfer`
- 状态机：状态和转移函数的集合


```python
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

```

## 设计思路

- 输入状态机：输入状态集合 ->  输入状态转移集合 -> 设置始末状态
- 输出状态机：打印出所有转移函数

# 具体实现

程序的算法：通过BFS实现子集构造法

# 问题解决

# 实现效果

程序的输入输出、运行截图。