x = eval(input ("Enter amount of bill: $"))
y = eval(input ("Enter number of people: "))
z = eval(input ("Enter amount of tips(%): "))

v = z/100 * x/y
print("Tip amount per person : ${:0.2f}".format(v) )
print("Total amount per person : ${:0.2f}".format(x/y + v))
