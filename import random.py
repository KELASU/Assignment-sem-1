import random


myList = ["Kenya","Candice","Kenma"]
kenyaList = ["Kenya fit deez nuts in your mouth","Kenya put deez nuts in ur mouth","Kenya shove deez nuts down ur throat"]
candiceList = ["Candice nuts fit in ur mouth","Candice nutz be shove down ur throat"]
kenmaList = ["Kenma nutz fin in ur jaw","Kenma nutz fit in ur mout","Kenma nutz be shove down ur throat"]

x = str(input (""))
print (x)
if x in myList :
    print(" ( ͡° ͜ʖ ͡°)")
else :
    print("Ur a dissapointment")

if x == "Kenya":
    z = [0,1,2]
    v = random.randint(0,2)
    y = kenyaList
    print(y[v])
elif x == "Candice":
    z = [0,1,2]
    v = random.randint(0,2)
    y = candiceList
    print(y[v])
elif x == "Kenma":
    z = [0,1,2]
    v = random.randint(0,2)
    y = kenmaList

    print(y[v])
else:
    print("L+Bozo")