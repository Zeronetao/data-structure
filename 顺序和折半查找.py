# 开发人：陶倩
# 开发时间： 2023/5/30  14:51
import math  # 后面向上取整用


class StaticTableItem(object):  # 静态查找表的数据项
    def __init__(self, key):
        self.key = key


class StaticTable(object):
    def __init__(self):  # 初始化静态查找表
        self.items = []
        self.length = 0

    def Add(self):  # 写入数据
        while True:
            info = input("请输入要写入表的数字，依次输入一条，输入“终止”以结束输入：")
            if info != "终止":
                try:
                    info_int = int(info)  # 转int
                except ValueError:
                    print("请输入数字")
                    continue  # 无效数据，跳过此次循环
                item = StaticTableItem(info_int)  # 新建数据项
                self.items.append(item)  # 将数据项添加入静态查找表
                self.length += 1  # 长度加一
                print("第%d个数据%d写入成功。" % (self.length, item.key))
            else:
                break  # 终止

    def EmptyJudgement(self):  # 判定是否为空
        if self.length == 0:
            return True
        else:
            return False

    def Traversal(self):  # 遍历
        if not self.EmptyJudgement():  # 若非空直接进行列表遍历
            print("遍历结果", end="：")
            for i in range(self.length):
                print(self.items[i].key, end=" ")
            print()  # 换行用的
        else:
            print("查找表为空，需先写入数据")

    def SequenceSearch(self, key):
        if not self.EmptyJudgement():
            flag = -1  # 特殊标识，用于识别是否能查找到（没有-1这个索引，因此这里用的-1）
            for i in range(self.length):
                if self.items[i].key == key:
                    flag = i  # 如果查找到就修改索引
                    break
            return flag
        else:
            print("查找表为空，需先写入数据")

    def Sorted(self):  # 检查静态查找表是否完成排序
        flag = True
        for i in range(self.length - 1):
            if self.items[i] > self.items[i + 1]:  # 这个是升序检验，不满足升序条件会把标签赋False
                flag = False
        return flag

    def BinarySearch(self, key):
        if not self.EmptyJudgement():
            if self.Sorted:  # 如果排序了（没排序不能用来做折半查找）
                low = 0
                high = self.length - 1
                while low <= high:
                    mid = math.ceil((low + high) / 2)  # 向上取整
                    if key == self.items[mid].key:  # 如果相等直接返回
                        return mid
                    elif key < self.items[mid].key:  # 如果大于
                        high = mid + 1  # 加一是为了避免漏掉一些东西
                    elif key > self.items[mid].key:
                        high = mid - 1  # 减一是为了尽量减少运行成本
                return False  # 找不到返回False
            else:
                info = input("该表尚不属于排序后表，无法使用折半查找")
        else:
            print("查找表为空，需先写入数据")

    def Choice(self):
        self.__init__()
        while True:
            info = input("请选择操作（写入数据，遍历，顺序查找，折半查找，是否为空）或输入“终止”以结束：")
            if info == "写入数据":
                self.Add()
            elif info == "遍历":
                self.Traversal()
            elif info == "顺序查找":
                try:
                    key = int(input("请输入要查找的关键字："))
                    flag = self.SequenceSearch(key)
                    if flag != -1:
                        print("关键字%d位于索引为%d的位置" % (key, flag))
                    else:
                        print("关键字不存在")
                except ValueError:
                    print("请输入数字")
            elif info == "折半查找":
                try:
                    key = int(input("请输入要查找的关键字："))
                    flag = self.BinarySearch(key)
                    if flag != -1:
                        print("关键字%d位于索引为%d的位置" % (key, flag))
                    else:
                        print("关键字不存在")
                except ValueError:
                    print("请输入数字")
            elif info == "是否为空":
                if self.EmptyJudgement():
                    print("确实为空")
                else:
                    print("不为空")
            elif info == "终止":
                print("程序已终止")
                break
            else:
                print("无效指令")


if __name__ == "__main__":
    static_table = StaticTable()
    static_table.Choice()