# Author : Eslam Aboutaleb
# Date   : 28/9/2020
from library import*
x = 0 
while(True):
    UserSelect = input("For admin Press \"0\"\nFor user press \"1\"\n") 
    if UserSelect == '0':
        while(x != 1):
            x,totalprice = Choice()
        if( x == 1):
            print("Quiting the system, Bye")
            if(totalprice != 0):
                print("Total price",totalprice)
            OrderList.clear()
        
    elif(UserSelect == '1'):
        while(x != 1):
            x,totalprice = CustomerChoice()
            if( x == 1):
                print("Quiting the order, Bye")
                if(totalprice != 0):
                    print("Total price",totalprice)
                OrderList.clear()
    x = 0
    

            
       
    
