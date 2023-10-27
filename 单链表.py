class LinkNode:  # 单链表结点类
    def __init__(self, data=None):  # 构造函数
        self.data = data  # data属性
        self.next = None  # next属性


class LinkList:  # 单链表类
    def __init__(self):  # 构造函数
        self.head = LinkNode()  # 头结点head
        self.head.next = None

    def CreateListF(self, a):  # 头插法：由数组a整体建立单链表
        for i in range(0, len(a)):  # 循环建立数据结点s
            s = LinkNode(a[i])  # 新建存放a[i]元素的结点s
            s.next = self.head.next  # 将s结点插入到开始结点之前,头结点之后
            self.head.next = s
        #头插法建立的单链表中数据结点的次序与a列表中的次序正好相反


    def CreateListR(self, a):  # 尾插法：由数组a整体建立单链表
        t = self.head  # t始终指向尾结点,开始时指向头结点
        for i in range(0, len(a)):  # 循环建立数据结点s
            s = LinkNode(a[i]);  # 新建存放a[i]元素的结点s
            t.next = s  # 将s结点插入t结点之后
            t = s
        t.next = None  # 将尾结点的next成员置为null
        # 尾插法建立的单链表中数据结点的次序与a数组中的次序正好相同


    def geti(self, i):  # 返回序号为i的结点,
        # 查找序号为i（0≤i≤n-1，n为单链表中数据结点个数）的结点

        p = self.head
        j = -1
        while (j < i and p is not None):
            j += 1
            p = p.next
        return p

    def Add(self, e):  # 在线性表的末尾添加一个元素e
        s = LinkNode(e)  # 新建结点s
        p = self.head
        while p.next is not None:  # 查找尾结点p
            p = p.next
        p.next = s;  # 在尾结点之后插入结点s

    def getsize(self):  # 返回长度
        p = self.head
        cnt = 0
        while p.next is not None:  # 找到尾结点为止
            cnt += 1
            p = p.next
        return cnt


    def setsize(self, nsize):  # 设置新长度为nsize(<size)
        len = self.getsize()
        assert nsize < len  # 规定只能减小长度
        if (nsize == len): return;
        p = self.geti(nsize - 1);  # 找到序号为nsize-1的结点p
        assert p is not None  # p不为空的检测
        p.next = None;  # 将结点p置为尾结点

    def __getitem__(self, i):  # 求序号为i的元素
        assert i >= 0  # 检测参数i正确性的断言
        p = self.geti(i)
        assert p is not None  # p不为空的检测
        return p.data

    def __setitem__(self, i, e):  # 设置序号为i的元素,设置线性表中序号为i的元素
        assert i >= 0  # 检测参数i正确性的断言
        p = self.geti(i)
        assert p is not None  # p不为空的检测
        p.data = e

    def GetNo(self, e):  # 查找第一个为e的元素的序号
        j = 0
        p = self.head.next
        while p is not None and p.data != e:
            j += 1  # 查找元素e
            p = p.next
        if p is None:
            return -1  # 未找到时返回-1
        else:
            return j  # 找到后返回其序号

# 在线性表中序号i位置插入元素e
    def Insert(self, i, e):
        assert i >= 0  # 检测参数i正确性的断言
        s = LinkNode(e)  # 建立新结点s
        p = self.geti(i - 1)  # 找到序号为i-1的结点p
        assert p is not None  # p不为空的检测
        s.next = p.next  # 在p结点后面插入s结点
        p.next = s

    # 在线性表中删除序号i位置的元素
    def Delete(self, i):
        assert i >= 0  # 检测参数i正确性的断言
        p = self.geti(i - 1)  # 找到序号为i-1的结点p
        assert p != None and p.next != None  # p和p.next不为空的检测
        p.next = p.next.next

    def display(self):  # 输出线性表
        p = self.head.next
        while p is not None:
            print(p.data, end=' ')
            p = p.next;
        print()


# ----------------------------------
if __name__ == '__main__':
    L = LinkList()
    print()
    print("  建立空单链表L")
    a = [1, 2, 3, 4, 5, 6]
    print("  1-6创建L")
    L.CreateListR(a)
    print("  L[长度=%d]: " % (L.getsize()), end=''), L.display()
    print("  插入6-11")
    for i in range(6, 11):
        L.Add(i)
    print("  L[长度=%d]: " % (L.getsize()), end=''), L.display()
    print("  序号为2的元素=%d" % (L[2]))
    print("  设置序号为2的元素为20")
    L[2] = 20
    print("  L[长度=%d]: " % (L.getsize()), end=''), L.display()
    x = 6
    print("  第一个值为%d的元素序号=%d" % (x, L.GetNo(x)))

    y = 2
    print(" 返回序号为%d的节点=%s" % (y, L.geti(y)))
    print(" 返回序号为%d的节点=%d" % (y, L.__getitem__(y)))