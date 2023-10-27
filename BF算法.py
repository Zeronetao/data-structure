# 开发人：陶倩
# 开发时间： 2023/4/18  14:38
MaxSize = 100             		#假设容量为100

class SqString:         		#顺序串类
    def __init__(self):   		#构造方法
        self.data=[None]*MaxSize	        #存放串中字符
        self.size=0   			#串中字符个数
    #串的基本运算算法

    def SubStr(self,i,j):	                	#求子串的运算算法
        s=SqString()                        	#新建一个空串
        assert i>=0 and i<self.size and j>0 and i+j<=self.size   #检测参数
        for k in range(i,i+j):            		#将data[i..i+j-1]-->s
            s.data[k-i]=self.data[k]
        s.size=j
        return s     				#返回新建的顺序串

def BF(s, t):
    i = 0
    j = 0
    k = 0
    flag1 = -1
    while (i < len(s) and j < len(t)):
        # 匹配成功
        if (i - k == j) and (j == len(t) - 1) and (s[i] == t[j]):
            flag1 = k
            break
        # s和t相等就继续向后匹配
        if s[i] == t[j]:
            i = i + 1
            j = j + 1
        # 不相等从k的位置开始匹配
        else:
            k = k + 1
            i = k
            j = 0
            # 假如s中所剩字符小于t中所剩字符
            if (len(s) - i) < len(t):
                flag1 = -1
                break
    return flag1


if __name__ == '__main__':
    s = input('输入目标串s：')
    t = input('输入模式串t：')
    flag = BF(s, t)
    if flag != -1:
        print('t在s的位置：', flag)
    else:
        print(flag, '匹配失败')