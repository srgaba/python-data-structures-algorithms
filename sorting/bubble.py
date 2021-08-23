def bubble(list):
  x = 0
  until = len(list)
  while(x < until):
    for z in range(0, until - 1):
      if list[z] > list[z+1]:
        tmp = list[z]
        list[z] = list[z+1]
        list[z+1] = tmp
    until -= 1
  return list

print(bubble([0, 1, 5, 3]))

