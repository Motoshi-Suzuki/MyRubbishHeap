data = [1, 2, 4, 5, 3, 6, 8]
data_count = len(data)

print("Original data\n", data)

for i in range((data_count-1) // 2, -1, -1):
    p = i
    c = p * 2 + 1

    while c < data_count:
        if c < data_count-1 and data[c] < data[c+1]:
            c += 1

        if data[p] >= data[c]:
            break

        data[p], data[c] = data[c], data[p]
        print(data)
        p = c 
        c = p * 2 + 1

print("Sorted data\n", data)