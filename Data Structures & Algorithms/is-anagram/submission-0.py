class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict = {}
        for i in s:
            if i not in dict:
                dict[i]=0
            dict[i] +=1
        for j in t:
            if j not in dict.keys():
                return False
            dict[j]-=1
        for i in dict.keys():
            if dict[i] !=0:
                return False
        return True       