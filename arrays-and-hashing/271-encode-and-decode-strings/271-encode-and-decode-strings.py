class Solution(object):
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        
        return res

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        res, i = [], 0
        
        while i < len(str):
            j = i
            while str[j] != "#":
                j += 1
            length = int(str[i:j])
            res.append(str[j+1:(j+length+1)])

            i = j + length + 1

        return res 



#Test Cases

mySolution = Solution()

print("Test Case 1")
print("Encoded: ", mySolution.encode(["lint","co#de","love","you"]))
print("Decoded: ", mySolution.decode(mySolution.encode(["lint","co#de","love","you"])))

print("Test Case 2")
print("Encoded: ", mySolution.encode(["we", "#4say", "1#:", "ye#s"]))
print("Decoded: ", mySolution.decode(mySolution.encode(["we", "#4say", "1#:", "ye#s"])))


