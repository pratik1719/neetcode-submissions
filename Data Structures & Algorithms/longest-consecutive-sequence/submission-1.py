class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # a= []
        # for i in nums:
        #     if i not in a:
        #         a.append(i)
        
        # longest = 0

        # for i in a:
        #     if i-1 in a:
        #         continue
        #     p= i
        #     l=0
        #     while(p in a):
        #         l+=1
        #         p+=1
        #     if l >longest:
        #         longest= l
        # return longest
        # 
        if not nums:
            return 0
        nums = sorted(set(nums))
        longest = current = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                current += 1
                if current > longest:
                    longest = current
            else:
                current = 1
        return longest
            
        
        