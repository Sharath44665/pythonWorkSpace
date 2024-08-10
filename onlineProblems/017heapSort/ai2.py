def radix_sort(arr):
    max_digit = max(map(len, map(str, arr)))
    for digit in range(max_digit):
        buckets = [[] for _ in range(10)]
        for num in arr:
            digit_val = (num // 10**digit) % 10
            buckets[digit_val].append(num)
        arr = [num for bucket in buckets for num in bucket]
    return arr
