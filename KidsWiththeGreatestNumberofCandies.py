class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        x=max(candies)
        c=[]
        for i in range(len(candies)):
            if(candies[i]+extraCandies>=x):
                c.append(True)
            else:
                c.append(False)
        return c