class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        
        res= []
        #{1:1, 2:2,3:3}
        while(k>0):
            max=0
            c=0
            for j in d.keys():
                if d[j] > max:
                    max= d[j]
                    c = j
            res.append(c)
            d[c]=0
            k-=1
        return res


        