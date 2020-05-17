class Solution:
    def arrangeWords(self, text: str) -> str:
        
        def sort(s, n): 
            s.sort(key=len)
            
            i=0
            d1=[]
            for word in s:
                print(word)
                if i==0:
                    d=word[0].upper()
                    f=d+word[1:]
                    d1.append(f)
                    i+=1
                else:
                    d=word[0].lower()
                    f=d+word[1:]
                    d1.append(f)
            return " ".join(d1)
            
        text=list(text.split())
        return sort(text,len(text))
