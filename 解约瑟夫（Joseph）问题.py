# 开发人：陶倩
# 开发时间： 2023/3/28  14:49
class Child:	        		#结点类型
    def __init__(self,no1):      	#构造方法
        self.no=no1                 	#编号no属性
        self.next=None              	#next属性

class Joseph:		    		#求解约瑟夫问题
    def __init__(self, n1, m1):       	#构造方法
        self.n=n1
        self.m=m1
        self.first=Child(1);            	#循环单链表首结点
        t=self.first
        for i in range(2,self.n+1):
            p=Child(i)			#建立一个编号为i的新结点p
            t.next=p			#将p结点链到末尾
            t=p
        t.next=self.first		    #构成一个首结点为first的循环单链表

    def Jsequence(self):  # 求约瑟夫序列
        for i in range(1, self.n + 1):  # 共出列n个小孩
            p = self.first  # 每次都从first开始
            j = 1
            while j < self.m - 1:  # 从first结点开始报数，报到第m-1个结点
                j += 1  # 报数递增
                p = p.next  # 移到下一个结点
            q = p.next  # q指向第m个结点
            print(q.no, end=' ')  # 该结点的小孩出列
            p.next = q.next  # 删除q结点
            self.first = p.next  # 从下一个结点重新开始
        print()

#---------------设计主程序--------------------

n = 6
m = 3
L = Joseph(n, m)
print("n=%d，m=%d的约瑟夫序列:" %(n, m))
L.Jsequence()
