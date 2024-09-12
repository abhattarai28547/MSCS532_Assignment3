import time
import random
from randomized_quicksort import randomized_quicksort

def deterministic_quicksort(arr):
    def quicksort_helper(arr, low, high):
        if low < high:
            pivot_index = low
            pivot = arr[pivot_index]
            i = low + 1
            for j in range(low + 1, high + 1):
                if arr[j] < pivot:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
            arr[low], arr[i - 1] = arr[i - 1], arr[low]
            pivot_index = i - 1
            quicksort_helper(arr, low, pivot_index - 1)
            quicksort_helper(arr, pivot_index + 1, high)
    
    quicksort_helper(arr, 0, len(arr) - 1)
    return arr

def measure_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr)
    return time.time() - start_time

def main():
    sizes = [10, 100, 1000, 5000]
    for size in sizes:
        arr_random = [random.randint(0, 10000) for _ in range(size)]
        arr_deterministic = arr_random.copy()

        time_randomized = measure_time(randomized_quicksort, arr_random)
        time_deterministic = measure_time(deterministic_quicksort, arr_deterministic)

        print(f"Array size: {size}")
        print(f"Randomized Quicksort time: {time_randomized:.5f} seconds")
        print(f"Deterministic Quicksort time: {time_deterministic:.5f} seconds")

if __name__ == "__main__":
    main()
