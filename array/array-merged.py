def arrayMerged(left, right):
  sorted = []
  r = 0
  l = 0
  sum = len(left) + len(right)
  while len(sorted) < sum:    
    if l < len(left):
      if r < len(right):
        if left[l] < right[r]:
          sorted.append(left[l])
          l += 1
        else: 
          sorted.append(right[r])
          r += r
      else:
        sorted.append(left[l])
        l += 1
    else: 
      sorted.append(right[r])
      r += 1

  return sorted

sorted = arrayMerged([1, 3, 5], [2, 4, 7])
print(sorted)
