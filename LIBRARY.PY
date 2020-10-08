print("""
           ___        ___    ____    __        ____    _____     __        __    ______
           \  \  __  /  /   |       |  |      / ___|  /     \   |  |\    /|  |  |
            \  \/  \/  /    |---    |  |___  | |___  |   O   |  |  | \  / |  |  |----
             \___/\___/     |____   |______|  \____|  \_____/   |__|  \/  |__|  |______
   
                                              TO

                                        SUNBEAM ACADEMY
             __         __   _______     _______        ______       _______   ___    ___
            |  |       |  | |   __  |   |   __  |      /  __  \     |   __  |  \  \  /  /
            |  |       |  | |  |__| |   |  |__| |     /  /  \  \    |  |__| |   \  \/  /
            |  |       |  | |   __  \   |   ____|    /  /____\  \   |   ____|    \    /
            |  |_____  |  | |  |__|  |  |  |\  \    /  /      \  \  |  |\  \      |  |
            |________| |__| |________|  |__| \__\  /__/        \__\ |__| \__\     |__|
""")
m="yes"
while m=="yes":
    #THE MENU
    print("""_________________MENU___________________ 
1.TO SEE LIBRARY BOOKS
2.TO SEE LIBRARY MEMBERS
3.TO ADD BOOKS IN LIBRARY
4.TO DELETE BOOKS OF LIBRARY
5.TO ADD LIBRARY MEMBERS
6.TO SEE DUE DATES OF BOOK RETURN
7.TO CALCULATE FINE
8.ABOUT LIBRARY RULES""")
    print("")
    print("")
    print("")
    q=int(input("ENTER YOUR CHOICE FROM ABOVE : "))
    
    if q==1:
        myfile=open("Library_Books.txt","r")
        s=myfile.read()
        print(s)
        myfile.close()
        m=input("DO YOU WANT TO GO TO MAIN MENU.......(yes/no)")
        if m!="yes":
            break
    if q==2:
        my_file=open("Library_Memberss.txt","r")
        p=my_file.read()
        print(p)
        my_file.close()
        m=input("DO YOU WANT TO GO TO MAIN MENU.......(yes/no)")
        if m!="yes":
            break
    if q==3:
        #THIS PROGRAM LETS YOU ADD LIBRARY BOOKS
        fileout=open("Library_Books.txt","a")
        count=int(input("HOW MANY BOOKS YOU WANT TO ADD ?? "))
        for i in range(count):
            print(" ENTER THE DETAILS OF THE BOOK ",(i+1)," BELOW :")
            bookname=input("ENTER NAME OF THE BOOK :")
            price=float(input(" ENTER PRICE OF THE BOOK :"))
            rec=bookname+"    "+str(price)+" "+"\n"
            fileout.write(rec)
            fileout.flush()

        fileout.close()
        m=input("DO YOU WANT TO GO TO MAIN MENU.......(yes/no)")
        if m!="yes":
            break
    if q==4:
        import os
        fin=open("Library_Books.txt","r")
        fout=open("temp.txt","w")
        N=int(input("ENTER WHICH LINE TO DELETE : "))
        COUNT=0
        rec=" "
        while rec:
            rec=fin.readline()
            COUNT+=1
            
            if COUNT==N:
                pass
            else:
                fout.write(rec)
        fin.close()
        fout.close()
        os.remove("Library_Books.txt")
        os.rename("temp.txt","Library_Books.txt")
    if q==5:
        #THIS PROGRAM LETS YOU ADD LIBRARY MEMBERS
        filout=open("Library_Memberss.txt","a")
        cont=int(input("HOW MANY MEMBERS YOU WANT TO ADD ?? "))
        for i in range(cont):
            print(" ENTER THE DETAILS OF THE MEMBER ",(i+1)," BELOW :")
            MEM_name=input("ENTER NAME OF THE MEMBER :")

            fileout.write(MEM_name)
            fileout.flush()

        fileout.close()
        m=input("DO YOU WANT TO GO TO MAIN MENU.......(yes/no)")
        if m!="yes":
            break
    if q==8:
        print(""" ________LIBRARY RULES________
A.PLEASE KEEP SILENCE IN THE LIBRARY HALL
B.PLEASE BRING YOUR LIBRARY CARD FOR ENTRY IN THE LIBRARY
C.KEEP THE DOCUMENRIES OF LIBRARY SAFER AND DO NOT TRY TO DESTROY IT
D.ANY BOOK FOUND WITHOUT THE INFORMATION OF THE MEMBER WILL BE KEPT IN THE LIBRARY
E.PLEASE TAKE CARE OF THE BOOKS ISSUED TO YOU
F.ANY WEAR AND TEAR IN THE BOOK WILL BE COUNTED AS FINE (after being issued)
G.FINE WILL BE TAKEN IF BOOK IS RETURNED AFTER ITS DUE DATE (Rs 10 PER DAY LATE)
H.REISSUING OF BOOK WILL BE DONE ON EVERY 6th DAY AFTER DATE OF ISSUE

""")
#_____________________only_for_LIBRARIAN____________________________________
Z=int(input("ENTER PASSWORD TO CHANGE LIBRARY SETTING :"))#password=123456
while Z==123456:
    print(""" a.TO LIST LIIBRARY MEMBERS
b.TO LIST BOOKS IN THE LIBRARY""")
    if q==a:
        fileo=open("Library_Memberss.txt","w")
        n="THE NAME OF LIBRARY MEMBERS ARE AS FOLLWS"
        fileo.write(n)
        fileo.flush()     
        fileo.write("\n")
        fileo.write("\n")
        for i in range(10):
            print(" ENTER THE MEMBER",(i+1)," BELOW :")

            Mname=input("ENTER NAME OF THE MEMBER :")
    
            fileo.write(Mname)
            fileo.flush()
            fileo.write("\n")

        fileo.close()

    if q==b:
        cunt=int(input("HOW MANY BOOKS YOU WANT TO KEEP ?? "))
        fileou=open("Library_Books.txt","w")
        n="""THE BOOK ARE ARRANGED SEPARATELY IN A COLOUMN AND ITS PRICE INFRONT OF IT"
         NAME OF THE BOOK                PRICE(Rs)"""
        fileou.write(n)
        fileou.flush()
        fileou.write("\n")
        fileou.write("\n")
        for i in range(cunt):
            print(" ENTER THE DETAILS OF THE BOOK ",(i+1)," BELOW :")
            bokname=input("ENTER NAME OF THE BOOK :")
            price=float(input(" ENTER PRICE OF THE BOOK :"))
            recO=bokname+"    "+str(price)+""+"\n"
    
            fileou.write(recO)
            fileou.flush()

        fileou.close()

        
        
