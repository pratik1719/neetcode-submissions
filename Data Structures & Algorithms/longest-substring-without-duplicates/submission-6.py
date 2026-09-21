class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        j=0
        l=0
        max_l=0
        while(j<len(s)):
            if s[j] not in s[i:j]:
                l+=1
                if l > max_l:
                    max_l=l
                j+=1
            else:
                i=i+1
                l=l-1
        return max_l

                
            
            

            
            

            

            


            
                
                
            

        