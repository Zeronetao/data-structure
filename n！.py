# 开发人：陶倩
# 开发时间： 2023/4/23  21:40
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        res = n * factorial(n-1)
        print("计算", n, "的阶乘：", n, "*", "factorial(", n-1, ") = ", res)
        return res

if __name__ == "__main__":
    factorial(5)