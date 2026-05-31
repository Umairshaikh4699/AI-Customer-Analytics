import random
import time

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = []
    right = []
    for x in arr[1:]:
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)
    return quick_sort(left) + [pivot] + quick_sort(right)

# Generate random array of size between 1 and 20
size = random.randint(100, 250)
array = [random.randint(0, 100) for i in range(size)]

print("Size of array: " + str(size))

# Merge Sort timing
arr1 = array.copy()
start = time.time()
merge_sort(arr1)
end = time.time()
print("Time taken by Merge Sort: " + str(round((end - start) * 1000, 4)) + " milliseconds")

# Quick Sort timing
arr2 = array.copy()
start = time.time()
arr2 = quick_sort(arr2)
end = time.time()
print("Time taken by Quick Sort: " + str(round((end - start) * 1000, 4)) + " milliseconds")
