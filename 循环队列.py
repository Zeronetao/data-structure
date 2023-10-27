# 开发人：陶倩
# 开发时间： 2023/4/12  11:14
MaxSize = 100
class CSqQueue:
    def __init__(self):
        self.data = [None] * MaxSize
        self.front = 0
        self.rear = 0

    def empty(self):
        return self.front == self.rear

    def push(self,e):
        assert (self.rear + 1) % MaxSize != self.front
        self.rear = (self.rear + 1) % MaxSize
        self.data[self.rear] = e

    def pop(self):
        assert not self.empty()
        self.front = (self.front + 1) % MaxSize
        return self.data[self.front]

    def gethead(self):
        assert not self.empty()
        head = (self.front + 1) % MaxSize
        return self.data[head]

    def size(self):
        return( (self.rear - self.front + MaxSize) % MaxSize)

    def pushk(qu,k,e):
        n = qu.size()
        if k < 1 or k > n+1:
            return False
        if k <= n:
            for i in range(1, n+1):
                if i == k:
                    qu.push(e)
                x = qu.pop()
                qu.push(x)
        else: qu.push(e)
        return True

    def popk(qu, k):
        n = qu.size()
        assert k >= 1 and k <= n
        for i in range(1,n + 1):
            x = qu.pop()
            if i != k: qu.push(x)
            else: e = x
        return e

if __name__ == '__main__':
    print()
    print("创建空链队qu")
    qu = CSqQueue()
    print("qu：", "空" if qu.empty() else "不空")
    print()
    print("1,2,3,4入队列:")

    qu.push(1)
    qu.push(2)
    qu.push(3)
    qu.push(4)
    for i in range(0,4):
        print(qu.pop(), end=" ")
    qu.push(1)
    qu.push(2)
    qu.push(3)
    qu.push(4)

    print()
    print("1,2出队列:")
    for i in range(1,3):
        print(qu.popk(3), end=" ")
    print()
    print("当前队列的个数:", end=" ")
    print(qu.size())

    print()
    print(qu.pushk(3,21), end=" ")
    print("当前队列的个数:", end=" ")
    print(qu.size())
    for i in range(1,5):
        print(qu.pop(), end=" ")