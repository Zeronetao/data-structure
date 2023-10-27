# 开发人：陶倩
# 开发时间： 2023/4/4  14:35
class SqStack:
    def __init__(self):  # 构造函数
        self.data = []  # 存放栈中元素，初始为空
        self.__mindata = []  # 存放min栈中元素，初始为空

    def empty(self):  # 判断栈是否为空
        if len(self.data) == 0:
            return True
        return False


    def __minempty(self):  # 判断min栈是否空
        return len(self.__mindata) == 0

    def __minpush(self, e):  # 元素进min栈
        self.__mindata.append(e)

    def __minpop(self):  # 元素出min栈
        assert not self.__minempty()  # 检测min栈为空的异常
        return self.__mindata.pop()

    def __mingettop(self):  # 取min栈栈顶元素
        assert not self.__minempty()  # 检测min栈为空的异常
        return self.__mindata[-1]

    def Getmin(self):  # 获取栈中最小元素
        assert not self.empty()  # 检测主栈为空的异常
        return self.__mindata[-1]  # 返回min栈顶元素即主栈最小元素

    # 元素e进栈
    def push(self, e):
        if self.empty() or e <= self.Getmin():
            self.__mindata.append(e)  # 栈空或者x<=min栈顶元素时进min栈
        self.data.append(e)  # 将x进主栈

    # 元素出栈
    def pop(self):  # 元素出栈
        assert not self.empty()  # 检测主栈为空的异常
        x = self.data.pop()  # 从主栈出栈x
        if x == self.__mingettop():  # 若栈顶元素为最小元素
            self.__minpop()  # min栈出栈一次
        return x

    def gettop(self):  # 取栈顶元素
        assert not self.empty()  # 检测栈为空
        return self.data[len(self.data) - 1]


##--------------------------
if __name__ == '__main__':
    print()
    print("  创建空顺序栈st")
    st = SqStack()
    print("  st：", "空" if st.empty() else "不空")
    print("  进栈1-4")
    st.push(1)
    st.push(2)
    st.push(3)
    st.push(4)
    print("  st：", "空" if st.empty() else "不空")
    print("  出栈顺序:", end=' ')
    while not st.empty():
        print(st.pop(), end=' ')
    print()
    print("  st：", "空" if st.empty() else "不空")
    print()
