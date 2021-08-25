def selection(list):
  for i in range(0, len(list)):
    lowerIndex = i 
    for y in range(i + 1, len(list)):
      if list[y] < list[lowerIndex]:
        lowerIndex = y
    tmp = list[i]
    list[i] = list[lowerIndex]
    list[lowerIndex] = tmp
  print(list)  

selection([5, 1, 2, 10, 12, 7, 3, 4, 9, 14, 13, 11, 6])
  