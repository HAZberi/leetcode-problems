from collections import Counter, deque
import heapq
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #Count the frequency of similar tasks
        count = Counter(tasks)

        #Biuild a Max Heap of frequency counts
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        #Setting starting time and a queue for cooling time
        time = 0
        queue = deque() #[task count, available time]

        #Excuting the tasks
        while maxHeap or queue:
            time += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt: #Only if a simiar task is remaining. 
                    queue.append([cnt, time + n])
            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap, queue.popleft()[0])
        return time

#Test Cases 
mySolution = Solution()
print("Test Case 1: ", mySolution.leastInterval(["A","A","A","B","B","B"], 2))
print("Test Case 1: ", mySolution.leastInterval(["A","C","A","B","D","B"], 1))
print("Test Case 1: ", mySolution.leastInterval(["A","A","A","B","B","B"], 3))
