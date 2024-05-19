def convert1(infile):

    f1=open(infile,"r")
    for i in range(0,4,1):
        s1=f1.readline().replace("\n","")
        list1=s1.split(" ")
        lhsvalue=float(list1[0])
        lhsunits=list1[1]
        equals=list1[2]
        rhsvalue=float(list1[3])
        rhsunits=list1[4]
        s2="1 "+ lhsunits + " = " + str(rhsvalue/lhsvalue) + " " + rhsunits
        s3="1 "+ rhsunits + " = " + str(lhsvalue/rhsvalue) + " " + lhsunits
        print(s2)
        print(s3)
        print()
convert1("convert1.txt")
