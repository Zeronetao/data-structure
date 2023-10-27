# 开发人：陶倩
# 开发时间： 2023/4/12  11:00

# 中缀表达式 --->  后缀表达式
# 1 + ((2+3)*4) - 5 ---->  1 2 3 + 4 * + 5 -

class ArrayStack2:
    def __init__(self, masSize):
        self.maxsize = masSize
        self.stack = []
        self.top = -1

    # 判断栈是不是 满的
    def isFull(self):
        return self.top == self.maxsize - 1

    # 判断栈是不是空的
    def isEmpty(self):
        return self.top == -1

    # 将数据压入栈中
    def push(self, value):
        if self.isFull():
            print("栈已经满了！")
            return
        self.top = self.top + 1
        self.stack.append(value)

    # 将栈中的数据进行删除
    def pop(self):
        if self.isEmpty():
            print("栈已经是空的了，没法执行出栈操作!")
            return
        value = self.stack.pop()
        self.top = self.top - 1
        return value

    # 显示栈的内容，需要先从栈顶显示数据
    def showStack(self):
        if self.isEmpty():
            print("栈已经是空的了，没法执行显示操作!")
            return
        i = self.top
        while i > -1:
            print("栈中存在的数据：", self.stack[i])
            i = i - 1

    # 返回运算法的优先级  有程序员决定  优先级使用数字来表示，数字越大优先级越高
    def priority(self, oper):
        if (oper == "*" or oper == "/"):
            return 1
        elif (oper == "+" or oper == "-"):
            return 0
        else:
            return -1

    # 判断是不是一个运算法
    def isOper(self, val):
        return val == "*" or val == "/" or val == "+" or val == "-"

    def isyunsuan(self, val):
        return val == "(" or val == ")"

    # 进行计算
    def cal(self, num1, num2, oper):
        if oper == "+":
            return num1 + num2
        elif oper == "-":
            return num2 - num1  # 注意顺序
        elif oper == "*":
            return num1 * num2
        elif oper == "/":
            return num2 / num1

    # 只返回最后的一个元素，但是并不是删除最后 一个元素
    def peek(self):
        return self.stack[self.top]


class Infixtohouzhui:
    def __init__(self, expression="1+((2+3)*4)-5"):
        self.expression = expression
        self.s1 = ArrayStack2(20)
        self.s2 = []  # 直接使用list比较好
        self.flag = 0
        self.index = 0
        self.data = 1
        self.keepnum = 0

    def change(self):
        while self.index <= len(self.expression) - 1:
            if self.s1.isOper(self.expression[self.index]) == False and self.s1.isyunsuan(
                    self.expression[self.index]) == False:
                self.keepnum = self.expression[self.index]
                while True:
                    if self.index + self.data <= len(self.expression) - 1:
                        if (self.s1.isOper(self.expression[self.index + self.data])) == False and self.s1.isyunsuan(
                                self.expression[self.index + self.data]) == False:
                            self.flag = 1
                            self.keepnum = self.keepnum + self.expression[self.index + self.data]
                            self.data = self.data + 1
                        else:
                            break
                    else:
                        break
                self.s2.append(self.keepnum)
                self.keepnum = ""
            elif self.expression[self.index] == "(":
                self.s1.push(self.expression[self.index])

            # 如果是有括号，就将s1中的运算符，压到s2中，知道遇到左括号为止
            elif (self.expression[self.index]) == ")":
                while (self.s1.peek()) != "(":
                    self.s2.append(self.s1.pop())
                self.s1.pop()  # 将s1中的左括号要删除掉
            else:
                # 当s1的栈顶运算符大于新来的运算符 将s1的栈顶运算符放到s2中，然后不停的比较
                while (self.s1.isEmpty() == False and self.s1.priority(self.s1.peek()) >= self.s1.priority(
                        self.expression[self.index])):
                    self.s2.append(self.s1.pop())
                self.s1.push(self.expression[self.index])
            if self.flag:
                self.index = self.index + self.data
                self.flag = 0
                self.data = 1
            else:
                self.index = self.index + 1

        while self.s1.isEmpty() == False:
            self.s2.append(self.s1.pop())
        return self.s2


if __name__ == '__main__':
    ll = Infixtohouzhui()
    print("表达式：1+((2+3)*4)-5")
    print("转化为后缀表达式：", end=" ")
    print(ll.change())
    print("result=%d"%(1+((2+3)*4)-5))







