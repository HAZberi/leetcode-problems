from collections import defaultdict
import heapq
from typing import List


class Twitter:

    def __init__(self):
        self.time = 0
        self.followMap = defaultdict(set) #{userId: Set(userIds)}
        self.tweetMap = defaultdict(list) #{userId: List([time, tweetId])}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.time, tweetId])
        self.time -= 1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                time, tweetId = self.tweetMap[followeeId][index]
                minHeap.append([time, tweetId, followeeId, index - 1])

        heapq.heapify(minHeap)

        while minHeap and len(res) < 10:
            time, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                time, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [time, tweetId, followeeId, index - 1])
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

#Test Case
twitter = Twitter()

print("Post Tweet(1, 5): ", twitter.postTweet(1, 5))
print("Get News Feed (1): ", twitter.getNewsFeed(1))
print("Follow(1, 2): ", twitter.follow(1, 2))
print("Post Tweet(2, 6): ", twitter.postTweet(2, 6))
print("Get News Feed (1): ", twitter.getNewsFeed(1))
print("Unfollow(1, 2): ", twitter.unfollow(1, 2))
print("Get News Feed (1): ", twitter.getNewsFeed(1))
