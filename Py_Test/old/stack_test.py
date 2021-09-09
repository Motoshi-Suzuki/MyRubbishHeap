
data_list = ["apple", "banana", "orange", "pineapple", "kiwi"]
stack = [""] * len(data_list)
stack_pointer = 0

def push(data):
    global stack_pointer

    if stack_pointer < len(data_list):
        stack[stack_pointer] = data
        stack_pointer += 1
        print("Data", data, "has pushed.")
    
    else:
        print("You can't push more data.")

def pop():
    global stack_pointer

    if stack_pointer > 0:
        stack_pointer -= 1
        return stack[stack_pointer]
    
    else:
        print("No stacked data")
        return None

for i in range(len(data_list)):
    push(data_list[i])

for i in range(len(data_list)):
    poped_data = pop()
    print("Poped data:", poped_data)