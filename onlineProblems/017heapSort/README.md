## Radix Sort or Heap Sort

Radix Sort is a non-comparative sorting algorithm that sorts integers or strings by grouping digits based on their place value. Here’s a step-by-step guide to manually running Radix Sort in Python:

### Phase 1: Preparation

Define a function `countingSort` to perform counting sort based on a given digit position (`exp`).
Initialize an array `arr` with unsorted elements.

### Phase 2: Radix Sort

Iterate through each digit position (from least significant to most significant) using a variable `exp`.
For each `exp`, call the `countingSort` function to distribute elements into buckets based on the digit value.
Update the `arr` array with the sorted elements from each bucket.

### another explanation

Radix Sort is a non-comparative, linear-time sorting algorithm that sorts elements by processing them digit by digit. It’s particularly efficient for integers or strings with fixed-size keys, as it avoids direct comparisons between elements. Instead, Radix Sort distributes elements into buckets based on each digit’s value, from the least significant digit to the most significant digit.

Here’s a step-by-step breakdown:

1. Initialize buckets or arrays to store elements based on each digit’s value (0-9).
2. Iterate through each digit’s position (starting from the least significant and moving to the most significant).
3. For each digit position, use counting sort as a subroutine to sort the elements based on that digit’s value.
4. Distribute elements into the corresponding buckets.
5. Repeat steps 2-4 for each digit position (from least significant to most significant).
6. Once all digit positions have been processed, concatenate the elements from each bucket to produce the sorted output.

Radix Sort has several advantages:

- Linear time complexity (O(nk), where n is the number of elements and k is the number of digits).
- Efficient use of memory, especially for large datasets.
- Stable sorting, preserving the relative order of elements with the same key value.

However, Radix Sort also has some limitations:

- Requires fixed-size keys (integers or strings with a fixed length).
- Not suitable for sorting small datasets, as its overhead exceeds the benefits.
- Can be slower for strings or floating-point numbers due to the need for character or digit extraction.

Radix Sort can be implemented in various ways, including:

- Least Significant Digit (LSD) sorting, which is generally stable and suitable for most applications.
- Most Significant Digit (MSD) sorting, which is more suitable for sorting strings or fixed-length integer representations.

In conclusion, Radix Sort is a powerful algorithm for sorting integers or strings with fixed-size keys, particularly when dealing with large datasets. Its linear time complexity and efficient memory usage make it an attractive choice for many applications. However, its limitations should be carefully considered before implementation.


## explanation with example:

array = [170, 45, 75, 90, 802, 24, 2, 66]

intialize `radixArr` with 10 empty lists

find the maxValue in array = 802
radixArr = [[] for _ in range(10)]

Now pop the values of the given array and put it in right index.

### first loop (looping on the base of `maxValue`)
[17`0`, 4`5`, 7`5`, 9`0`, 80`2`, 2`4`, `2`, 6`6`]
<table>
<tr>
<th>
idx
</th>
<th>
radixArr
</th>
<th>
poppedValue
</th>
</tr>
<tr>
<td>0</td>
<td>[90, 170]</td>
<td>step5 = 90, step8 = 170</td>
</tr>
<tr>
<td>1</td>
<td>[]</td>
<td></td>
</tr>
<tr>
<td>
2
</td>
<td>

[2, 802]
</td>
<td>
step1 = 2, step4 = 802
</td>
</tr>
<tr>
<td>3</td>
<td>[]</td>
<td></td>
</tr>
<tr>
<td>
4
</td>
<td>
[24]
</td>
<td>
step3 = 24
</td>
</tr>
<tr>
<td>5</td>
<td>[75, 45]</td>
<td>step6 = 75, step7 = 45</td>
</tr>
<tr>
<td>
6
</td>
<td>

[6`6`]
</td>
<td>
step0 = 66
</td>
</tr>
<tr>
<td>7</td>
<td></td>
<td></td>
</tr>
<tr>
<td>8</td>
<td></td>
<td></td>
</tr>
<tr>
<td>9</td>
<td></td>
<td></td>
</tr>
</table>

from above table, place the values of radixArr like this:

arr = [170, 90, 802,  2, 24, 45, 75,  66 ] # pop from `radixAr` and appending at the end, whatever value found in radixArr

### second loop based on maxValue:

arr = [1`7`0, `9`0, 8`0`2,  2, `2`4, `4`5, `7`5,  `6`6 ]

<table>
<tr>
<th> idx </th>
<th> radixAr</th>
</tr>
<tr>
<td>0</td>
<td>[2, 802]</td>
</tr>
<tr>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>[24]</td>
</tr>
<tr>
<td>3</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>[45]</td>
</tr>
<tr>
<td>6</td>
<td>[66]</td>
</tr>
<tr>
<td>7</td>
<td>[75, 170]</td>
</tr>
<tr>
<td>8</td>
<td></td>
</tr>
<tr>
<td>9</td>
<td>[90]</td>
</tr>
</table>

end of the the loop ar = [802, 2, 24, 45, 66, 170, 75,  90]

### third loop based on maxValue:

ar= [`8`02, 2, 24, 45, 66, `1`70, 75,  90]

<table>
<tr>
<th>idx</th>
<th>radixAr</th>
</tr>
<tr>
<td>0</td>
<td>[90, 75, 66, 45, 24, 2 ]</td>
</tr>
<tr>
<td>1</td>
<td>[170]</td>
</tr>
<tr>
<td>2</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td></td>
</tr>
<tr>
<td>7</td>
<td></td>
</tr>
<tr>
<td>8</td>
<td>[802]</td>
</tr>
<tr>
<td>9</td>
<td></td>
</tr>
</table>

ar = [2, 24, 45, 66, 75, 90, 170, 802]
