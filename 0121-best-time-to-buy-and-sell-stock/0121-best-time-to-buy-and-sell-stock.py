class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # x=min(prices)
        # b=0
        # for i in range(len(prices)):
        #     if prices[i]==x:
        #         b=1
        #     if b==1 and prices[i] == max(prices[i:]):
        #         return max(prices[i:])-x
        # return x
        x=0
        y=1
        p=0
        while y<len(prices):
            cp=prices[y]-prices[x]
            if prices[x]<prices[y]:
                p=max(cp,p)
            else:
                x=y
            y+=1
        return p