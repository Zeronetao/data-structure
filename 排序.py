# 开发人：陶倩
# 开发时间： 2023/6/6  14:55
import time
import random
import copy

def InsertSort(R): 			 #对R[0..n-1]按递增有序进行直接插入排序
    for i in range(1,len(R)):		#从第2个元素即R[1]开始
        if R[i]<R[i-1]:     		#反序时
            tmp=R[i]				#取出无序区的第一个元素
            j=i-1;		#在有序区R[0..i-1]中从右向左找R[i]的插入位置
            while True:
                R[j+1] = R[j]    #将大于tmp的元素后移
                j-=1				#继续向前比较
                if j<0 or R[j]<=tmp: break  #若j<0或者R[j]<=tmp,退出循环
            R[j+1]=tmp				#在j+1处插入R[i]

def BinInsertSort(R):			    #对R[0..n-1]按递增有序进行折半插入排序
    for i in range(1,len(R)):
        if R[i]<R[i-1]:			    #反序时
            tmp=R[i]			    #将R[i]保存到tmp中
            low,high=0,i-1
            while low<=high:	#在R[low..high]中折半查找插入位置high+1
                mid=(low+high)//2   #取中间位置
                if tmp<R[mid]:
                    high=mid-1	    #插入点在左区间
                else:
                    low=mid+1				#插入点在右区间
            for j in range(i-1,high,-1):    #元素集中后移
               R[j+1] = R[j]
            R[high+1] = tmp					#插入原来的R[i]


def ShellSort(R):				    #对R[0..n-1]按递增有序进行希尔排序
    d=len(R)//2					    #增量置初值
    while d>0:
        for i in range(d,len(R)): #对相隔d位置的元素组采用直接插入排序
            tmp=R[i]
            j=i-d
            while j>=0 and R[j]>tmp:    #找到R[j]<=tmp为止
                R[j+d] = R[j]	  #对相隔d位置的元素组排序
                j = j - d
            R[j+d]=tmp
        d=d//2						    #递减增量

def SelectSort(R):
    for i in range (len(R)-1):
        minj = i
        for j in range(i+1,len(R)):
            if R[j] < R[minj]:
                minj = j
        if minj != i:
            R[i],R[minj] = R[minj],R[i]
        print("Pass", i + 1, ":", end=" ")  # 每次遍历后输出数组的当前状态
        for k in range(len(R)):
            print(arr[k], end=" ")
        print()


#主程序
a=[]
for i in range(20000):
    a.append(random.random()*10000)
b=copy.deepcopy(a)
t1=time.time()              #获取开始时间
InsertSort(b)
t2=time.time()              #获取结束时间
print()
print("  直接插入排序的时间: %ds" %(t2-t1))
b=copy.deepcopy(a)
t1=time.time()              #获取开始时间
BinInsertSort(b)
t2=time.time()              #获取结束时间
print("  折半插入排序的时间: %ds" %(t2-t1))
b=copy.deepcopy(a)
t1=time.time()              #获取开始时间
ShellSort(a)
t2=time.time()              #获取结束时间
print("  希尔排序的时间:     %ds" %(t2-t1))

arr = [49, 38, 65, 97, 13, 27, 49]
print("Initial Array:", arr)
print()
t1=time.time()
SelectSort(arr)
t2=time.time()
print("  简单选择排序的时间:     %ds" %(t2-t1))
print()
print("Sorted Array:", arr)
