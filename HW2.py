## Implementation

import random
import time
import sys
import tracemalloc

# Quick Sort 
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Merge Sort 
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result



##Performance Measurement Function

def measure_performance(sort_function, arr):
    # Track memory and execution time
    tracemalloc.start()
    start_time = time.time()
    sort_function(arr.copy())  # Copy to avoid in-place sorting affecting results
    execution_time = time.time() - start_time
    memory_used = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()
    return execution_time, memory_used


## Creating Test Datasets
def generate_test_datasets(size):
    sorted_data = list(range(size))
    reverse_sorted_data = list(range(size, 0, -1))
    random_data = random.sample(range(size * 2), size)
    return sorted_data, reverse_sorted_data, random_data



##Run and Record Results

def run_tests():
    dataset_size = 5555  
    sorted_data, reverse_sorted_data, random_data = generate_test_datasets(dataset_size)
    
    datasets = {
        "Sorted": sorted_data,
        "Reverse Sorted": reverse_sorted_data,
        "Random": random_data
    }
    
    for dataset_name, dataset in datasets.items():
        print(f"\nTesting on {dataset_name} dataset (size={dataset_size}):")
        
        # Quick Sort
        time_qs, memory_qs = measure_performance(quick_sort, dataset)
        print(f"Quick Sort - Time: {time_qs:.6f}s, Memory: {memory_qs / 1024:.2f} KB")
        
        # Merge Sort
        time_ms, memory_ms = measure_performance(merge_sort, dataset)
        print(f"Merge Sort - Time: {time_ms:.6f}s, Memory: {memory_ms / 1024:.2f} KB")




run_tests()
