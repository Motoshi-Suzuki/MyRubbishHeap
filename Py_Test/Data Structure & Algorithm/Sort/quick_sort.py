import random

n = 15
data = [0] * n

for i in range(n):
    data[i] = random.randint(1, 99)

def quick_sort(left, right):
    i = left
    j = right
    pivot = data[(left+right) // 2]

    while True:
        while data[i] < pivot:
            i += 1
        while data[j] > pivot:
            j -= 1      
        if i >= j:
            break

        data[i], data[j] = data[j], data[i]
        print("Sorting now !!\n", data)
        i += 1
        j -= 1
    
    if left < i-1:
        quick_sort(left, i-1)
        print("Start sorting left side")
    
    if right > j+1:
        quick_sort(j+1, right)
        print("Start sorting right side")

print("---Originl data---\n", data)
quick_sort(0, n - 1)
print("---Sorted data---\n", data)

