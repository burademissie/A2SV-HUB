# Problem: Insert Delete GetRandom O(1) - https://leetcode.com/problems/insert-delete-getrandom-o1/description/

class RandomizedSet:

    def __init__(self):
        self.hashMap = {}
        self.numList = []
        
    def insert(self, val: int) -> bool:
        ret = val not in self.hashMap
        if ret:
            self.hashMap[val] = len(self.numList)
            self.numList.append(val)
        return ret

    def remove(self, val: int) -> bool:
        ret = val in self.hashMap
        if ret:
            index = self.hashMap[val]
            last = self.numList[-1]
            self.numList[index] = last
            self.hashMap[last] = index
            self.numList.pop()
            del self.hashMap[val]
        
        return ret
        
    def getRandom(self) -> int:
        return random.choice(self.numList)

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()