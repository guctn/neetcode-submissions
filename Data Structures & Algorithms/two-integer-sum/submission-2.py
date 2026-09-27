class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #[3,4,5,6] -> x + y = target (7)
        # target - nums[i] = 
        # 7 - 3 = 4     -> Time O(n)
        # 7 - 4 = 3
        # 7 - 5 = 2 
        # 7 - 6 = 1 
        # key  |  value -> Space O(n) 
        #   4  |    0
        #      | 
        dic = {}
        for i in range (len(nums)):
            if nums[i] in dic:
                return [dic.get(nums[i]), i]
            remainder = target - nums[i]
            if remainder not in dic:
                dic[remainder] = i

        # i = 1 | 4 | r = 3
        # dic = {4: 0, 3: 1}

# Time Complexity: O(n) -> iterate through the entire list (worst case) - some times i can not even get to the end
# Space Complexity: O(n) 


        