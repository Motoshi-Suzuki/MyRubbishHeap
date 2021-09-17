
data = [75, 48, 2, 34, 96, 36, 87, 60, 71, 24]
# flag = False
i = 0

while True:
    num_string = input("Number? ")

    if num_string == "":
        print("Search test is terminated")
        break

    try:
        num = int(num_string)
    except:
        print("Enter number")
        continue

    while i < len(data) and data[i] != num:
        i += 1

    if i == len(data):
        print("Number", str(num), "doesn't exist")
    else:
        print("data[{}] is {}".format(i, num))
        # flag = True

    # if flag == False:
    #     print("Number", str(num), "doesn't exist")