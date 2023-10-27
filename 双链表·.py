class DLinkNode:                    	#双链表结点类
  def __init__(self,data=None):     	#构造方法
    self.data=data                  	#data属性
    self.next=None                  	#next属性
    self.prior=None                 	#prior属性

class DLinkList:                    	#双链表类
    def __init__(self):               	#构造方法
        self.dhead=DLinkNode()          	#头结点dhead
        self.dhead.next=None
        self.dhead.prior=None
  #基本运算算法

    def CreateListF(self, a):  # 头插法：由数组a整体建立双链表
        for i in range(0, len(a)):  # 循环建立数据结点s
            s = DLinkNode(a[i])  # 新建存放a[i]元素的结点s，将其插入到表头
            s.next = self.dhead.next  # 修改s结点的next成员
            if self.dhead.next != None:  # 修改头结点的非空后继结点的prior
                self.dhead.next.prior = s
            self.dhead.next = s  # 修改头结点的next
            s.prior = self.dhead  # 修改s结点的prior

    def CreateListR(self, a):  # 尾插法：由数组a整体建立双链表
        t = self.dhead  # t始终指向尾结点,开始时指向头结点
        for i in range(0, len(a)):  # 循环建立数据结点s
            s = DLinkNode(a[i])  # 新建存放a[i]元素的结点s
            t.next = s  # 将s结点插入t结点之后
            s.prior = t
            t = s
        t.next = None  # 将尾结点的next成员置为None



    def Delx(L,x):
        p = L.dhead.next
        while p != None and p.data != x:
            p = p.next
        if p != None:
            if p.next != None :
                p.prior.next = p.next

                p.next.prior = p.prior

