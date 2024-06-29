def least_common_multiple(a, b):
  greater = 0
  if a> b:
    greater = a
  else:
    greater = b

  while True:
    if greater%a == 0 and greater%b == 0:
      return greater
    greater += 1


# print(least_common_multiple(10, 12)) # 60
# multiples of 4 are 4, 8, 12, 16, 20, ...
# multiples of 6 are 6, 12, 18, 24, ...
print(least_common_multiple(4, 6)) # 12
