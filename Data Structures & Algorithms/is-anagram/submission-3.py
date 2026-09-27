class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s = jar
        # t = ja
        # s -> 3 letters -> 1 j, 1 a, 1 r
        # t -> 3 letters -> 1 j, 1 a, 1 m 
        # Return False

        # s = racecar  
        # t = carrace 
        # s -> 7 letters -> 2 r, 2 a, 2 c, 1 e, 
        # t -> 7 letters -> 2 r, 2 a, 2 c, 1 e, 
        # Return True
        
        # edge case 01 -> inputs with different sizes will never be anagrams
        if len(s) != len(t): # O(1)
            return False 

        # create a dict with keys being the letter and values the amount
        dicLetters = {}     
        for letter in s:     # O(len(s)) iterated through the entire string
            if letter not in dicLetters:
                dicLetters[letter] = 1   
            else:
                dicLetters[letter] += 1
        
        for letter in t:    # O(len(t)) iterated through the entire string
            if letter not in dicLetters:
                return False
            elif letter in dicLetters and dicLetters[letter] > 0:
                dicLetters[letter] -= 1
            else:
                return False
        
        return True

# Time Complexity: O(len(s) + len(t)) -> O(n)
# Space Complexity: 1 dict -> size = set(s) -> O(n) worst case if the string has no
#                 duplicate charactors




