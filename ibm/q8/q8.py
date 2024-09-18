"""

1. Question 1
Given in request ids as an array of strings,
requests, and an integer k, after all requests are received, 
find the k most recent requests. Report the answer in order of most 
recent to least recent.
Example:
Suppose n = 5, 
requests = ["item1", "item2", "item3", "item1", "item3"], 
and k = 3.
Starting from the right and moving left, collecting distinct requests,
there is "item3" followed by "item1". 
Skip the second instance of "item3" and find "item2". 
The answer is ["item3", "item1", "item2"].
Function Description
Complete the function getLatestKRequests in the editor below.
getLatestKRequests takes the following arguments: str requests[n]: 
the request ids
int k: the number of requests to report
"""

from typing import List


def getLatestKRequest(requests:List[str], k:int):
    res = []
    seen = set()

    for i in range(len(requests) - 1, -1, -1):
        if requests[i] not in seen:
            res.append(requests[i])
            seen.add(requests[i])
        
        if len(res) == k:
            return res
    
#Test Case 
print("Test Case 1: ", getLatestKRequest(["item1", "item2", "item3", "item1", "item3"], 3))

