class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1st way - Sorting approach

# Time: O(n log n) -> because every string was sorted and in python, this method uses the algorithm of Timsort (merge sort + insertion sort)
# Space: O(n) because the sorted method created new strings instead of doing in in-place

        # 2nd way - Hashtable approach
        sLetters = {}
        tLetters = {}

        for letter in s:
            sLetters[letter] = 1 + sLetters.get(letter, 0)
        
        for letter in t:
            tLetters[letter] = 1 + tLetters.get(letter, 0)

        for letter, number in sLetters.items():
            if letter not in tLetters: 
                return False    
            elif tLetters[letter] != sLetters[letter]:
                return False

        for letter, number in tLetters.items():
            if letter not in sLetters: 
                return False    
            elif tLetters[letter] != sLetters[letter]:
                return False

        return True
        


        
