# classic fizz buzz

for i in range(101):
    output = ""
    if (i % 5 == 0) and (i % 3 == 0):
        output = "turu"
    elif i % 3 == 0:
        output = "fizz"
    elif i % 5 == 0:
        output = "buzz"
    else:
        output = i
    print(output)
