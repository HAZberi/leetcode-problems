"""
1. Question 1
When multiple tasks are executed on a single-threaded CPU, 
the tasks are scheduled based on the principle of pre-emption. 
When a higher-priority task arrives in the execution queue, 
then the lower- priority task is pre-empted, i.e. its execution 
is paused until the higher-priority task is complete.
There are n functions to be executed on a single-threaded CPU, 
with each function having a unique ID between 0 and n-1. 
Given an integer n, representing the number of functions 
to be executed, and an execution log as an array of strings, 
logs, of size m, determine the exclusive times of each of the 
functions. Exclusive time is the sum of execution times for all 
calls to a single-threaded CPU.

Example:
n = 3
log = {
    "0:start:0",
    "1:start:2",
    "2:start:3",
    "2:end:4",
    "1:end:5",
    "0:end:6",
}

Output = [3, 2, 2]
"""

from typing import List


def executionTime(n:int, logs:List[str]):
    res = [0] * n
    stack = []
    prev = 0

    for log in logs:
        parsed_log = log.split(":")
        func_id = int(parsed_log[0])
        action = parsed_log[1]
        time_stamp = int(parsed_log[2])

        if action == 'start':
            if stack:
                f_id = stack[-1]
                res[f_id] += (time_stamp - prev)
            stack.append(func_id)
            prev = time_stamp
        else:
            f_id = stack.pop()
            res[f_id] += ((time_stamp - prev) + 1)
            prev = time_stamp + 1
    
    return res

#Test Cases
print("Test Case 1: ", executionTime(3, [
    "0:start:0",
    "1:start:2",
    "2:start:3",
    "2:end:4",
    "1:end:5",
    "0:end:6"
]))
print("Test Case 2: ", executionTime(2, [
    "0:start:0",
    "1:start:2",
    "1:end:5",
    "0:end:6"
]))
print("Test Case 3: ", executionTime(3, [
    "0:start:0",
    "0:end:1",
    "1:start:2",
    "1:end:4",
    "2:start:5",
    "2:end:7"
]))



