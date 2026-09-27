class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # nums = [2,1,1,4,4,4]
        # {2: 1, 1: 2, 3: 4} -> then we'll iterate through the items and store the number in 
        # another list and the frequency will be its index 
        # [0, 2, 1, 0, 3, 0] -> iterate beginning by the end until we get k values

        dic = {}
        for num in nums:
            dic[num] = 1 + dic.get(num, 0)

        ordemNums = [[] for i in range(len(nums) + 1)]
        for key, value in dic.items():
            ordemNums[value].append(key)

        res = []
        for i in range(len(ordemNums) - 1, 0, -1): 
            for num in ordemNums[i]:
                res.append(num)
                if len(res) == k:
                    return res

        return res
            



