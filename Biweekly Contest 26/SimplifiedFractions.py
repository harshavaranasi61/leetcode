class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        frac=[]
        den=[]
        if(n==2):
            return ["1/2"]
        j=3
        for i in range(2,n+1):
            frac.append("1/"+str(i))
            den.append(1/i)
        while(j<=n):
            i=2
            while(i<j):
                if i/j in den:
                    i+=1
                    continue
                else:
                    frac.append(str(i)+"/"+str(j))
                    den.append(i/j)
                    i+=1
            j+=1
        return frac
