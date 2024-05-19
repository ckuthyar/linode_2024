f1=open("in1.txt","r")
start=int(f1.readline())
end=int(f1.readline())
for j in range(start,end+1,1):
    for i in range(1,11,1):
        info1=str(j)+"*"+str(i)+"="+str(j*i)
        print(info1)
    print()


