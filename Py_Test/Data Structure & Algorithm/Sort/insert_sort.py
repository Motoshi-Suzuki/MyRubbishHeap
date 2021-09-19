import random
from typing import Text

n = 15
data = [0] * n

for i in range(n):
    data[i] = random.randint(1, 99)

print("Original data\n", data)

for i in range(1, n):
    tmp = data[i]
    j = i

    while j > 0 and data[j-1] > tmp:
        data[j] = data[j-1]
        j = j - 1
    
    data[j] = tmp

print("Sorted data\n", data)