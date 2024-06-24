import logging

# Configure logging
logging.basicConfig(filename='shellsort.log', level=logging.DEBUG, format='%(message)s')

def shellSort(arr):
    n = len(arr)
    gap = n // 2 
    logging.debug(f"Starting shellSort with initial array: {arr}")
    
    while gap > 0:
        logging.debug(f"Current gap: {gap}")
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
            logging.debug(f"Array after inserting element at index {i}: {arr}")
        gap //= 2
    logging.debug(f"Array after sorting: {arr}")

# Test array
arr = [35, 33, 42, 10, 14, 19, 27, 44]

n = len(arr)
print("Array before sorting:")
for i in range(n):
    print(arr[i])

shellSort(arr)

print("\nArray after sorting:")
for i in range(n):
    print(arr[i])
