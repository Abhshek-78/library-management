import os 
l1=["EnginneringMathematics","digital system","python","c programming","data structure"]
print("Welcome to the bookself")
def checkbook():
    book = input("enter book name")
    if book in l1:
        buy() 
    else:
        print("book is not available")
def buy():
    print("book is available")
    print("book self is \n",l1)
    name=int(input("enter the book self address star from 0 "))
    l1[name]
    del l1[name]
    print("book is successfully issue")
    print("remaining book",l1)
    
def returnbook():
    bkrtn=input("which book you want to return")
    if bkrtn in l1:
        print("book is already in the list")
    else:
        l1.append(bkrtn)
        print("book is returned")
def fine():
    price = 20
    inidt = int(input("Enter the issue date: "))
    smtdt = int(input("Enter the return date: "))
    days = smtdt - inidt
    if days > 15:
        fine = 0
        for i in range(days - 15):
            fine += 10
        final_amount = price + fine
        print("Final amount to be paid: ", final_amount)
    else:
        print("Final amount to be paid: ", price)
def decore():
    print("***********************")
    print("-----,-----")
    print("||---|-b-||")
    print("||-a-|---||")
    print("||---|-c-||")
    print("-----'-----")
    print("--Library Management--")
    print("Created by: Abhishek")
def start():
    print("choose the task:\n"\
         "1.buy\n"\
         "2.return\n"\
          "3.exit\n"\
     )

for i in range(3):
    decore()
    start()
    chioce=int(input("enter the choice"))
    if chioce==1:
        checkbook()
        
    elif chioce==2:
         returnbook()
         fine()
    elif choice==3:
        os.exit()
    else:
        print("Invalid choice")
