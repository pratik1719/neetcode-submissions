class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        i=0
        while(i < len(nums)-2):
            j=i+1
            k=len(nums)-1
            while(j<k):
                s = nums[i]+nums[j]+nums[k]
                if s< 0:
                    j+=1
                elif s>0:
                    k-=1
                else:
                    if [nums[i],nums[j],nums[k]] not in res:
                        res.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
            i+=1
        return res                


                




    


            
        