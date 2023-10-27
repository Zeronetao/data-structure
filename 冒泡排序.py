# 开发人：陶倩
# 开发时间： 2023/6/6  15:03
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):   #遍历所有数组元素
        for j in range(0, n-i-1):  # 最后 i 个元素已经到位，遍历数组从0到n-i-1
            if arr[j] > arr[j+1]:    #如果找到的元素更大则交换
                  arr[j],arr[j+1] = arr[j+1],arr[j]
        print("Pass", i+1, ":", end=" ")  # 每次遍历后输出数组的当前状态
        for k in range(n):
            print(arr[k], end=" ")
        print()
# Example usage:
arr = [49, 38, 65, 97, 13, 27, 49]
print("Initial Array:", arr)
print()
bubble_sort(arr)
print()
print("Sorted Array:", arr)