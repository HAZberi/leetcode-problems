"""
1. Question 1
A password string, pwd, consists of binary characters (Os and 1s). 
A cyber security expert is trying to determine the minimum number 
of changes required to make thepassword secure. 
To do so, it must be divided into substrings of non-overlapping, 
even length substrings. 
Each substring can only contain 1s or Os, not a mix. 
This helps to ensure that the password is strong and less vulnerable 
to hacking attacks.
Find the minimum number of characters that must be flipped in the 
password string, L.e. changed from 0 to 1 or 1 to 0 to allow 
the string to be divided as described.
"""

def minFlips(pwd: str):
    res = 0

    for i in range(0, len(pwd), 2):
        if pwd[i] != pwd[i + 1]:
            res += 1
    
    return res


#Test Cases 
print("Test Case 1:", minFlips("101011"))
print("Test Case 2:", minFlips("100110"))
print("Test Case 3:", minFlips("1001101111"))




