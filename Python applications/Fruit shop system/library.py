# Author : Eslam Aboutaleb
# Date   : 28/9/2020

# Admin list
AdminList = ["Eslam","Ahmed"]
# passwords of the admins
AdminsPass= ["1234" ,"5678"]
# Fruits list
FruitList = ["Banana","Orange","Apple","Mango","Strawberry"]
# Prices list 
FruitPrice= [10 , 20 , 30 ,50 ,70 ]
# Create empty order list
OrderList = list()
# Create empty order prices list
OrderPrices = list()
# Global variable used as a total price
totalprice = 0

def AddSellerItems():
    Name = input("Enter fruit name\n")
    if(Name.isalpha() != True):
        print("You entered name not alphabetic, Please try again")
        return
    Name = Name.capitalize()
    try:
        price = int(input("Enter kilo price\n"))
    except:
        print("You entered strange symbols, Please try again with numbers")
        return
    FruitList.append(Name)
    FruitPrice.append(price)
    print("Your fruit is added")

def AddItem():
        global totalprice
        Flag =0
        Name=input("Enter name of the fruit\nchoices:{0}\n".format(FruitList))
        Name = Name.capitalize()
        for i in FruitList:
            if i == Name:
                Flag = 1
                break
        if(Flag != 1):
            print("Your order is not found")
            return
        kilos =input("Enter Number of kilos\n")
        
        if(kilos.isnumeric() == True):
            place = FruitList.index(i)
            kilos = float(kilos)
            if kilos > 0:
                price = FruitPrice[place] * kilos
                if(i in OrderList):
                    pass
                else:
                    OrderList.append(i)
                OrderIndex = OrderList.index(i)
                try:
                    if(OrderPrices[OrderIndex] > 0):
                        OrderPrices[OrderIndex] = OrderPrices[OrderIndex]+ price
                except:
                    OrderPrices.append(price)
                print("Your order is added")
                print ("Price will be" , price)
                totalprice = totalprice + price
                return
            else:
                print("Invalid quantity")
                return
        elif(kilos.isnumeric() == False):
            print("You entered strange symbols, Please try again with numbers")
            return
        
def PrintOrder():
        print("Orders: ")
        j = 0
        for i in OrderList:
            place = OrderList.index(i) 
            print("Fruit:",i ,"price:",OrderPrices[place],"LE")
            
        
        
  
def Choice():
    global totalprice
    
    print("To Creat a new order press \" 1 \"")
    print("To print your order press  \" 2 \"")
    print("To exit press              \" 3 \"")
    print("To add fruit press         \" 4 \"")
    print("To change settings press   \" 5 \"")
    Num = input("")
    if Num == '1':
        AddItem()
        return 0,0
    elif Num == '2':
        PrintOrder()
        return 0,0
    elif Num == '3':
        rePrice = totalprice
        totalprice = 0
        return 1,rePrice
    elif Num == '4':
        AdminName = input("Enter user naem\n")
        Place = AdminList.index(AdminName)
        if (AdminName == AdminList[Place]):
           PW = input("Enter pass\n")
           if(PW in AdminsPass):
                AddSellerItems()
           else:
                print("Wrong Pass")
        else:
            print("Wrong admin user name")
        
        return 0,0
    elif Num == '5':
        AdminName = input("Enter user name\n")
        if AdminName in AdminList:
           Place = AdminList.index(AdminName)
           PW = input("Enter pass\n")
           if(PW == AdminsPass[Place]):
                temp1 = input("Enter new password\n")
                temp2 = input("Enter password again\n")
                if temp1 == temp2:
                    AdminsPass[Place] = temp1
                    print("Password has been changed")
                else:
                    print("Passwords aren't match")
           else:
                print("Wrong Pass")
        else:
            print("Wrong admin user name")
            
        return 0,0
    else:
        print("Wrong choice")
        return 0,0


def CustomerChoice():
    global totalprice
    global password
    
    print("To Creat a new order press \" 1 \"")
    print("To print your order press  \" 2 \"")
    print("To exit press              \" 3 \"")
    Num = input("")
    if Num == '1':
        AddItem()
        return 0,0
    elif Num == '2':
        PrintOrder()
        return 0,0
    elif Num == '3':
        rePrice = totalprice
        totalprice = 0
        return 1,rePrice
    
