from collections import deque
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        char_occur = {}
        window_map = {}
        window_size = len(s1)

        for letter in s1:
            char_occur[letter] = 1 + char_occur.get(letter, 0)


        for i in range(window_size):
            window_map[s2[i]] = 1 + window_map.get(s2[i], 0)


        if char_occur == window_map:
            return True
        
        for i in range(len(s2) - window_size):
            if window_map[s2[i]] and window_map[s2[i]] > 1:
                window_map[s2[i]] -= 1
            else:
                window_map.pop(s2[i])
            
            window_map[s2[i+window_size]] = 1 + window_map.get(s2[i+window_size], 0)

            if window_map == char_occur:
                return True

        return False
