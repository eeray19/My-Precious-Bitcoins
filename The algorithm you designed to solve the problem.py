#O(n) space is forced, we have to save the values for after we print 
# the number of candidates
from itertools import chain
import timeit
n = int(input('What is the value of n?\n'))

start = timeit.default_timer()
count = 0
# 3 boolean arrays are used in order to keep track of the numbers that has been used for x, y and z.
xTested = [False] * (n+1) 
yTested = [False] * (n+1)
zTested = [False] * (n+1)

toPrint = []
maxtoPrint = []
maxCount = -1
for i in range(n):
  count = 0
  toPrint = []
  xTested = [False] * (n+1)
  yTested = [False] * (n+1)
  zTested = [False] * (n+1)
  # try values for x in the range of n
  for x in range(n+1): 
    # try values for y by splitting the range of n in two and then concatenating them with the reversed way 
    for y in chain(range(i,n+1), range(i)):
      z = n-x-y
      if y>n or z<0: 
        continue
        
      if not xTested[x] and not yTested[y] and not zTested[z]:

        toPrint.append(str(x) + " " + str(y) + " " + str(z))
        count+=1
        xTested[x] = True
        yTested[y] = True
        zTested[z] = True

      z = n - y - x
  if count > maxCount: 
    maxCount = count
    maxToPrint = toPrint.copy()

print(maxCount)
for k in maxToPrint:
  print(k)

stop = timeit.default_timer()
print("Time: ",stop-start)
