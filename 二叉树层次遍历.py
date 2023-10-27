# 开发人：陶倩
# 开发时间： 2023/5/9  14:44
from collections import deque  # 引用双端队列deque


class BTNode:  # 二叉链中结点类
    def __init__(self, d=None):  # 构造方法
        self.data = d  # 结点值
        self.lchild = None  # 左孩子指针
        self.rchild = None  # 右孩子指针


class BTree:  # 二叉树类
    def __init__(self, d=None):  # 构造方法
        self.b = None  # 根结点指针

    def SetRoot(self, r):  # 设置根结点为r
        self.b = r

    def DispBTree(self):  # 返回二叉链的括号表示串
        return self._DispBTree1(self.b)

    def _DispBTree1(self, t):  # 被DispBTree方法调用
        if t == None:  # 空树返回空串
            return ""
        else:
            bstr = t.data  # 输出根结点值
            if t.lchild != None or t.rchild != None:
                bstr += "("  # 有孩子结点时输出"("
                bstr += self._DispBTree1(t.lchild)  # 递归输出左子树
                if t.rchild != None:
                    bstr += ","  # 有右孩子结点时输出","
                bstr += self._DispBTree1(t.rchild)  # 递归输出右子树
                bstr += ")"  # 输出")"
            return bstr


def LevelOrder(bt):  # 层次遍历的算法
    qu = deque()
    qu.append(bt.b)
    while len (qu) > 0:
        p = qu.popleft()
        print(p.data, end=" ")
        if p.lchild != None:
            qu.append(p.lchild)
        if p.rchild != None:
            qu.append(p.rchild)

if __name__ == '__main__':
    b = BTNode('A')  # 建立各个结点
    p1 = BTNode('B')
    p2 = BTNode('C')
    p3 = BTNode('D')
    p4 = BTNode('E')
    p5 = BTNode('F')
    p6 = BTNode('G')
    b.lchild = p1  # 建立结点之间的关系
    b.rchild = p2
    p1.lchild = p3
    p3.rchild = p6
    p2.lchild = p4
    p2.rchild = p5
    bt = BTree()
    bt.SetRoot(b)
    print("bt:", end=' ');
    print(bt.DispBTree())
print("层次序列:", end=' ');
LevelOrder(bt);
print()
