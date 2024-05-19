def table2(start,end):
    info1=""
    for j in range(start,end+1,1):
        for i in range(1,11,1):
            info1=info1+str(j)+"*"+str(i)+"="+str(j*i)+"\n"
            print(info1)
        print()
        info1=info1+"\n"
    return info1


result=table2(3,8)
print(result)        
