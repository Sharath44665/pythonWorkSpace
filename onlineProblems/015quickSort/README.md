# Quick sort explanation:

> arr = [5, 3, 1, 9, 2, 4, 8]

### first loop:

use pivot = 5, low = 0, high  = 6 compare five with rest of the array

arr[1], arr[2] less than pivot,  but arr[3]= 9 is greater than pivot val, stop checking here from the left to right // `left=3`

now start comparing from right, checking array from `high` with pivot, 

arr[6] is greater than pivot, but arr[5]=4 is less than pivot // `right=5`

`do swap` arr[left] <--> arr[right] // `do only if left <= right`

> arr = [5, 3, 1, 4, 2, 9, 8]

note that `left=3`

arr[4] is less than pivot, arr[5] is not `left = 5`

from previous we know that `right = 5`, so lets continue from there, arr[5] greater than pivot

so right = 4 // by decrementing in code

note that `left = 5` is not less than or equal to `right =4` 

in this case,`break` out of loop, 

`do swap` arr[low] <--> arr[right] // `do only at out of loop`

> arr = [2, 3, 1, 4, 5, 9, 8]


append the stack  with new indexes = (low, right-1)

also do append the stack from indexes = (right+1, high)


### second loop: continue the same steps from above





