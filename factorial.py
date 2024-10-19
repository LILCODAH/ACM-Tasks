def facto(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
def summseries(n):
    summ=0
    for i in range(1,n+1):
        summ+=1/facto(i)
    return summ
x=summseries(eval(input("Enter the value for n...")))
print(x)