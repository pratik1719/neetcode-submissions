import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        p ="abcdefghijklmnop0123456789"
        s= s.lower()
        print(s)
        i=0
        j= len(s)-1
        while(i<j):
            if s[i] not in p:
                i+=1
            elif s[j] not in p:
                j-=1
            else:
                if s[i]!= s[j]:
                    return False
                else:
                    i+=1
                    j-=1
        return True


        