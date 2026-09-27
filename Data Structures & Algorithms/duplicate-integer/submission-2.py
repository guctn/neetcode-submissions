class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # [1, 2, 3, 3] -> True -> 3 
        # lenghtArray = 4 
        # set(array) -> {1, 2, 3} -> lengthSet = 3
        # lenghtArray != lengthSet -> True
        # [1, 2, 3, 4] -> False -> None

        numsSet = set(nums)
        if len(numsSet) == len(nums):
            return False
        else:
            return True

        