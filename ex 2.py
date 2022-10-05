a = int(input("value:"))

if a > 1: 
    for i in range(2, a):
        if (a/i)%1 == 0:
            print(a,"is not a prime number") 
            break
        else:
            print(a,"is a prime number")
            break
