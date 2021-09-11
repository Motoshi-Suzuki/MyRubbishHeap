
data = [1, 2, 9, 12, 20, 25, 32, 48, 50, 57, 72, 78, 80, 93, 100]

while True:
    left = 0
    right = len(data) - 1
    flag = False
    key_string = input("Number? ")

    if key_string == "":
        print("Search test is terminated")
        break

    try:
        key = int(key_string)
    except:
        print("Enter number")
        continue

    while left <= right:
        mid = (left + right) // 2
        print("left={} mid={} right={}".format(left, mid, right))

        if data[mid] == key:
            print("data[{}] is {}".format(mid, key))
            flag = True
            break

        if data[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    
    if flag == False:
        print("Could not find this value")