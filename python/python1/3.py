start=int(input("Enter first number: "))
end=int(input("Enter second number: "))
for j in range(start, end+1,1):
    for i in range(1,11,1):
        info1=str(j)+"*"+str(i)+"="+str(j*i)
        print(info1)
    print()

