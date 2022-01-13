#!/usr/bin/env python3
toSum = []
for num in range(1, 1000):
    if num % 5 == 0:
        toSum.append(num)
    else:
        if num % 3 == 0:
            toSum.append(num)
theSum = 0
for number in toSum:
    theSum = number + theSum
print(toSum)
print(theSum)