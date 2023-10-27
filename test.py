
#顺序查找
def SeqSearch1(R , k):
    n = len(R)
    i = 0
    while i < n and R[i] != k: i+=1
    if i >= n: return -1
    else: return i

#折半查找
def BinSearch1(R , k):
    n = len(R)
    low, high = 0, n-1
    flag = 0
    while low <= high:
        mid = (low + high)//2
        if k == R[mid]:
            x = mid
        if k < R[mid]:
            high = mid -1
        else:
            low = mid + 1
        flag += 1
    print(f"Number of comparisons is {flag}")
    return x


if __name__ == '__main__':
    r1 = [12 ,76 ,29 ,15 ,62 ,35 ,33 ,89 ,48 ,20]
    k1 = 35
    a = SeqSearch1(r1 , k1)
    print(f"keyword {k1} number is {a}")
    n1 = a + 1
    print(f"Number of comparisons is {n1}")
    r2 = [8 ,15 ,19 ,26 ,33 ,41 ,47 ,52 ,64 ,90]
    k2 = 41
    b = BinSearch1(r2 , k2)
    print(f"keyword {k2} number is {b}")
