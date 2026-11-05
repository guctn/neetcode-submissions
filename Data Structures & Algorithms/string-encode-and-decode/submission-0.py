class Solution:

    def encode(self, strs: List[str]) -> str:
        # approach: for each string will get its size and add the number to a string followed by a # and the string - "2#me4#love"
        encoded_string = ""
        for word in strs:
            length = len(word)
            encoded_string = encoded_string + f"{length}#{word}"

        return encoded_string

    def decode(self, s: str) -> List[str]:
        # approach: getting the encoded_string we'll get the first number and start after the # then count then iterate the same times of the number and add the string to a new array
        decoded_strings = []
        l, r = 0, 0


        while l < len(s):
            while s[r] != "#":
                r +=1
            size = int(s[l:r])
            decoded_strings.append(s[r+1:r+size+1])
            l = r + size+1
            r = l

        return decoded_strings

