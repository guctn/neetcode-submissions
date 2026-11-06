class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # approach 1: so we're basically going to iterate through the entire list and add it to a hashset, then after we'll iterate again and ask if the number + 1 is in the hashset, if it's we add one to the longest tmp variable, and if not we just go to the next number in the array
        if not nums:
            return 0 

        hashSet = set()

        for num in nums:
            if num not in hashSet:
                hashSet.add(num)
        
        longest = 1

        for num in nums:
            tempLong = 1
            add = 1
            if num - 1 not in hashSet:
                while num + add in hashSet:
                    tempLong += 1
                    add += 1
                longest = max(longest, tempLong)
        
        return longest

# Time: O(n²) -> because the second loop we point to one number in the array and the while can make it point to all the next values on the array (hashSet actually) but then when it gets to the end it can do the same thing but minus 1 times if the next number is just the curr + 1 -> so baiscally every call can call the same size again 
