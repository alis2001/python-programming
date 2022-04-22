import random
def randomCase():
    result = random.randint(1, 100)
    return result


i = 1

while i == 1:
    result = randomCase()
    print(result)
    num = input("Number please")
    
    if int(num) == result:
        print("Success")
    else:
        print("Failed")
        
    anw = input("Again?")
    if anw == "yes":
        i = 1
    else:
        i = 0
        
        
    
    