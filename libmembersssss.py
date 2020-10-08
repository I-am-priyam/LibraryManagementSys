fileout=open("Library_Memberss.txt","w")
n="THE NAME OF LIBRARY MEMBERS ARE AS FOLLWS"
fileout.write(n)
fileout.flush()
fileout.write("\n")
fileout.write("\n")
for i in range(10):
    print(" ENTER THE MEMBER",(i+1)," BELOW :")
    Mname=input("ENTER NAME OF THE MEMBER :")
    
    fileout.write(Mname)
    fileout.flush()
    fileout.write("\n")

fileout.close()
