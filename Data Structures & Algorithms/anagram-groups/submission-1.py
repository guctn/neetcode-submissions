class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # ["act","pots","tops","cat","stop","hat"]
        # [["hat"],["act", "cat"],["stop", "pots", "tops"]]
        # act -> hash{sorted(act)}: [act]
        # cat -> hash{sorted(cat)}: [act, cat]
        # but sorting is O(n logn)

        dic = {}
        for word in strs:               # O(n) -> n being the amount of strings
            key = ''.join(sorted(word))     # O(n log n)
            if key not in dic:
                dic[key] = [word]
            else:
                dic[key].append(word)
        return list(dic.values())

# Time Complexity: O(n log n) bc of sorted() function
# Space Complexity: O(n) -> we created a dictionary an also many string after sorting the str method idk how works