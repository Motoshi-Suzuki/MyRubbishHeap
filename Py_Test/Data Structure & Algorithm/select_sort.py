
data = [9, 3, 7, 1, 4, 2, 5, 6, 8, 0]

print("Original data", "\n", data)

for i in range(0, 9):
    min_num = i

    for j in range(i + 1, 10):
        if data[j] < data[min_num]:
            min_num = j
    
    data[i], data[min_num] = data[min_num], data[i]
    print(i + 1, data)

print("Sorted data", "\n", data)