from Table import *


while(True):
    
    print("*" * 40)
    print("To add task press          \" 1 \"")
    print("To remove task press       \" 2 \"")
    print("To print to do tasks press \" 3 \"")
    print("To print done tasks press  \" 4 \"")
    print("To load to do tasks press  \" 5 \"")
    print("To load done tasks press   \" 6 \"")
    print("To save tasks press        \" 7 \"")
    print("To exit press              \" 8 \"")
    print("*" * 40)
    Choice = input("")
    if(Choice == '1'):
        AddTable()
    elif(Choice == '2'):
        DoneTask()
    elif(Choice == '3'):
        PrintToDo()
    elif(Choice == '4'):
        PrintDone()
    elif(Choice == '5'):
        ReadToDo()
    elif(Choice == '6'):
        ReadDone()
    elif(Choice == '7'):
        SaveToDoList()
        SaveDoneList()
    elif(Choice == '8'):
        CloseFiles()
        print("Bye, Closing the program")
        break
    else:
        print("Invalid choice")
        
    