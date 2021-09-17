
data = [9, 4, 7, 2, 3, 8, 6, 1, 5, 0]
data_count = len(data)

print("Original data\n", data)

for i in range(0, data_count-1):
    for j in range(data_count-1, i, -1):
        if data[j-1] > data[j]:
            data[j], data[j-1] = data[j-1], data[j]

print("Sorted data\n", data)