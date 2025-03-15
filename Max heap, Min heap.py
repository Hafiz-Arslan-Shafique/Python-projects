######## 3.Implement a max-heap and min-heap using an array and provide push() and pop() operations.

# class Max():
#     def __init__(self):
#         self.heap=[]

#     def push(self,value):
#         self.heap.append(value)
#         self.shift_up(len(self.heap)-1)

#     def shift_up(self,idx):
#         parent=(idx-1)//2
#         if idx>0 and self.heap[idx] > self.heap[parent]:
#             self.swap(idx,parent)
#             self.shift_up(parent)

#     def pop(self):
#         self.swap(0,len(self.heap)-1)
#         rem_item=self.heap.pop()
#         print('Item',rem_item)
#         self.shift_down(0)

#     def shift_down(self,id):
#         largest=id
#         left=2*id+1
#         right=2*id+2
#         if left < len(self.heap) and self.heap[left] > self.heap[largest]:
#             largest =left
#         if right < len(self.heap) and self.heap[right] > self.heap[largest]:
#             largest=right
#         if largest !=id:
#             self.swap(id,largest)
#             self.shift_down(id)

#     def swap(self,i,j):
#         self.heap[i],self.heap[j] = self.heap[j],self.heap[i]

#     def final(self):
#         print('Final heap =>',self.heap)

# max=Max()
# max.push(5)
# max.push(45)
# max.push(87)
# max.push(200)
# max.final()
# max.pop()
# max.pop()
# max.pop()









class MaxHeap:
    def __init__(self):
        self.heap = []

    def parent(self, index):
        return (index - 1) // 2

    def left_child(self, index):
        return 2 * index + 1

    def right_child(self, index):
        return 2 * index + 2

    def heapify_up(self, index):
        while index > 0 and self.heap[self.parent(index)] < self.heap[index]:
            # Swap if current node is greater than the parent
            self.heap[self.parent(index)], self.heap[index] = self.heap[index], self.heap[self.parent(index)]
            index = self.parent(index)

    def heapify_down(self, index):
        largest = index
        left = self.left_child(index)
        right = self.right_child(index)

        # Check if left child is larger
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left

        # Check if right child is larger
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        # If the largest is not the current node, swap and continue heapifying
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.heapify_down(largest)

    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def extract_max(self):
        if len(self.heap) == 0:
            return None  # or raise exception

        if len(self.heap) == 1:
            return self.heap.pop()

        # Swap the first element with the last element
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        max_value = self.heap.pop()
        self.heapify_down(0)
        return max_value

    def peek(self):
        return self.heap[0] if self.heap else None

    def size(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

# Example usage:
max_heap = MaxHeap()
max_heap.insert(10)
max_heap.insert(20)
max_heap.insert(15)

print("Max value:", max_heap.extract_max())  # 20
print("Max value:", max_heap.extract_max())  # 15
print("Max value:", max_heap.extract_max())  # 10














import heapq

# # Creating a Min Heap using heapq
# min_heap = []
# heapq.heappush(min_heap, 3)
# heapq.heappush(min_heap, 5)

# print("Min Heap:", min_heap)
# ##Extract the smallest element
# min_element = heapq.heappop(min_heap)
# print("Extracted Min:", min_element)



# Creating a Max Heap using heapq (negating the values)
max_heap = []
heapq.heappush(max_heap, 3)
heapq.heappush(max_heap, 5)

print("Max Heap:", [-x for x in max_heap]) 
##Extract the larg element
max_element = -heapq.heappop(max_heap)

print("Extracted Max:", max_element)