from random import choice

class RandomizedSet:

    def __init__(self):
        self.hash_map = {}
        self.lst = []


    def insert(self, val: int) -> bool:
        if val in self.hash_map:
            return False
        else:
            self.hash_map[val] = 1
            return True
        

    def remove(self, val: int) -> bool:
        if val in self.hash_map:
            self.hash_map.pop(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        keys = list(self.hash_map.keys())
        return choice(keys)