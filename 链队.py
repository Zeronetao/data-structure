# 开发人：陶倩
# 开发时间： 2023/4/12  10:15

class LinkNode:  # 链队结点类
    def __init__(self, data=None):  # 构造方法
        self.data = data  # data域
        self.next = None  # next域


class LinkQueue:  # 链队类
    def __init__(self):  # 构造方法
        self.front = None  # 队头指针
        self.rear = None  # 队尾指针

    def empty(self):  # 判断队是否为空
        return self.front == None

    def push(self, e):  # 元素e进队
        s = LinkNode(e)
        if self.empty():
            self.front = self.rear = s
        else:
            self.rear.next = s
            self.rear = s

    def pop(self):  # 出队操作
        assert  not self.empty()
        if self.front == self.rear:
            e = self.front.data
            self.front = self.rear = None
        else:
            e = self.front.data
            self.front = self.front.next
        return e

    def gethead(self):  # 取队顶元素操作
        assert not self.empty()  # 检测空链队
        e = self.front.data  # 取首结点值
        return e


if __name__ == '__main__':
    print()
    print("  创建空链队qu")
    qu = LinkQueue()
    print("  qu：", "空" if qu.empty() else "不空")
    print()
    print("1,2,3入队列 ")
    for i in range(1 , 4):
        qu.push(i)
    for i in range(1, 4):
        x = qu.pop()
        print(x, end=" ")

#1,2出队显示队列
    for i in range(1, 4):
        qu.push(i)
    for i in range(1, 3):
        x = qu.pop()
    print()
    print("1,2出队显示队列：")
    print(qu.pop())

#4,5,6入队列显示队列
    for i in range(3, 7):
        qu.push(i)
    print("4,5,6入队显示队列：")
    for i in range(1, 4):
        x = qu.pop()
        print(x, end=" ")

#3,4出队显示队列
    for i in range(3, 7):
        qu.push(i)
    print()
    print("3,4出队显示队列：")
    for i in range(2, 5):
        qu.pop()
    for i in range(5, 7):
        x = qu.pop()
        print(x, end=" ")

#7,8,9入队列显示队列
    for i in range(5, 10):
        qu.push(i)
    print()
    print("7,8,9入队列显示队列：")
    for i in range(5, 10):
        x = qu.pop()
        print(x, end=" ")

#10入队列显示队列
    for i in range(5, 11):
        qu.push(i)
    print()
    print("7,8,9入队列显示队列：")
    for i in range(5, 11):
        x = qu.pop()
        print(x, end=" ")