
data_limit = 5
data = [None] * data_limit
pointer = [None] * data_limit
head = 0

def add_list(new_data):
    n = -1

    for i in range(data_limit):
        if data[i] == None:
            n = i
            break

    if n == -1:
        print("No available storage")
        return False

    for i in range(data_limit):
        if data[i] != None and pointer[i] == None: 
            pointer[i] = n
            break
    
    data[n] = new_data
    pointer[n] = None

    print("Data", new_data, "has added")
    return True

def delete_list(useless_data):
    global head
    n = -1

    for i in range(data_limit):
        if data[i] == useless_data:
            n = i
            break
    
    if n == -1:
        print("There is no such data")
        return False
    
    if n != head:
        for i in range(data_limit):
            if pointer[i] == n:
                pointer[i] = pointer[n]
    else:
        head = pointer[n]

        if head == None:
            head = 0
    
    data[n] = None
    pointer[n] = None

    print("Data", useless_data, "has deleted")
    return True

def print_list():
    p = head

    while True:
        print(data[p], end="→")

        if pointer[p] == None:
            print("End of File")
            break

        p = pointer[p]

for i in range(10, 70, 10):
    add_list(i)

delete_list(10)
print_list()