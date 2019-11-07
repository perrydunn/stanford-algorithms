class MaxHeap:
    def __init__(self):
        self.heap = []

    def size(self):
        return len(self.heap)

    def insert(self, x):
        self.heap.append(x)
        i = len(self.heap)
        placed = False
        while not placed:
            parent = i // 2
            if parent < 1 or x <= self.heap[parent - 1]:
                placed = True
            else:
                self.heap[i - 1] = self.heap[parent - 1]
                self.heap[parent - 1] = x
                i = parent

    def peak(self):
        return self.heap[0]

    def pop(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        x = self.heap[0]
        elem = self.heap.pop()
        i = 1
        placed = False
        limit = len(self.heap)
        while not placed:
            left = 2 * i
            right = 2 * i + 1
            if right <= limit:
                if x >= self.heap[left - 1] and x >= self.heap[right - 1]:
                    placed = True
                elif self.heap[left - 1] > self.heap[right - 1]:
                    self.heap[i - 1] = self.heap[left - 1]
                    self.heap[left - 1] = x
                    i = left
                else:
                    self.heap[i - 1] = self.heap[right - 1]
                    self.heap[right - 1] = x
                    i = right
            else:
                if left <= limit and x < self.heap[left - 1]:
                    self.heap[i - 1] = self.heap[left - 1]
                    self.heap[left - 1] = x
                placed = True
        return elem


class MinHeap:
    def __init__(self):
        self.heap = []

    def size(self):
        return len(self.heap)

    def insert(self, x):
        self.heap.append(x)
        i = len(self.heap)
        placed = False
        while not placed:
            parent = i // 2
            if parent < 1 or x >= self.heap[parent - 1]:
                placed = True
            else:
                self.heap[i - 1] = self.heap[parent - 1]
                self.heap[parent - 1] = x
                i = parent

    def peak(self):
        return self.heap[0]

    def pop(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        x = self.heap[0]
        elem = self.heap.pop()
        i = 1
        placed = False
        limit = len(self.heap)
        while not placed:
            left = 2 * i
            right = 2 * i + 1
            if right <= limit:
                if x <= self.heap[left - 1] and x <= self.heap[right - 1]:
                    placed = True
                elif self.heap[left - 1] < self.heap[right - 1]:
                    self.heap[i - 1] = self.heap[left - 1]
                    self.heap[left - 1] = x
                    i = left
                else:
                    self.heap[i - 1] = self.heap[right - 1]
                    self.heap[right - 1] = x
                    i = right
            else:
                if left <= limit and x > self.heap[left - 1]:
                    self.heap[i - 1] = self.heap[left - 1]
                    self.heap[left - 1] = x
                placed = True
        return elem


if __name__ == "__main__":
    min_heap = MinHeap()
    max_heap = MaxHeap()
    median_sum = 0
    with open("Median.txt", "r") as f:
        num = f.readline()
        v1 = int(num)
        median_sum += v1
        num = f.readline()
        v2 = int(num)
        if v1 >= v2:
            min_heap.insert(v1)
            max_heap.insert(v2)
            median_sum += v2
        else:
            min_heap.insert(v2)
            max_heap.insert(v1)
            median_sum += v1
        num = f.readline()
        while num:
            v = int(num)
            if v >= min_heap.peak():
                min_heap.insert(v)
            else:
                max_heap.insert(v)
            min_heap_size = min_heap.size()
            max_heap_size = max_heap.size()
            if min_heap_size == max_heap_size:
                median_sum += max_heap.peak()
            elif min_heap_size - max_heap_size == 1:
                median_sum += min_heap.peak()
            elif max_heap_size - min_heap_size == 1:
                median_sum += max_heap.peak()
            else:
                if min_heap_size > max_heap_size:
                    max_heap.insert(min_heap.pop())
                else:
                    min_heap.insert(max_heap.pop())
                median_sum += max_heap.peak()
            num = f.readline()
    print(median_sum % 10000)
