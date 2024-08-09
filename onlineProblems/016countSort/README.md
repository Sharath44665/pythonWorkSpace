# Count Sort

`first` find out max in `arr` = [4, 2, 2, 8, 3, 3, 1] , that is `8`

`step2` create counter array of size 9, that is counter[0 for val in maxVal+1]

`step3` count the occurence of each value

counter = [0, 1, 2, 2, 1, 0, 0, 0, 1] meaning: 0 = 0 time, 1 = '1' occurence, 2 = `2` ocucurence, 3 = `2` occurence...

`step 4`: find cumilative sum

like this:

[`0`, `1`, 2, 2, 1, 0, 0, 0, 1] == inital array

idx = 1, [0, `1`, `2`, 2, 1, 0, 0, 0, 1] ---> 1 -> 0+1

idx = 2, [0, 1, `3`, `2`, 1, 0, 0, 0, 1] ---> 3 -> 2+1

idx = 3, [0, 1, 3, `5`, `1`, 0, 0, 0, 1] ---> 5 -> 3+2

idx = 4, [0, 1, 3, 5, `6`, `0`, 0, 0, 1] ---> 6 -> 5+1

idx = 5, [0, 1, 3, 5, 6, `6`, `0`, 0, 1] ---> 6 -> 6+0

idx = 6, [0, 1, 3, 5, 6, 6, `6`, `0`, 1] ---> 6 -> 6+0

idx = 7, [0, 1, 3, 5, 6, 6, 6, `6`, `1`] ---> 6 -> 6+0

idx = 8, [0, 1, 3, 5, 6, 6, 6, 6, `7`] ---> 7 -> 6+1

`Step 5`: Create an output array 

outputAr = [0 for _ in range(len(`arr`))]

`Step 6`: Build the output array using the count array 

Output Array: [0, 0, 0, 0, 0, 0, 0] // Initialize output array

counter array: [0, 1, 3, 5, 6, 6, 6, 6, 7]

reverseArray =  [1, 3, 3, 8, 2, 2, 4]
Placing elements:
- Place 1 at index 0: Output Array: [1, 0, 0, 0, 0, 0, 0]
- Place 3 at index 4: Output Array: [1, 0, 0, 0, 3, 0, 0]
- Place 3 at index 3: Output Array: [1, 0, 0, 3, 3, 0, 0]
- Place 8 at index 6: Output Array: [1, 2, 2, 3, 3, 0, 8]
- Place 2 at index 2: Output Array: [1, 0, 2, 3, 3, 0, 8]
- Place 2 at index 1: Output Array: [1, 2, 2, 3, 3, 0, 8]
- Place 4 at index 5: Output Array: [1, 2, 2, 3, 3, 4, 8]
 
