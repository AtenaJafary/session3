i=0
number=[]
while i<10 :
    a=input("please enter a number:")
    i=i+1
    number.append(a)
print("input:",number)
b=set(number)
print("output:", b)