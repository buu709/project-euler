#!/usr/bin/env python3
fibSeq = [1, 2]
while True:
    fibSeq.append(fibSeq[-1] + fibSeq[-2])
    if fibSeq[-1] >= 4000000:
        break
evenFibSeq = []
for num in fibSeq:
    if num % 2 == 0:
        evenFibSeq.append(num)
    else:
        pass
print(sum(evenFibSeq))
#answer = 0
#for num in evenFibSeq:
#    answer = answer + num
#print(answer)
# print(evenFibSeq)
# print(fibSeq)