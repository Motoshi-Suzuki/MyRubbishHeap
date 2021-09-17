
data = [
    ["sato", "0000"],
    ["suzuki", "1111"],
    ["tanaka", "2222"],
    ["takahashi", "3333"]
]

while True:
    i = 0
    name = input("Name? ")

    if name == "":
        print("Search test is terminated")
        break

    while i < len(data) and data[i][0] != name:
        i += 1
    
    if i == len(data):
        print("This name is not registered")
    else:
        print("Phone number of", data[i][0], "is", data[i][1])