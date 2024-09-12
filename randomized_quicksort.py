import random

def randomized_quicksort(arr):
    def quicksort_helper(arr, low, high):
        if low < high:
            pivot_index = random.randint(low, high)
            arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
            pivot = arr[high]
            i = low - 1
            for j in range(low, high):
                if arr[j] < pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            pivot_index = i + 1
            quicksort_helper(arr, low, pivot_index - 1)
            quicksort_helper(arr, pivot_index + 1, high)
    
    quicksort_helper(arr, 0, len(arr) - 1)
    return arr

# Example usage
if __name__ == "__main__":
    sample_array = [3, 6, 8, 10, 1, 2, 1]
    print("Original array:", sample_array)
    sorted_array = randomized_quicksort(sample_array)
    print("Sorted array:", sorted_array)
