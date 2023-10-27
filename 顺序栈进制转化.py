class Stack:  # 默认继承object
    def __init__(self):  # 初始为空列表
        self.items = []

    def pop(self):  # 将栈顶的元素移除(出栈)
        return self.items.pop(0)

    def push(self, item):  # 将元素放入栈里
        return self.items.insert(0, item)

    def peek(self):  # 查看栈顶的元素
        return self.items[0]

    def size(self):  # 查看栈的长度大小
        return len(self.items)

    def isEmpty(self):  # 判断是否为空栈
        return self.items == []


n = int(input())


def DivideBy2(n):
    remstack = Stack()

    while n > 0:
        rem = n % 2
        remstack.push(rem)  # 求余数
        n = n // 2  # 被整除

    b = ''
    while not remstack.isEmpty():
        b = b + str(remstack.pop())  # 将栈顶的元素拿出拼接

    return b


print(DivideBy2(n))