from EmpolyeeSys import *
from Admin import *
                     
        
while(True):
    Choice = 0

    #AdminLogIn()
    
    
    while(Choice != '5'):
        print("=" * 35)
        print("To print employee data press  \"1\"")
        print("To add employee data press    \"2\"")
        print("To remove employee data press \"3\"")
        print("To show employees IDs press   \"4\"")
        print("To logout press               \"5\"")
        
        print("=" * 35)
        Choice=input("Enter choice:\n")
        if(Choice == '1'):
            printEmployee()
        elif(Choice == '2'):
            AddEmployee()
        elif(Choice == '3'):
            RemoveEmployee()
        elif(Choice == '4'):
            PrintIDs()
        elif(Choice == '5'):
            print("Bye, See you soon")
        else:
            print("Invalid choice")