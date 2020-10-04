Empolyees_Dict={
    "12345"  : {
        "Name"  : "Eslam Ehab Aboutaleb",
        "ID"    : "12345",
        "Salary": "99999999"
    },
    "12312"  : {
        "Name"  : "Somebody Works Here",
        "ID"    : "12312",
        "Salary": "2000"
    }
}

OldEmployeesList= list()
EmployeeID_Length = 5
   

def AddEmployee():
    # Flag to check if ID mets the ID requirements
    EmployeeID_Check = 0
    
    EmployeeName  = input("Enter employee name\n")
    length = len(EmployeeName.split())
    
    while(length < 3):
        EmployeeName  = input("Enter full name(First, mid, last) using alphabetic charcters only\n")
        length = len(EmployeeName.split())
        print(length)
    EmployeeName  = EmployeeName.capitalize().strip()
    
    EmployeeID    = input("Enter employee ID\n")
    
    while EmployeeID_Check == 0:
        while((EmployeeID.isnumeric()==False) or (len(EmployeeID) != EmployeeID_Length) ):
            EmployeeID = input("Please enter employee ID as five numbers\n")
        EmployeeID_Check = 1
        if((EmployeeID in Empolyees_Dict.keys())or (EmployeeID in OldEmployeesList)):
            while((EmployeeID in Empolyees_Dict.keys()) or (EmployeeID in OldEmployeesList)):
                EmployeeID = input("ID is already found,Enter another employee ID\n")
            if((EmployeeID.isnumeric()==False) or (len(EmployeeID) != EmployeeID_Length) ):
                EmployeeID_Check = 0
            else:
                EmployeeID_Check = 1
            
    EmplyeeSalary = input("Enter employee salary\n")
    while(EmplyeeSalary.isnumeric() == False):
        EmplyeeSalary = input("Enter salary in numbers")
        
    Employee      = {"Name"  :EmployeeName
                    ,"ID"    :EmployeeID,
                     "Salary":EmplyeeSalary
                    }
    #add new employee dict in employees dict
    Empolyees_Dict[EmployeeID] = Employee

def printEmployee():
    EmployeeID = input("Enter employee ID\n")
    if(EmployeeID not in Empolyees_Dict):
        print("There is no employees with this ID")
        return
    print(Empolyees_Dict[EmployeeID])

def PrintIDs():
    for EmployeeKey,EmployeeVal in Empolyees_Dict.items():
        print(f"Empolyee {EmployeeKey} Name:{EmployeeVal['Name']}")

def RemoveEmployee():
    EmployeeID = input("Enter employee ID\n")
    if(EmployeeID not in Empolyees_Dict):
        print("There is no employees with this ID")
        return
    OldEmployeesList.append(EmployeeID)        
    Empolyees_Dict.pop(EmployeeID)
    
    print(f"Empolyee with ID:{EmployeeID} is removed")
