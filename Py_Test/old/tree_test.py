
LEFT = 0
RIGHT = 1
data = 2

node = [
    [1, 2, 10],
    [3, 4, 20],
    [5, None, 30],
    [None, None, 40],
    [6, 7, 50],
    [None, None, 60],
    [None, None, 70],
    [None, None, 80]
]

data_limit = len(node)

while True:
    num_string = input("number = ")

    if num_string == "":
        print("Tree test is terminated")
        break

    try:
        num = int(num_string)
    except:
        print("Enter number")
        continue

    if 0 <= num and num < data_limit:
        print("The value of node {} is {}".format(num, node[num][data])) 

        left = node[num][LEFT]
        if left != None:
            print("The child of left side is", str(node[left][data]))
        else:
            print("The child of left side is None")
        
        right = node[num][RIGHT]
        if right != None:
            print("The child of right side is", str(node[right][data]))
        else:
            print("The child of right side is None")
    
    else:
        print("Enter value from 0 to", str(data_limit -1))