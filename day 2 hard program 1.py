

a=int(input("enter the no.of fresh breads:"))
b=int(input("enter the no.of day old breads:"))
c=int(input("regularprice:"))
discount=c-((60/100)*c)
print("the amount of fresh breads:",c*a)
print("the amount of day old breads:",discount*b)
print("Total amount:",(c*a)+(discount*b))
