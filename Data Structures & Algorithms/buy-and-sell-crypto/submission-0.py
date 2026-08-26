class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        j=i+1
        n=len(prices)
        
        max_profit=0
        while(j<n):
            val=prices[j]-prices[i]
            if val <= 0:
                i=j
                j+=1
            else:
                if max_profit < val:
                    max_profit = val
                j+=1
        return max_profit


            

