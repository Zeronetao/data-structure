# 开发人：陶倩
# 开发时间： 2023/4/23  21:45
def find_max(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        mid = len(arr) // 2
        max1 = find_max(arr[:mid])
        max2 = find_max(arr[mid:])
        return max(max1, max2)

# 测试用例
if __name__ == "__main__":
    arr = input("请输入数组，每个元素用空格分隔：")
    arr = arr.split(" ")
    arr = [int(x) for x in arr]
    print(arr)
    print("数组中的最大元素:%d"%find_max(arr))  # 输出：9