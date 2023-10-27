# 开发人：陶倩
# 开发时间： 2023/5/30  15:36
##################################
# 类名称：Element
# 类说明：数据元素类型
# 类释义：该类拥有带排序的关键字key
###################################
class Element(object):
    def __init__(self, key):
        self.key = key
##############################################################
# 类名称：HashTable
# 类说明：哈希表的顺序存储结构
# 类释义：该类拥有一个数据元素类型的列表data和data的长度length
##############################################################
class HashTable(object):
    #####################################
    # 初始化哈希表
    #####################################
    def __init__(self):
        self.data = []
        self.length = 0
    ########################
    # 创建哈希表，依据关键字个位构建哈希表
    ########################
    def CreateHashTableList(self):
        elements = []
        print("---------------------------------------------------")
        print(" 请输入数据后按回车键确认，若想结束输入请按“#”。 ")
        print("---------------------------------------------------")
        Elements = input("请输入元素：")
        while Elements != '#':
            elements.append(int(Elements))
            Elements = input("请输入元素：")
        print("现有关键字的数目为：", len(elements))
        self.length = int(input("请输入哈希表的长度："))
        if self.length >= len(elements):
            for i in range(self.length):
                self.data.append(None)
            for i in range(len(elements)):
                addr = elements[i] % 5
                if self.data[addr] is None:
                    self.data[addr] = Element(elements[i])
                else:
                    while self.data[addr] is not None:
                        addr = (addr + 1) % self.length
                    self.data[addr] = Element(elements[i])
            print("哈希表 HashTable 创建完成")
        else:
            print("哈希表的长度小于关键字的数目，无法创建该哈希表！")
            return
    ########################
    # 打印哈希表函数
    ########################
    def PrintHashTable(self):
        for i in range(len(self.data)):
            if self.data[i]:
                print(i, "--->", self.data[i].key)
            else:
                print(i, "--->", "   ")
    ###########################
    # 输出函数
    ###########################
    def PrintOut(self):
        print("范例：[12, 34, 56, 78, 90]  -> 10")
        self.CreateHashTableList()
        self.PrintHashTable()
if __name__ == '__main__':
    H = HashTable()
    H.PrintOut()