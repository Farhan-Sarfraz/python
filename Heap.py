# import heapq
# nums = [5, 1, 9, 3]
# heapq.heapify(nums)
# sorted_nums = [heapq.heappop(nums) for _ in range(len(nums))]
# print(sorted_nums)  

# import heapq
# n = [77,55,99,33,89,21]
# heapq.heapify(n)
# sort_num = [heapq.heappop(n) for _ in range(len(n))]
# print(sort_num)

# import heapq

# heap = []
# n = [10,3,5,11,8,6]

# for num in n:
#     heapq.heappush(heap,num)

# print("mini_heap:",heap)
# print("minimum elements:",heapq.heappop(heap))

# import heapq

# heap = []
# elements = [10,4,7,2,8]

# for n in elements:
#     heapq.heappush(heap,-n)

# print("maxi_heap is:",[-x for x in heap])
# print("maximum elemets:",-heapq.heappop(heap))

# import heapq

# task = []

# heapq.heappush(task, (2, "write code"))
# heapq.heappush(task, (1, "study heap"))
# heapq.heappush(task, (3,"take quiz"))

# while task:
#     priority, tsk = heapq.heappop(task)
#     print(f"priority {priority} -> {task}")


class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def pop_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def _heapify_up(self, i):
        parent = (i - 1) // 2
        if i > 0 and self.heap[i] < self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            self._heapify_up(parent)

    def _heapify_down(self, i):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self._heapify_down(smallest)

h = MinHeap()
for num in [5, 3, 17, 10, 84, 19, 6, 22, 9]:
    h.insert(num)

print("Heap:", h.heap)
print("Min Element:", h.pop_min())
