def quickSort(arr):
    first  = 0
    last = len(arr)-1
    stack  = [(first, last)]

    while stack:
        first, last = stack.pop()
        pointer = first
        pivot = arr[last]

        for i in range(first, last):
            if arr[i] < pivot:
                arr[i], arr[pointer] = arr[pointer], arr[i]
                pointer += 1
        #[1, 3, 2, 5, 7, 6, 4]
        arr[pointer], arr[last] = pivot, arr[pointer]
        #[1, 3, 2, 4, 7, 6, 5]
        if pointer - 1 > first:
            stack.append((first, pointer-1))

        if pointer + 1 < last:
            stack.append((pointer+1, last))
    return arr


arr = [7, 1, 5, 3, 6, 2, 4]
sortedArray = quickSort(arr)
print(sortedArray)
