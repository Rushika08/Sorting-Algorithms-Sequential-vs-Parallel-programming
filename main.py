import time
import random
import multiprocessing


# Task 1

# ----------------------------------------------------------------------------------------
# Merge Sort Sequential manner

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged


# ----------------------------------------------------------------------------------------
# Quick Sort Sequential manner

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)



# ----------------------------------------------------------------------------------------


# Task 2

# ----------------------------------------------------------------------------------------
# Merge Sort Parallel manner

def parallel_merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    with multiprocessing.Pool() as pool:
        left = pool.apply(merge_sort, (left,))
        right = pool.apply(merge_sort, (right,))

    return merge(left, right)


# ----------------------------------------------------------------------------------------
# Quick Sort Parallel manner

def parallel_quick_sort(arr, processes=2):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    if processes > 1:
        with multiprocessing.Pool(processes=processes) as pool:
            # Use apply_async for non-blocking execution
            left_result = pool.apply_async(parallel_quick_sort, args=(left, processes // 2))
            right_result = pool.apply_async(parallel_quick_sort, args=(right, processes // 2))

            # Retrieve the results
            left = left_result.get()
            right = right_result.get()

    else:
        left = parallel_quick_sort(left, processes // 2)
        right = parallel_quick_sort(right, processes // 2)

    return left + middle + right



# ----------------------------------------------------------------------------------------


# Task 3

# ----------------------------------------------------------------------------------------
if __name__ == '__main__':
    print("\nPlease wait a while...\n")

    # Generate a larger random list for testing
    larger_list = random.sample(range(1, 100000000), 1000000)

    # Evaluate time for Sequential Merge Sort
    start_time = time.time()
    sequential_merge_sort_result = merge_sort(larger_list)
    sequential_merge_sort_time = time.time() - start_time

    # Evaluate time for Sequential Quick Sort
    start_time = time.time()
    sequential_quick_sort_result = quick_sort(larger_list)
    sequential_quick_sort_time = time.time() - start_time

    # Evaluate time for Parallel Merge Sort
    start_time = time.time()
    parallel_merge_sort_result = parallel_merge_sort(larger_list)
    parallel_merge_sort_time = time.time() - start_time

    # Evaluate time for Parallel Quick Sort
    start_time = time.time()
    parallel_quick_sort_result = parallel_quick_sort(larger_list)
    parallel_quick_sort_time = time.time() - start_time

    # Print the results
    print(f"Sequential Merge Sort Time: {sequential_merge_sort_time:.5f} seconds")
    print(f"Sequential Quick Sort Time: {sequential_quick_sort_time:.5f} seconds")
    print(f"Parallel Merge Sort Time: {parallel_merge_sort_time:.5f} seconds")
    print(f"Parallel Quick Sort Time: {parallel_quick_sort_time:.5f} seconds")
