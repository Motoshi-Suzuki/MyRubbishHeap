
# data_list = ["apple", "banana", "orange", "pineapple", "kiwi"]

# file = open("Pytest.text", 'w')

# for i in range(len(data_list)):
#     file.write(data_list[i], ",")

# file.close()

file = open("Pytest.text", 'r')
read = file.read()
file.close()

string = read.split(",")
num = len(string)
data = [""] * num

for i in range(num):
    if string[i] != None:
        data[i] = string[i]

print(data)
print(read)
