#!/usr/bin/env python3
sum_list = []
for num in range(3, 1000, 3):
        sum_list.append(num)
for num in range(5, 1000, 5):
        sum_list.append(num)
print(sum(set(sum_list)))
