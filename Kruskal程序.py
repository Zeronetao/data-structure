# 开发人：陶倩
# 开发时间： 2023/5/23  14:46
from operator import itemgetter,attrgetter
MAXV=100							    #表示最多顶点个数
INF=0x3f3f3f3f				            #表示∞
visited=[0]*MAXV                        #全局访问标志数组
class MatGraph:				            #图邻接矩阵类
    def __init__(self,n=0,e=0):         #构造方法
        self.n=n                        #顶点数
        self.e=e			            #边数
        self.edges=[[INF]*MAXV for i in range(MAXV)]   #邻接矩阵数组
        for i in range(MAXV):           #主对角线元素置为0
            self.edges[i][i]=0
    def CreateMatGraph(self):  	        #通过文件数据建立图的邻接矩阵
        f=open("gin.txt","r")
        tmp=f.readline().split()        #读取第1行
        self.n=int(tmp[0])
        self.e=int(tmp[1])
        while True:
            tmp=f.readline().split()
            if not tmp: break
            i,j,w=int(tmp[0]),int(tmp[1]),int(tmp[2])
            self.edges[i][j]=w
            self.edges[j][i]=w
        f.close()
    def DispMatGraph(self):			    #输出图
        for i in range(self.n):
            for j in range(self.n):
                if self.edges[i][j]==INF:
                    print("%4s"%("∞"),end=' ')
                else:
                    print("%5d" %(self.edges[i][j]),end=' ')
            print()

#基本的Kruskal算法
def Kruskal(g):        	                    #求最小生成树
    vset=[-1]*MAXV					            #建立数组vset
    sum=0                                       #存放权值和
    E=[]					                    #建立存放所有边的列表E
    for i in range(g.n):					    #由邻接矩阵g产生的边集数组E
        for j in range(i+1,g.n):		        #对于无向图仅考虑上三角部分的边
            if g.edges[i][j]!=0 and g.edges[i][j]!=INF:
                E.append([i,j,g.edges[i][j]])   #添加[i,j,w]元素
    E.sort(key=itemgetter(2))  	                #按权值递增排序
    for i in range(g.n):vset[i]=i		        #初始化辅助数组
    cnt=1									    #cnt表示当前构造生成树的第几条边,初值为1
    j=0									        #取E中边的下标,初值为0
    while cnt<g.n:								#生成的边数小于n时循环
        u1,v1=E[j][0],E[j][1]			        #取一条边的头尾顶点
        sn1=vset[u1]
        sn2=vset[v1]						    #分别得到两个顶点所属的集合编号
        if sn1!=sn2:							#两顶点属于不同的集合,加入不会构成回路
            print("   (%d,%d):%d" %(u1,v1,E[j][2]))    #输出最小生成树的边
            sum+=E[j][2]                        #累计权值和
            cnt+=1								#生成边数增1
            for i in range(g.n):			    #两个集合统一编号
                if vset[i]==sn2:				#集合编号为sn2的改为sn1
                    vset[i]=sn1
        j+=1								    #继续取E的下一条边
    print("   所有边的取值和=%d" %(sum))

#主程序
g=MatGraph()
g.CreateMatGraph()
print()
print("  图g:")
g.DispMatGraph()
v=0
print("  求出的一棵最小生成树");
Kruskal(g)