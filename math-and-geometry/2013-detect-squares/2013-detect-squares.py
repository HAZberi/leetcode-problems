from collections import defaultdict
from typing import List


class DetectSquares:

    def __init__(self):
        self.ptsMap = defaultdict(int)
        self.ptsList = []

    def add(self, point: List[int]) -> None:
        self.ptsMap[tuple(point)] += 1
        self.ptsList.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        qx, qy = point
        for x, y in self.ptsList:
            if (abs(qx - x) != abs(qy - y)) or qx == x or qy == y:
                continue
            res += self.ptsMap[(qx, y)] * self.ptsMap[(x, qy)]
        
        return res
    
#Test Case 1
solution = DetectSquares()
solution.add([3, 10])
solution.add([11, 2])
solution.add([3, 2])
solution.add([1, 1])
solution.add([1, 1])
print("Test case 1 [11, 10]: ", solution.count([11, 10]))
print("Test case 1 [14, 8]: ", solution.count([14, 8]))
solution.add([11, 2])
print("Test case 1 [11, 10]: ", solution.count([11, 10]))
print("Test case 1 [1, 1]: ", solution.count([1, 1]))

