from functools import reduce

def large(num1,num2):
    if num1 > num2:
        return num1
    else:
        return num2


p1=[1,100,200,50,40,500]
q=reduce(large,p1)
print(q)


