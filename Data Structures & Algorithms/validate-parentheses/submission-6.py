class Solution:
    def isValid(self, s: str) -> bool:
        characters = {')': '(', 
                     ']': '[', 
                     '}': '{'} 

        charStack = []

        for p in s:
            if p in characters.keys():
                if charStack and charStack[-1] == characters[p]:
                    charStack.pop()
                else:
                    return False
            else:
                charStack.append(p)
        
        
        return False if len(charStack) > 0 else True


