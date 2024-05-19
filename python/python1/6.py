f1=open("in2.txt","r")
f2=open("out2.txt","w")
s1=f1.readline().replace("\n","")
list1=s1.split(",")
start=int(list1[0])
end=int(list1[1])
for j in range(start,end+1,1):
    for i in range(1,11,1):
        info1=str(j)+"*"+str(i)+"="+str(j*i)
        print(info1)
        f2.write(info1+"\n")
    print()
    f2.write("\n")


        
