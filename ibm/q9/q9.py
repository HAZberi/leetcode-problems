"""
1. Question 1
Implement a simple prototype service to find the difference 
between two JSON (JavaScript Object Notation) objects.
To keep the prototype simple, a JSON will contain only key-value pairs
and no nested objects or arrays in it. Given two JSON strings, 
json 1 and json2, find the list of keys for which the values are different. 
If a key is present in only one of the JSONS, 
it should not be considered in the result. 
The list of keys should be sorted in lexicographically ascending order.
Example:
Suppose json1 = "{"hello":"world","hi":"hello","you":"me"}" 
and json2=" {"hello":"world","hi":"helloo", "you":"me"}"
The only common key where the values differ is "hi". 
Hence the answer is ["hi"].
Function Description
Complete the function getJSONDiff in the editor below.
get/SONDiff has the following parameter(s):
json1: the first JSON string
json2: the second JSON string
Returns
string[]: a sorted list of keys that have different associated values in the two JSONS
Constraints
1≤json1|, |json2| ≤ 10^5
There are no white spaces in the string.
"""

import json


def getJSONDiff(json1:str, json2:str):
    dict1 = json.loads(json1)
    dict2 = json.loads(json2)

    res = []

    for key in dict1:
        if key in dict2 and dict1[key] != dict2[key]:
            res.append(key)
    
    return sorted(res)

#Test Case
print("Test Case 1:", getJSONDiff('{"hello":"world","hi":"hello","you":"me"}', '{"hello":"worlds","hi":"helloo", "you":"me"}' ))



