# 开发人：陶倩
# 开发时间： 2023/5/16  14:41
#图的邻接表和邻接矩阵的实现和转换
import copy
MAXV=100							    #表示最多顶点个数
INF=0x3f3f3f3f				            #表示∞
class ArcNode:                          #边结点
    def __init__(self,adjv,w):          #构造方法
        self.adjvex=adjv                #邻接点
        self.weight=w                   #边的权值

class AdjGraph:				            #图邻接表类
    def __init__(self,n=0,e=0):         #构造方法
        self.adjlist=[]		            #邻接表数组
        self.vexs=[]			        #存放顶点信息，暂时未用
        self.n=n                        #顶点数
        self.e=e			            #边数
    def CreateAdjGraph(self,a,n,e):  #通过数组a、n和e建立图的邻接表
        self.n=n                        #置顶点数和边数
        self.e=e
        for i in range(n):				#检查边数组a中每个元素
            adi=[]                      #存放顶点i的邻接点
            for j in range(n):
                if a[i][j]!=0 and a[i][j]!=INF: #存在一条边
                    p=ArcNode(j,a[i][j])   #创建<j,a[i][j]>出边的结点p
                    adi.append(p)               #将结点p添加到adi中
            self.adjlist.append(adi)
    def DispAdjGraph(self):				        #输出图的邻接表
        for i in range(self.n):                 #遍历每一个顶点i
            print("  [%d]" %(i),end='')
            for p in self.adjlist[i]:
                print("->(%d,%d)" %(p.adjvex,p.weight),end='')
            print("->∧")

class MatGraph:				            #图邻接矩阵类
    def __init__(self,n=0,e=0):         #构造方法
        self.edges=[]		            #邻接矩阵数组
        self.vexs=[]		            #存放顶点信息，暂时未用
        self.n=n                        #顶点数
        self.e=e			            #边数
    def CreateMatGraph(self,a,n,e):  #通过数组a、n和e建立图的邻接矩阵
        self.n=n                        #置顶点数和边数
        self.e=e
        self.edges=copy.deepcopy(a)     #深拷贝
    def DispMatGraph(self):			    #输出图
        for i in range(self.n):
            for j in range(self.n):
                if self.edges[i][j]==INF:
                    print("%4s"%("∞"),end=' ')
                else:
                    print("%5d" %(self.edges[i][j]),end=' ')
            print()

def MatToAdj(g):  	                    #由图的邻接矩阵转换为邻接表
    G=AdjGraph(g.n,g.e)
    for i in range(g.n):				#检查数组g.edges中每个元素
        adi=[]                          #存放顶点i的邻接点
        for j in range(g.n):
            if g.edges[i][j]!=0 and g.edges[i][j]!=INF: #存在一条边
                p=ArcNode(j,g.edges[i][j])  #创建<j,g.edges[i][j]>出边的结点p
                adi.append(p)               #将结点p添加到adi中
        G.adjlist.append(adi)
    return G

def AdjToMat(G):  	                    #由图的邻接表转换为邻接矩阵
    g=MatGraph(G.n,G.e)
    g.edges=[[INF]*g.n for i in range(g.n)]
    for i in range(g.n):                #对角线置为0
        g.edges[i][i]=0
    for i in range(g.n):
        for p in G.adjlist[i]:
            g.edges[i][p.adjvex]=p.weight
    return g

MAXV = 100
visited = [0] * MAXV
def DFS1(G , v):
    print(v, end='')
    visited[v] = 1
    for p in G.adjlist[v]:
        w = p.adjvex
        if visited[w] == 0:
            DFS1(G,w)

if __name__ == '__main__':
    G=AdjGraph()
    n,e=5,5
    a=[ [0,8,INF,5,INF],
        [INF,0,3,INF,INF],
		[INF,INF,0,INF,6],
        [INF,INF,9,0,INF],
        [INF,INF,INF,INF,0]]
    print()
    print(" (1)由a创建邻接表G")
    G.CreateAdjGraph(a,n,e)
    print("  G:")
    G.DispAdjGraph()
    print(" (2)G->g")
    g=AdjToMat(G)
    print("  g:")
    g.DispMatGraph()
    print(" (3)g->G1")
    G1=MatToAdj(g)
    print("  G1:")
    G1.DispAdjGraph()
    print(" 邻接表深度优先搜索")
    DFS1(G, 0)