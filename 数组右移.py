# 开发人：陶倩
# 开发时间： 2023/4/18  15:02
def rotate_array(nums, m):
    n = len(nums)
    m = m % n
    # 翻转整个数组
    reverse(nums, 0, n - 1)
    # 翻转前m个元素
    reverse(nums, 0, m - 1)
    # 翻转剩下的n-m个元素
    reverse(nums, m, n - 1)

def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1

if __name__ == "__main__":
    nums = [1,2,3,4,5,6]
    m = int(input("右移m位："))
    rotate_array(nums, m)
    i = 0
    while i < len(nums):
        print("%d"%nums[i], end=" ")
        i+=1