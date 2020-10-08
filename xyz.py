# -*- coding: cp1252 -*-
import random
import pickle
class library():
    lb=random.randint(1000,2000)
    def __init__(self):
        self.gt=0
        self.bookcon=""
        self.timecon=""
        self.delay=""
        library.lb +=1
        self.book2=[]
        self.da=""
        self.name=""
        self.age=""
        self.tk=0
        self.dt=""
        self.jun=""
        self.gender=""
        self.pho=""
        self.time1=[]
        self.fine1=0
        self.fine2=0
        self.fine3=0
        self.fine4=0
        self.fine5=0
        self.fine=0
        self.forte1="Undefined"
        self.book()
        self.avail()
        self.conf()
    def dis(self):                                              #Book Information                 
        print( 'The Card:',library.lb)
        print("The Name of Borrower:",self.tno," "*20)
    def book(self):
        print('\n'*5)                                         #Your Issue
        self.dt=input("Enter the Subject:-")
        self.jun=input("Enter your Topic (Fiction\Fact) :-")
    def avail(self):                                           #Dispaly the Books available
        print("The Following Books are availables:-")
        books=['Harry Potter and the Cursed Child',"Stephen Hawking's Into The Dark","The day we went to Moon",'Abra ka dabra','India Alone',
               'Sumita Arora- An inspiration','Samyak the trader','Ashutosh Vohra- Snakes' ,'The sound of rain','American History',
               'The History of oscars','1984 by George Orwell','2001: A Space Odyssey by Arthur C. Clarke','84',
               'Charing Cross Road by Helene Hanff','Above the Dark Circus by Hugh Walpole','The Accidental Tourist by Anne Tyler',
               'The Adventures of Huckleberry Finn by Mark Twain','The Age of the Cathedrals: Art and Society',
               '980-1420 by Georges Duby','The Alexandria Quartet by Lawrence Durrell','I Am Legend by Richard Matheson',
               "Amiel's Journal by Henri Frédéric Amiel",'Among the Believers: An Islamic Journey by V. S. Naipaul',
               'On Mulberry Street','Maths Puzzle by Das Gupta','The Maths of our life by Anjana Mitra']
        self.da=[7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
        qw=len(books)-1                                     #for Timming
        no=random.randint(6,10)
        for i in range(0,no):
            rq=random.randint(0,qw)
            th=random.randint(0,23)
            tm=random.randint(0,60)
            tk=str(th)+':'+str(tm)
            self.time1.append(tk)
            print(i+1,':',"Book name:",books[rq])
            self.book2.append(books[rq])
        self.gt=int(input("Enter the Book Number for Details-"))
        self.info()
    def Fines(self):                                       #Fines
        print("Fines are as Follows")
        self.fine1=random.randint(300,500)
        print("Exclusive Hard Copy-",self.fine1)
        self.fine2=random.randint(200,300)
        print("Exclusive Paperback-",self.fine2)
        self.fine3=random.randint(100,200)
        print("E-book-",self.fine3)
        self.fine4=random.randint(50,100)
        print("Indian Edition-",self.fine4)
        self.fine5=random.randint(25,50)
        print("Hindi Edition-",self.fine5)
    def info(self):
        print("--------------------------------------------------------------------------------------------------------------------------------------------------")
        print("Details for Book:")                    #Timing Details
        print("Name of Book-",self.book2[self.gt-1])
        print("Delay in Arriving (if any)")
        f=random.randint(0,3)
        if f==0:
            print("The Book delivery is ON TIME")
        else:
            self.da=[7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
            print("Delay for",self.da[random.randint(7,29)],'days due to transport problem')
        ft=input("Do you to check other book details(y/n)-")
        if ft=='y':
            self.gt=int(input("Enter the Book Number for Details-"))
            self.info()
    def priCard(self):
        print("DETAILS"  )                   #Card generation
        print("""----------------------------------------------------------------------------------------------------------------------------------
                                                                 S U N B E A M   A CA D E M Y   L I B R A R Y  """)
        print("Book Name-",self.bookcon)
        print("Timming-",self.timecon)
        print("Name-",self.name)
        print("Age-",self.age)
        print("Gender-",self.gender)
        print("Phone Number-",self.pho)
        print("Book type-",self.forte1)
        self.finalfine()
        print("Fines",self.fine)
        print("""----------------------------------------------------------------------------------------------------------------------------------""")
    def finalfine(self):          #Forte-Fine Generation
        if self.forte1=="Exclusive Hard Copy":
            self.fine=self.fine1
        if self.forte1=="Exclusive Paperback":
            self.fine=self.fine2
        if self.forte1=="E-book":
            self.fine=self.fine3
        if self.forte1=="Indian Edition":
            self.fine=self.fine4
        if self.forte1=="Hindi Edition":
            self.fine=self.fine5
            
    
    def conf(self):                    #Library Card Mangement Main
        dg=input("Do you want to borrow the  book?")
        while dg=='y':
            self.gt=int(input("Enter the book number you wish to borrow-"))
            self.Fines()
            fg=input("Do you want to confirm?-")
            if fg=='y':
                self.bookcon=self.book2[self.gt-1]
                self.timecon=self.time1[self.gt-1]
                self.forte()
                self.info1()
                self.priCard()
                dk='y'
                if dk=='y':
                    break
            gh=input("Do you want to edit your order?")
            if gh=='y':
                self.book()
    def forte(self):              #Forte Defining
        print(""" 1)International Edition
                 2)Indian Edition
                 3)Hindi Edition
                 """)
        df=int(input("Enter the choice"))
        if df==1:
            print('''1)Exclusive Hard Copy
                    2)Exclusive Paperback
                    3)E-book
                    ''')
            kl=int(input("Enter the number"))
            if kl==1:
                self.forte1="Exclusive Hard Copy"
            if kl==2:
                self.forte1="Exclusive Paperback"
            if kl==3:
                self.forte1="E-book"
        if df==2:
            self.forte1="Indian Edition"
        if df==3:
            self.forte1="Hindi Edition"
    def info1(self):                 #Personal info load
        self.name=input("Enter your name-")
        self.age=input("Enter your age-")
        print("""GENDER
                 1)MALE
                 2)FEMALE
                 3)OTHER  """)
        jk=input("Enter your choice-")
        if jk=='1':
            self.gender='Male'
        if jk=='2':
            self.gender='Female'
        else:
            self.gender=='Other'
        self.pho=input('Enter you phone number')
while True:                   #main menu   
    print('''                  W E L C O M E    T O    S U N B E A M    A C A D E M Y    L I B R A R Y
                                Accelerating towards academic pinnacle since 1972
     1)Borrowing Book
     2)Loading Previous information
     3)Total Books to Arrive
     4)Total Books going for donation
     5)Exit
     ''')
    ad=input("Enter your choice:")
    if ad=='1':
        while True:
            file1=open("information.txt","ab+")
            try1=library()
            pickle.dump(try1,file1)
            file1.close()
            g=input("Want to Borrow another book?")
            if g=='n':
                break
    if ad=='2':
        file2=open("information.txt","rb")
        try:
            while True:    
                cus1=pickle.load(file2)
                cus1.priCard()
        except EOFError:
            file2.close()
    if ad=="3":
        print("The Following Books will be available")
        books=['Harry Potter and the Cursed Child',"Stephen Hawking's Into The Dark","The day we went to Moon",'Abra ka dabra','India Alone',
               'Sumita Arora- An inspiration','Samyak the trader','Ashutosh Vohra- Snakes' ,'The sound of rain','American History',
               'The History of oscars','1.	1984 by George Orwell','2001: A Space Odyssey by Arthur C. Clarke','84',
               'Charing Cross Road by Helene Hanff','Above the Dark Circus by Hugh Walpole','The Accidental Tourist by Anne Tyler',
               'The Adventures of Huckleberry Finn by Mark Twain','The Age of the Cathedrals: Art and Society',
               '980-1420 by Georges Duby','The Alexandria Quartet by Lawrence Durrell','I Am Legend by Richard Matheson',
               "Amiel's Journal by Henri Frédéric Amiel",'Among the Believers: An Islamic Journey by V. S. Naipaul',
               'On Mulberry Street','Maths Puzzle by Das Gupta','The Maths of our life by Anjana Mitra']
        for i in range(0,random.randint(10,15)):
            print(books[random.randint(0,len(books)-1)])
            da=[7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
            print('Books will be available within',da[random.randint(7,30)],'days')
    if ad=='4':
        print("The Following Trains are going")
        books=['Harry Potter and the Cursed Child',"Stephen Hawking's Into The Dark","The day we went to Moon",'Abra ka dabra','India Alone',
               'Sumita Arora- An inspiration','Samyak the trader','Ashutosh Vohra- Snakes' ,'The sound of rain','American History',
               'The History of oscars','1.	1984 by George Orwell','2001: A Space Odyssey by Arthur C. Clarke','84',
               'Charing Cross Road by Helene Hanff','Above the Dark Circus by Hugh Walpole','The Accidental Tourist by Anne Tyler',
               'The Adventures of Huckleberry Finn by Mark Twain','The Age of the Cathedrals: Art and Society',
               '980-1420 by Georges Duby','The Alexandria Quartet by Lawrence Durrell','I Am Legend by Richard Matheson',
               "Amiel's Journal by Henri Frédéric Amiel",'Among the Believers: An Islamic Journey by V. S. Naipaul',
               'On Mulberry Street','Maths Puzzle by Das Gupta','The Maths of our life by Anjana Mitra']
        for i in range(0,random.randint(10,15)):
            print(books[random.randint(0,len(books)-1)])
            da=[20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,
                41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60]
            print('The book will be donated in',da[random.randint(20,59)],'days')
    if ad=='5':
        break

        
