class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
                    
        countS, countT = {}, {}
        for i in range(len(s)):
            if s[i] in countS:
                countS[s[i]] = 1 + countS.get(s[i])
            else:
                countS[s[i]] = 1
            if t[i] in countT:
                countT[t[i]] = 1 + countT.get(t[i])
            else:
                countT[t[i]] = 1
        if countS == countT:
            return True
        return False
        