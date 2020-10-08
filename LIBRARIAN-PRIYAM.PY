count=int(input("HOW MANY BOOKS YOU WANT TO KEEP ?? "))
fileout=open("Library_Books.txt","w")
n="""THE BOOK ARE ARRANGED SEPARATELY IN A COLOUMN AND ITS PRICE INFRONT OF IT"
 NAME OF THE BOOK                PRICE(Rs)"""
fileout.write(n)
fileout.flush()
fileout.write("\n")
fileout.write("\n")
for i in range(count):
    print(" ENTER THE DETAILS OF THE BOOK ",(i+1)," BELOW :")
    bookname=input("ENTER NAME OF THE BOOK :")
    price=float(input(" ENTER PRICE OF THE BOOK :"))
    rec=bookname+"    "+str(price)+""+"\n"
    
    fileout.write(rec)
    fileout.flush()

fileout.close()

    
