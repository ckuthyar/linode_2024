def goldmedal(fname):
    f1=open(fname)
    names=[]
    subjects=[]
    sub1=[]
    sub2=[]
    sub3=[]
    sub4=[]
    sub5=[]
    total=[]
    topper_sub1=[]
    topper_sub2=[]
    topper_sub3=[]
    topper_sub4=[]
    topper_sub5=[]
    goldmedalist=[]
    for i in range(0,26,1):
        s1=f1.readline().replace("\n","")
        list1=s1.split(",")
        names.append(list1[0])

        list2=list1[3].split(":")
        subjects.append(list2[0])
        sub1.append(int(list2[1]))

        list2=list1[4].split(":")
        subjects.append(list2[0])
        sub2.append(int(list2[1]))

        list2=list1[5].split(":")
        subjects.append(list2[0])
        sub3.append(int(list2[1]))

        list2=list1[6].split(":")
        subjects.append(list2[0])
        sub4.append(int(list2[1]))

        list2=list1[7].split(":")
        subjects.append(list2[0])
        sub5.append(int(list2[1]))

        total.append(sub1[i]+sub2[i]+sub3[i]+sub4[i]+sub5[i])

    maxSub1=max(sub1)
    maxSub2=max(sub2)
    maxSub3=max(sub3)
    maxSub4=max(sub4)
    maxSub5=max(sub5)
    maxTotal=max(total)

    for i in range(0,26,1):
        if sub1[i]==maxSub1:
            topper_sub1.append(names[i])
        if sub2[i]==maxSub2:
            topper_sub2.append(names[i])
        if sub3[i]==maxSub3:
            topper_sub3.append(names[i])
        if sub4[i]==maxSub4:
            topper_sub4.append(names[i])
        if sub5[i]==maxSub5:
            topper_sub5.append(names[i])
        if total[i]==maxTotal:
            goldmedalist.append(names[i])
    r1=(topper_sub1,subjects[0],maxSub1)
    r2=(topper_sub2,subjects[1],maxSub2)
    r3=(topper_sub3,subjects[2],maxSub3)
    r4=(topper_sub4,subjects[3],maxSub4)
    r5=(topper_sub5,subjects[4],maxSub5)
    g1=(goldmedalist,"total",maxTotal)
    return(r1,r2,r3,r4,r5,g1)

