# Quick sort explanation:

> arr = [7, 1, 5, 3, 6, 2, 4]

### first loop:

use pivot = 4, in stack === low = 0, high  = 6 

compare rest with five 

pointer  = low

if arr[i] < pivot:

swap values of arr[i] and arr[pointer] and increment pointer by 1

after ending the loop, place the **pivot value** at **arr[pointer]**

**next** find the low and high for new **pivotValue**, that is if pointer-1 > low, then stack.append((low, pointer-1))

if pointer+1 < high, stack.append((pointer+1, high))

### second loop: repeat the same