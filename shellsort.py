def shellSort(arr):
    
    n = len(arr)
    gap = n // 2 # original sshell sequence.

    
    while gap > 0:
        for i in range(gap, n):
        
            temp = arr[i]

           
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap


            arr[j] = temp
        gap //= 2  


# test array
arr = [35, 33, 42, 10,14,19,27,44]

n = len(arr)
print("Array before sorting:")
for i in range(n):
    print(arr[i])

shellSort(arr)

print("\nArray after sorting:")
for i in range(n):
    print(arr[i])
