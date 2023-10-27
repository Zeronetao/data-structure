# coding=utf-8

"""
question:
在一个链表中，存在重复的节点，请删除该链表中重复的节点，重复节点只保留一个，返回链表头指针
例；
链表：1->2->3->3->3->4->4->5
处理后：1->2->3->4->5
"""


# 节点类
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# 根据列表元素创建一条链表
def list2link(items):
    if not items:
        return None

    header = Node(items[0])  # 头节点

    if len(items) == 1:
        return header

    tmp = header
    for item in items[1:-1]:
        new = Node(item)
        tmp.next, tmp = new, new
    tmp.next = Node(items[-1])  # 尾节点
    return header


# 将链表元素按序保存在列表中
def link2list(header):
    cur = header
    t = []
    while cur:
        t.append(cur.val)
        cur = cur.next
    return t


# 删除重复节点
def del_link_repeat(header):
    if not header:
        return None

    t = []  # 存放出现过的元素
    cur = header  # 当前节点指针
    pre = None  # 前一个节点指针

    # 遍历链表
    while cur:
        if cur.val not in t:
            t.append(cur.val)
            pre, cur = cur, cur.next  # 下一个节点
        else:
            pre.next, cur = cur.next, cur.next  # 删除节点

    return header


if __name__ == '__main__':
    l = [1, 2, 3, 3, 3, 4, 5]
    print("去重后：", end = " ")
    print(link2list(del_link_repeat(list2link(l))))
    pass