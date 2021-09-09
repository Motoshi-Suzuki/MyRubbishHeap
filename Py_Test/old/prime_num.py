
is_prime = [True] * 100
is_prime[0] = False
is_prime[1] = False
num = 2

def create_list():
    prime_list = ""

    for i in range(100):
        if is_prime[i] == True:
            prime_list += "{:2d}, ".format(i)
        else:
            prime_list += "/, "
        
        if i % 10 == 9:
            prime_list += "\n"
    
    print(prime_list)

def drop_off_non_prime():
    global num

    for i in range(num + num, 100, num):
        is_prime[i] = False
        print(i)
    
    print("Dropped off multiples of ", num, ".")
    create_list()

    while num < 100:
        num += 1
        if is_prime[num] == True:
            break

create_list()

while num < 10:
    input("Press Enter")
    drop_off_non_prime()