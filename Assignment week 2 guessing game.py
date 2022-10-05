import random
Rint = random.randint(1,100)
Guess = eval(input("input your value here :"))
while Guess != Rint:
    if Guess < Rint:
        print(Guess,"is too low",sep="")
        Guess = eval(input("Try again:"))
    elif Guess > Rint:
        print(Guess,"is too high",sep="")
        Guess = eval(input("Try again:"))
    else :
        print("Value invalid")
print(Guess,"is correct",sep="")
            
    
       
        
