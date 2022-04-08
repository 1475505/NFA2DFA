> 开发环境：
> python == 3.9(需要`graphviz`库支持)

# 成员设定

| 姓名  | 学号         | 班级         | 分工           |
|-----|------------|------------|--------------|
| 刘亮  | 2020211318 | 2020211322 | 顶层设计         |
| 王祥龙 | 2020211415 | 2020211322 | 可视化设计        |
| 马紫薇 | 2020211392 | 2020211322 | 代码实现         |
| 金耘石 | 2019211328 | 2020211322 | 代码实现         |

# 结构设计

按照类似于邻接矩阵的图存储方式，存储状态机，设计类如下

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
> 可见，略为繁琐，选择从文件读取解析的方式
- 输出状态机：打印出所有转移函数

# 具体实现

程序的算法：通过BFS实现子集构造法

# 使用方式及效果

按照格式编辑"_nfa.in"文件（与`.py`同目录）：
```
nfa.in 格式：

StartState: #初态
p
EndState:   #终态
r
States:     #所有非终结符，用空格分隔
p q r
Inputs:     #所有非终结符，用空格分隔
a b
Transfer:   #状态转移表，格式为：
-           #各个状态以分隔符 "-"
p           #状态
a-p-q-r     #输入符1-转移状态1-转移状态2-...
b-NoS       #输入符2-转移状态1-转移状态2-...，若转移状态为空，则为NoS(No State).不可省略
-
q
a-r
b-q-r
-
r
a-p-r
b-NoS
-           #分隔符 "-" 作为文件结尾
```