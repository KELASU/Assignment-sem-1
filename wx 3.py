from decimal import ROUND_DOWN, Rounded


x = eval(input("enter a number of seconds :"))
h = (x//3600)
m = (x//60 - h*60)
s = (x-((h*3600) + (m*60)))
print(f"{h:02}",f"{m:02}",f"{s:02}",sep=":")