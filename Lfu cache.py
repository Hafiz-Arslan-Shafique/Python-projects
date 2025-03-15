# class LFUCache:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.cache = {}
#         self.frequency = {}

#     def get(self, key):
#         if key in self.cache:
#             self.frequency[key] += 1  # Increase frequency of the key
#             return self.cache[key] if key else -1
        

#     def put(self, key, value):
#         if self.capacity == 0:
#             return
        
#         if key in self.cache:
#             # self.cache[key] = value
#             self.cache.update({key:value})
#             self.frequency[key] += 1
#         else:
#             if len(self.cache) >= self.capacity:
#                 # Evict the least frequently used key
#                 min_lfu_key = min(self.frequency, key=lambda k: self.frequency[k])
#                 ## del self.cache[lfu_key]
#                 ## del self.frequency[lfu_key]
#                 self.cache.pop(min_lfu_key)
#                 self.frequency.pop(min_lfu_key)
            
#             self.cache[key] = value
#             self.frequency[key] = 1  # Initialize frequency to 1

# # Usage Example:
# lfu_cache = LFUCache(3)
# lfu_cache.put(1, 'A')
# lfu_cache.put(2, 'B')
# lfu_cache.put(3, 'C')
# print(lfu_cache.get(3))  # Output: 'A'
# print(lfu_cache.cache)  # Output: 'A'
# print(lfu_cache.frequency)  # Output: 'A'
# lfu_cache.put(2, 'D')    # Evicts key 2
# print(lfu_cache.get(2))  # Output: -1
