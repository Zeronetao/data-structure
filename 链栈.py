# 开发人：陶倩
# 开发时间： 2023/4/4  14:54

class LinkNode:               	#单链表结点类
    def __init__(self, data=None):  	#构造方法
        self.data = data               	#data属性
        self.next = None               	#next属性

class LinkStack:                	#链栈类
    def __init__(self):           	#构造方法
        self.head = LinkNode()        	#头结点head
        self.head.next = None

    def empty(self):  # 判断栈是否为空
        if self.head.next == None:
            return True
        return False

    def push(self, e):  # 元素e进栈
        p = LinkNode(e)
        p.next = self.head.next
        self.head.next = p

    def pop(self):  # 元素出栈
        assert self.head.next != None  # 检测空栈的异常
        p = self.head.next
        self.head.next = p.next
        return p.data

    def gettop(self):  # 取栈顶元素
        assert self.head.next != None  # 检测空栈的异常
        return self.head.next.data



if __name__ == '__main__':
    print("创建空顺序栈st")
    st = LinkStack()
    while not st.empty():
        print(st.pop(), end=' ')

    print("进栈1-4")
    st.push(1)
    st.push(2)
    st.push(3)
    st.push(4)
    while not st.empty():
        print(st.pop(), end=' ')

    print()
    st.push(1)
    st.push(2)
    st.push(3)
    st.push(4)
    print("逆置后：")
    a = []
    while not st.empty():  # 将出栈的元素放到列表a中
        a.append(st.pop())
    for j in range(len(a)):  # 将列表a的所有元素进栈
        st.push(a[j])
    while not st.empty():
        print(st.pop(), end=' ')