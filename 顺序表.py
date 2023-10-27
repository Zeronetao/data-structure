
#整数顺序表的实现
class SqList:
    def __init__(self):                         #构造函数
        self.initcapacity=5;                    #初始容量设置为10
        self.capacity=self.initcapacity         #容量设置为初始容量
        self.data=[None]*self.capacity          #设置顺序表的空间
        self.size=0                             #长度设置为0

    def resize(self, newcapacity):              #改变顺序表的容量为newcapacity
        assert newcapacity>=0                   #检测参数正确性的断言
        olddata=self.data
        self.data=[None]*newcapacity
        self.capacity=newcapacity
        for i in range(self.size):
            self.data[i]=olddata[i]

    def CreateList(self, a):                    #由数组a中元素整体建立顺序表
        for i in range(0,len(a)):
            if self.size==self.capacity:        #出现上溢出时
                self.resize(2*self.size);       #扩大容量
            self.data[self.size]=a[i]
            self.size+=1                        #添加后元素个数增加1

    def Add(self, e):                       #在线性表的末尾添加一个元素e
        if self.size==self.capacity:            #顺序表空间满时倍增容量
            self.resize(2*self.size)
        self.data[self.size]=e                  #添加元素e
        self.size+=1                            #长度增1

    def getsize(self):                          #返回长度
        return self.size

    def setsize(self, nsize):                   #设置新长度为nsize(<size)
        assert 0<=nsize<self.size               #规定只能减小长度
        self.size=nsize

    def __getitem__(self,i):                    #求序号为i的元素
        assert 0<=i<self.size                   #检测参数i正确性的断言
        return self.data[i]

    def __setitem__(self, i, x):                #设置序号为i的元素
        assert 0<=i<self.size                   #检测参数i正确性的断言
        self.data[i]=x

    def Insert(self, i, e):                     #在线性表中序号i位置插入元素e
        assert 0<=i<=self.size                  #检测参数i正确性的断言
        if self.size==self.capacity:            #满时倍增容量
            self.resize(2*self.size)
        for j in range(self.size,i-1,-1):       #将data[i]及后面元素后移一个位置
            self.data[j]=self.data[j-1]
        self.data[i]=e                          #插入元素e
        self.size+=1     #长度增1

#顺序表的删除运算
#在顺序表L中删除序号i的元素
#先用assert函数检测参数i正确性
#将data[i]后面元素前移一个位置
#长度减1
#检查容量不是初始容量，数据不足1/4，则容量减半

    def Delete(self, i):                        #在线性表中删除序号i的元素
        assert 0 <= i <= self.size-1
        for j in range(i,self.size-1):
            self.data[j]=self.data[j+1]
        self.size-=1
        if self.capacity>self.initcapacity and self.size<=self.capacity/4:
            self.resize(self.capacity//2)
    #顺序表按内容查找，查找第一个为e的元素的序号
#在顺序表L中查找与e相等的元素，若self.data[i]=e,则找到该元素，
#找到返回其序号i，若找不到，则返回-1

    def GetNo(self, e):
        i=0;
        while i<self.size and self.data[i]!=e:
            i+=1
        if (i>=self.size):
            return -1;
        else:
            return i;



    def display(self):                          #输出顺序表
        for i in range(0,self.size):
            print(self.data[i],end=' ')
        print()

#----------------------------------
if __name__ == '__main__':
    L=SqList()
    print()
    print("  建立空顺序表L，其容量=%d" %(L.capacity))
    a=[1,2,3,4,5,6]
    print("  1-6创建L")
    L.CreateList(a)
    print("  L[容量=%d,长度=%d]: " %(L.capacity,L.getsize()),end=''),L.display()
    print("  插入6-11")
    for i in range(6,11):
        L.Add(i)
    print("  L[容量=%d,长度=%d]: " %(L.capacity,L.getsize()),end=''),L.display()
    print("  序号为2的元素=%d" %(L[2]))
    print("  设置序号为2的元素为20")
    L[2]=20
    print("  L[容量=%d,长度=%d]: " %(L.capacity,L.getsize()),end=''),L.display()
    x=6
    print("  第一个值为%d的元素序号=%d" %(x,L.GetNo(x)))
