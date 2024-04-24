class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        values = self.store[key]

        res = ""
        l, r = 0, len(values) - 1
        while (l <= r):
            mid = (l + r) // 2
            if values[mid][-1] <= timestamp:
                res = values[mid][0]
                l = mid + 1
            else: 
                r = mid - 1
        
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

#Test Cases

mySolution = TimeMap()

print("Set: ", mySolution.set("foo", "bar", 1))
print("Get: ", mySolution.get("foo", 1))
print("Get: ", mySolution.get("foo", 3))
print("Set: ", mySolution.set("foo", "bar2", 4))
print("Get: ", mySolution.get("foo", 4))
print("Get: ", mySolution.get("foo", 5))