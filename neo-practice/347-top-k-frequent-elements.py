from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for n, c in count.items():
            freq[c].append(n)
        
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


solution = Solution()
test_case_1 = print(solution.topKFrequent([1,1,1,2,2,3], 2))
test_case_1 = print(solution.topKFrequent([1,1,1,2,2,3,100,100,100,100,1], 2))