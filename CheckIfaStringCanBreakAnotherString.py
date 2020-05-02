class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        h1=[0 for i in range(26)]
        for i in range(len(s1)):
            h1[ord(s1[i])-97]+=1
            h1[ord(s2[i])-97]-=1
        h=[]
        h2=[]
        for i in range(26):
            if(h1[i]==0):
                continue
            else:
                h.append(h1[i])
                h2.append(-1*h1[i])
        #print(h)
        for i in range(len(h)):
            if(h[i]>0):
                #print(h[i])
                for j in range(i+1,len(h)):
                    if(h[j]<0):
                        #print(h[j],h[i])
                        if(h[i]==(-1*h[j])):
                            h[i],h[j]=0,0
                            break
                        elif(h[i]>(-1*h[j])):
                            h[i]=h[i]+h[j]
                            h[j]=0
                            continue
                        else:
                            h[j]=h[j]+h[i]
                            h[i]=0     
                            break
                    else:
                        continue
                #print(h)
        #print(h)
        #print(h2)
        for i in range(len(h2)):
            if(h2[i]>0):
                #print(h2[i])
                for j in range(i+1,len(h2)):
                    if(h2[j]<0):
                        #print(h2[j],h2[i])
                        if(h2[i]==(-1*h2[j])):
                            h2[i],h2[j]=0,0
                            break
                        elif(h2[i]>(-1*h2[j])):
                            h2[i]=h2[i]+h2[j]
                            h2[j]=0
                            continue
                        else:
                            h2[j]=h2[j]+h2[i]
                            h2[i]=0
                            break
                
                    else:
                        continue
                #print(h2)
        
        #print(h2)
        flag,flag1=0,0
        for i in range(len(h)):
            if(h[i]>0):
                flag=1
                #print("harsha")
                break
        for j in range(len(h2)):
            
            if(h2[j]>0):
                flag1=1
                #print("vardhan")
                break
        if(flag==1 and flag1==1):
            return False
        return True
