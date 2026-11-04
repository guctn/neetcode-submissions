class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashtable - here we'll store the target - number as the key and the value will be the idx of the number 
        numIdx = {}

        for i in range(len(nums)):
            if nums[i] in numIdx:
                return [numIdx[nums[i]], i]
            else:
                numIdx[target-nums[i]] = i
        
        


        