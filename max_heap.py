class MaxHeap:
    def __init__(self):
        self.heap = []
    
    
    def insert(self, value):
        self.heap.append(value)
        self.bubble_up(len(self.heap) - 1)
    
    def bubble_up(self, index):
        parent_index = (index - 1) // 2
        while index > 0 and self.heap[index] > self.heap[parent_index]:
            # swap
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = (index - 1) // 2
    
    def delete_max(self):
        if len(self.heap) == 0:
            return None
        
        # Step 1: Replace the root (max element) with the last element
        max_value = self.heap[0]
        self.heap[0] = self.heap[-1]  # Using [-1] to reference the last element
        self.heap.pop()  # Remove the last element
        
        self._bubble_down(0)
        return max_value
        
    def _bubble_down(self, index):
        heap_size = len(self.heap)
        while True:
            largest = index
            left_child = 2 * index + 1 # check less than heap size
            right_child = 2 * index + 2 # bounded by the size of heap
            
            if left_child < heap_size and self.heap[left_child] > self.heap[largest]:
                largest = left_child
                # if both true, largest becomes left_child then right_child, making largest among 3 index 

            if right_child < heap_size and self.heap[right_child] > self.heap[largest]:
                largest = right_child
            
            if largest != index:
                self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
                index = largest
            else:
                break