class MRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.stack = []

    def get(self, key):
        if key in self.cache:
            self.stack.remove(key)
            self.stack.append(key)
            print(self.cache[key] if key else -1)
       

    def put(self, key, value):
        if key in self.cache:
            self.stack.remove(key)
        elif len(self.cache) >= self.capacity:
            most_recently_used_key = self.stack.pop()
            del self.cache[most_recently_used_key]
        self.cache[key] = value
        self.stack.append(key)

# Usage
mru_cache = MRUCache(3)
mru_cache.put(1, 'A')
mru_cache.put(2, 'B')
mru_cache.put(3, 'C')
mru_cache.get(3)  # Output: 'C'
# mru_cache.put(4, 'D')    # Evicts key 3
# print(mru_cache.get(3))  # Output: -1























# class MRUCache:
#     def __init__(self, limit):
#         self.limit = limit
#         self.cache = {}
#         self.stack = []

#     def get(self, key):      
#         return self.cache[key] if key else -1
        

#     def put(self, key, value):
#         if key in self.cache:
#             self.stack.remove(key)
#         elif len(self.cache) >= self.limit:
#             remove_recently_used_key = self.stack.pop()
#             remove_recently_used_key1 = self.cache.pop()
#             return remove_recently_used_key, remove_recently_used_key1
#         ## self.cache[key]=value
#         self.cache.update({key:value})
#         self.stack.append(key)

# # Usage
# mru_cache = MRUCache(3)
# mru_cache.put(1, 'A')
# mru_cache.put(2, 'B')
# mru_cache.put(3, 'c')    # Evicts key 2
# print(mru_cache.get(2))  # Output: 'C'
# ## print(mru_cache.cache)  
# ## print(mru_cache.stack)  
