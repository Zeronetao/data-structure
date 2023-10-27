# 开发人：陶倩
# 开发时间： 2023/4/25  15:11
from collections import deque


class BTNode:  # 二叉链中结点类
    def __init__(self, d=None):  # 构造方法
        self.data = d  # 结点值
        self.lchild = None  # 左孩子指针
        self.rchild = None  # 右孩子指针


class BTree:  # 二叉树类
    def __init__(self):  # 构造方法
        self.b = None  # 根结点指针

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

    def FindNode(self, x):  # 查找值为x的结点算法
        return self._FindNode1(self.b, x)

    def _FindNode1(self, t, x):  # 被FindNode方法调用
        if t == None:
            return None  # t为空时返回null
        elif t.data == x:
            return t  # t所指结点值为x时返回t
        else:
            p = self._FindNode1(t.lchild, x)  # 在左子树中查找
            if p != None:
                return p  # 在左子树中找到p结点，返回p
            else:
                return self._FindNode1(t.rchild, x)  # 返回在右子树中查找结果


def PreOrder(bt):  # 先序遍历的递归算法
    _PreOrder(bt.b)


def _PreOrder(t):  # 被PreOrder方法调用
    if t != None:
        print(t.data, end=' ')  # 访问根结点
        _PreOrder(t.lchild)  # 先序遍历左子树
        _PreOrder(t.rchild)  # 先序遍历右子树


# 中序遍历的递归算法
def InOrder(bt):
    _InOrder(bt.b)


def _InOrder(t):  # 被PreOrder方法调用
    if t != None:
        _InOrder(t.lchild)  # 中序遍历左子树
        print(t.data, end=' ')  # 访问根结点
        _InOrder(t.rchild)  # 中序遍历右子树


# 后序遍历的递归算法
def PostOrder(bt):
    _PostOrder(bt.b)


def _PostOrder(t):  # 被PreOrder方法调用
    if t != None:
        _PostOrder(t.lchild)  # 后序遍历左子树
        _PostOrder(t.rchild)  # 后序遍历右子树
        print(t.data, end=' ')  # 访问根结点

def CreateBTree2(posts, ins):  # 由后序序列posts和中序序列ins构造二叉链
    bt = BTree()
    bt.b = _CreateBTree2(posts, 0, ins, 0, len(posts))
    return bt


def _CreateBTree2(posts, i, ins, j, n):
    if n <= 0:
        return None
    d = posts[i + n - 1]  # 取后序序列尾元素d
    t = BTNode(d)  # 创建根结点(结点值为d)
    p = ins.index(d)  # 在ins中找到根结点的索引
    k = p - j  # 确定左子树中结点个数k
    t.lchild = _CreateBTree2(posts, i, ins, j, k)  # 递归构造左子树
    t.rchild = _CreateBTree2(posts, i + k, ins, p + 1, n - k - 1)  # 递归构造右子树
    return t

def NodeCount4(bt):
    return _NodeCount4(bt.b)

def _NodeCount4(t):
    if t == None:
        return 0
    else:
        return _NodeCount4(t.lchild)+_NodeCount4(t.rchild)+1

def DispleafCount(bt):
    return _DispleafCount(bt.b)

def _DispleafCount(t):
    if t is None:
        return 0
    if t.lchild is None and t.rchild is None:
        return 1
    return _DispleafCount(t.lchild) + _DispleafCount(t.rchild)


def get_tree_height(bt):
    return _get_tree_height(bt.b)

def _get_tree_height(t):
    if not t:
        return 0
    return max(_get_tree_height(t.lchild), _get_tree_height(t.rchild)) + 1

# 主程序------
ins = ['D', 'G', 'B', 'A', 'E', 'C', 'F']
posts = ['G', 'D', 'B', 'E', 'F', 'C', 'A']
print()
print("  中序:", end=' ')
print(ins)
print("  后序:", end=' ')
print(posts)
print("  构造二叉树bt")
bt = BTree()
bt = CreateBTree2(posts, ins)
print("  bt:", end=' ')
print(bt.DispBTree())
x = 'X'
p = bt.FindNode(x)
if p != None:
    print("  bt中存在" + x)
else:
    print("  bt中不存在" + x)
print("  先序序列:", end=' ')
PreOrder(bt)
print()
print("  中序序列:", end=' ')
InOrder(bt)
print()
print("  后序序列:", end=' ')
PostOrder(bt)
print()
a = NodeCount4(bt)
print("  结点总数：", a)
b = DispleafCount(bt)
print("  叶子结点总数：", b)
c = get_tree_height(bt)
print("  树高：", c)
