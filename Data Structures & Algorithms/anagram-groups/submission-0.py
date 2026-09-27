class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # ["act","pots","tops","cat","stop","hat"]
        # [["hat"],["act", "cat"],["stop", "pots", "tops"]]
        # act -> hash{sorted(act)}: [act]
        # cat -> hash{sorted(cat)}: [act, cat]
        # but sorting is O(n logn)

        dic = {}
        for word in strs:  
            key = str(sorted(word))
            if key not in dic:
                dic[key] = [word]
            else:
                dic[key].append(word)
        return list(dic.values())

 # act                | pots
 # ACT not in dic     | POTS not in dic
 # dic = {ACT: [act]} | dic = {ACT: [act], POTS: [pots]}
 # 
 # tops                                     | cat
 # POTS in dic                              | ACT in dic
 # dic = {ACT: [act], POTS: [pots, tops]} | dic = {ACT: [act, cat], POTS: [pots, tops]} 
