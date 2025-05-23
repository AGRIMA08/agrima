def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])      # Sort left half
    right = merge_sort(arr[mid:])     # Sort right half
    return merge(left, right)         # Merge sorted halves
def merge(left, right):
    result = []
    i = j = 0
    # Merge two sorted arrays
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # Append remaining elements (only one of these will actually run)
    result.extend(left[i:])
    result.extend(right[j:])
    return result
n = int(input())                             
arr = list(map(int, input().split()))        
k = int(input())                             
sorted_arr = merge_sort(arr)
print(sorted_arr[k-1])