def bubbleSort(array):
	for i in range(len(array)):
		# number of comparison after i
		for j in range(0, len(array) - i - 1): 
		# ignore largest element at the end, j+1 = last element in comparison
			if array[j] > array[j+1]:
				array[j], array[j+1] = array[j+1], array[j]

def insertionSort(nums: list[int]):
    """Insertion sort"""
    # Outer loop: sorted range is [0, i-1]
    for i in range(1, len(nums)):
        base = nums[i]
        j = i - 1
        # Inner loop: insert base into the correct position within the sorted range [0, i-1]
        while j >= 0 and nums[j] > base:
            nums[j + 1] = nums[j]  # Move nums[j] to the right by one position
            j -= 1
        nums[j + 1] = base  # Assign base to the correct position

def insertionSort(nums: List[int]):
	for i in range(1, len(nums)):
		base = nums[i]
		j = i - 1
		while j >= 0 and nums[j] > base: # sorted on the left of base which mean nums[j] should be largest
			nums[j + 1] = nums[j] # Move nums[j] to right : nums[j+1] 
			j -= 1
		num[j + 1] = base # assign base to the correct position


from typing import List

# better than while loop because python for loop is optimized for performance and faster than while loop j+=1 
def selectionSort(nums: List[int]):
    for i in range(len(nums)):
        min_index = i 
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_index]:  # Corrected comparison and added colon
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]


def selectionSort(nums: List[int]):
	for i in range(len(nums)):
		min_index = i 
		j = i + 1 
		while j < len(nums):
			if nums[j] > nums[min_index]:
				min_index = j
			j += 1
		nums[i], nums[min_index] = nums[min_index], nums[i]

def mergeSort(nums: List[int]):
	def split(nums: List[int], start,end):
		if len(nums) == 1:
			return  

		mid =  // 2
		left = split(start, mid)
		right = split(mid+1, end)

		if left > right:


def mergeSort(nums: List[int]):
	def merge(nums: List[int], left: int, mid: int, right: int):
		# create a temporary array to store merged results
		tmp = [0] * (right - left + 1)
		# initialize the start indices of the left and right subarrays (mid + 1), k is current indices of tmp
		i, j, k = left, mid+1, 0  
		# while both subarrays still have elements, compare and copy the smaller element into the temporary array
		while i <= mid and j <= right:
			if nums[i] <= nums[j]:
				tmp[k] = nums[i]
				i += 1
			else:
				tmp[k] = nums[j]
				j += 1
			k += 1

		# Copy the remaining elements , either one of the subarray would have elements
		while i <= mid:
			tmp[k] = nums[i]
			i += 1
			k += 1

		while j <= right:
			tmp[k] = nums[j]
			j += 1
			k += 1

		#copy result to nums
		for idx in range(0, len(tmp)):
			nums[left + idx] = tmp[idx]

	def merge_sort(nums: List[int], left: int, right: int)
		if left >= right:
			return # terminate recursion when length is 1
		#if len(nums) == 1:
		#	return  

		mid = left + (right - left) // 2
		merge_sort(nums, left, mid)
		merge_sort(nums, mid+1, right)
		# Merge stage
		merge(nums, left, mid, right)

	merge_sort(nums, 0, len(nums)-1)
    return nums

def quickSort(nums: list[int]):
	def partition(nums: list[int], left: int, right: int) -> int:
		i, j = left, right
		while i < j:
			while i < j and nums[j] >= nums[left]:
				j -= 1
			while i < j and nums[j] <= nums[left]:
				i += 1
			nums[i], nums[j] = nums[j], nums[i]
		# Swap the pivot with the intersection element
		nums[i], nums[left] = nums[left], nums[i]
		return i


	def quick_sort(nums: list[int], left: int, right: int):

		# Base case: terminate when subarray length is 1
		if left >= right:
			return

		# Partition
		pivot = partition(nums, left, right)
		quick_sort(nums, left, pivot - 1)
		quick_sort(nums, pivot + 1, right)
		




