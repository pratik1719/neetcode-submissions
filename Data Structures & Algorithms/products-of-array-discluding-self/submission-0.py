class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p= 1
        peo = 1
        noz = 0
        out=[0]*len(nums)
        for i in nums:
           #[-1,1,2,0,1,2,3]
            if i == 0 and noz == 0:
                p = p*i
                noz +=1
            else:
                p = p*i
                peo = peo * i
        print(p)
        print(peo)
        
        if noz <=1:
            for i in range (0,len(nums)):
                if nums[i] == 0:
                    out[i]= peo
                else:
                    out[i]= p//(nums[i])
        else:
            out = nums*0
        return out

            

        