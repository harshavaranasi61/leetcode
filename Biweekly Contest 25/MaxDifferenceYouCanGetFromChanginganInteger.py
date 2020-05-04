class Solution:
    def maxDiff(self, num: int) -> int:
        num1=list(str(num))
        num=list(str(num))
        f=''
        for i in range(len(num)):
            if(num[i]=='9'):
                continue
            else:
                f=num[i]
                num[i]='9'
                break
        for i in range(len(num)):
            if num[i]==f:
                num[i]='9'
        print(num,f)
        if(len(num1)==1):
            num1=['1']
        elif(len(num1)>1 and num1[0]=='1'):
            f=""
            for i in range(1,len(num1)):
                if num1[i] not in ['0','1']:
                    f=num1[i]
                    break
            for i in range(len(num1)):
                if(f==num1[i]):
                    num1[i]='0'
        else:
            f=num1[0]
            for i in range(len(num1)):
                if(num1[i]==f):
                    num1[i]='1'
        print(num1)
        num=int(''.join(num))
        num1=int(''.join(num1))
        return num-num1
