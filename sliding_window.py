# Fixed Size Window
def max_sum_subarray(arr, k):
    n = len(arr)
    current_sum = 0
    max_sum = 0
    for i in range(k):
        current_sum += arr[i]
    max_sum = current_sum
    for i in range(k, n):
        current_sum += arr[i] - arr[i-k]
        max_sum = max(max_sum, current_sum)
    return max_sum



"""
n = 6
k = 3
max_sum = 2+1+5 = 8 

"""        

# Dynamic Sized Window        
arr = [2, 1, 5, 1, 3, 2]
k = 3
max_sum = max_sum_subarray(arr, k)
print(max_sum)


def min_subarray_len(s, arr):
    n = len(arr)
    min_len = float('inf')
    current_sum = 0
    start = 0
    for end in range(n):
        current_sum += arr[end]
        
        while current_sum >= s:
            min_len = min(min_len, end - start + 1)
            current_sum -= arr[start]
            start += 1
    
    return min_len if min_len != float('inf') else 0
        
    
        
arr = [2, 3, 1, 2, 4, 3]
s = 7
print(min_subarray_len(s, arr))  # Output: 2 (subarray [4, 3])