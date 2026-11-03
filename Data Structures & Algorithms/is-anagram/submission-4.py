class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1st way
        sSorted = sorted(s)
        tSorted = sorted(t)

        return True if sSorted == tSorted else False