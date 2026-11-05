class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # approach -> we're going to iterate trough the array and increment the frequency of the values in a hastable | T: O(n) - S: O(n) | after that we can create an array with the input size plus 1 then we'll add each number to the index of its frequency, so if a number appears 4 times, this number must go to index 4 |T: O(n) - S: O(n)| after that we'll iterate through the new array and get the number from the end to start and add it to the result array and when if gets the lenght of k we stop and return |T: O(n) - S: O(k)

        frequencyHash = {}
        arrayLen = len(nums)
        numsOrder = [[] for i in range(arrayLen + 1)]
        res = []

        for num in nums:
            frequencyHash[num] = 1 + frequencyHash.get(num, 0)
        
        for num, idx in frequencyHash.items():
            numsOrder[idx].append(num)
        
        i = arrayLen
        while len(res) < k and i >= 0:
            for n in numsOrder[i]:
                res.append(n)
                if len(res) == k:
                    return res
            i -= 1 




            



