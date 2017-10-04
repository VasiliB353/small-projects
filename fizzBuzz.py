# Vasili B
# 8/2/2017

for i in range(1, 101):

    output = ""
    if not i%3:
        output += "Fizz"
    
    if not i%5:
        output += "Buzz"
    
    if output == "":
        output = i
    
    print(output)