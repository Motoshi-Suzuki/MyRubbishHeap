
a = [1, 3, 4, 7, 8, 9]
b = [0, 2, 5, 6]
a_count = len(a)
b_count = len(b)
c = [0] * (a_count + b_count)

i = 0
j = 0
p = 0

print("Data a\n", a)
print("Data b\n", b)

while i < a_count and j < b_count:
    if a[i] <= b[j]:
        c[p] = a[i]
        i += 1
        p += 1
    else:
        c[p] = b[j]
        j += 1
        p += 1

while i < a_count:
    c[p] = a[i]
    i += 1
    p += 1

while j < b_count:
    c[p] = b[j]
    j += 1
    p += 1

print("Merged data\n", c)