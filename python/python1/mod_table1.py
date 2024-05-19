def table3(infile,outfile):
    def table2(start,end):
        info1=""
        for j in range(start,end+1,1):
            for i in range(1,11,1):
                info1=info1+str(j)+"*"+str(i)+"="+str(j*i)+"\n"
                print(info1)
            print()
            info1=info1+"\n"
        return info1
    f1=open(infile,"r")
    f2=open(outfile,"w")
    start=int(f1.readline())
    end=int(f1.readline())
    result=table2(start,end)
    print(result)
    f2.write(result)


