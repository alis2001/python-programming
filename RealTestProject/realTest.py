import re
welcomeText = "welcome to the test!"
welcomeText = welcomeText.title()
print(welcomeText)
score = 0 
counter = 2
while counter > 0 and score <= 1:
    firstqes = input("Please choose the choices in regard of their corresponding numbers \n Who had been the 20th president of the United States of America: \n 1:Obama \n 2:Trump \n 3:Clinton \n 4:Garfield \n" )
    if firstqes != "":
        if int(firstqes) == 4:
            score += 1
            print(score)
        else:
            counter = counter - 1
            print(counter)
        secondqes = input("When is the independence day? \n 1:July 4 \n 2:July 6 \n 3:July 10 \n 4:July 15 \n")
        if int(secondqes) == 1:
            score += 1
            print(score)
        else:
            counter = counter - 1
            print(counter)
        thirdqes = input("Where is the state of Texas located? \n 1:north \n 2:south \n 3:west \n 4:east \n" )
        if int(thirdqes) == 2:
            score += 1
            print(score)
        else:
            counter = counter - 1
            print(counter)
        
if score >= 2:
    print("You have passed")
else:
    print("Maybe next time!")    
        
              
                
    
    
    