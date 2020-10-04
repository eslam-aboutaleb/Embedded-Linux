from datetime import *

ToDo_Dict = {}
Done_Dict = {}


UnWantedCh = ['\'','\"','}',',','=']

ToDoFileName = "ToDo.txt"
DoneFileName = "Done.txt"

def CleanWord(str):
    for Index in UnWantedCh:
        str = str.replace(Index,'')
    return str

def AddTable():
    TaskPriority = input("Enter task priority\n")
    TaskChecker = 0
    while(TaskChecker == 0):
        if (TaskPriority in ToDo_Dict):
            TaskChecker = 0
            while (TaskPriority in ToDo_Dict):
                print("You already task with this priority")
                TaskPriority = input("Enter task priority\n")
                
        else:
            TaskChecker = 1 
        
    Task = input("Enter task\n")
    
    TimeHour = input("Enter hour\n")
    while(int(TimeHour) > 12):
        TimeHour = input("Enter reasonable hour\n")
    TimeMinutes = input("Enter minutes\n")
    while(int(TimeMinutes) > 59):
        TimeMinutes = input("Enter reasonable minutes\n")
    TaskDict = {
        "Task priority": TaskPriority,
        "Task"         : Task,
        "Hour"         : TimeHour,
        "Minutes"      : TimeMinutes
    } 
    ToDo_Dict[Task] = TaskDict

def DoneTask():
    TaskName = input("Enter task name\n")
    if TaskName in ToDo_Dict.keys():
        EndTime = input("Enter end hour\n")
        while(int(EndTime) > 12):
           EndTime = input("Enter reasonable hour\n")
           
        EndMinute = input("Enter end minutes\n")
        while(int(EndMinute) > 59):
           EndTime = input("Enter reasonable minutes\n")
        
        Done_Dict[TaskName] = { "Task"         :ToDo_Dict[TaskName].get("Task") ,
                                "Start clock"  :ToDo_Dict[TaskName].get("Hour"),
                                "Start minutes":ToDo_Dict[TaskName].get("Minutes"),
                                "End Time"     :EndTime,
                                "End minutes"  :EndMinute}
        ToDo_Dict.pop(TaskName)
        print("Task has been added to done list")
    elif(TaskName in DoneTask.keys()):
        print("You already added this task to done list")
    else:
        print("There is no task with this name")
    

def PrintToDo():
    for item,val in ToDo_Dict.items():
        print(item, "==>" , val)
        
def PrintDone():
    for item,val in Done_Dict.items():
        print(item, " ==> " , val)
    

def SaveToDoList():
    fileToDo = open("ToDo.txt",'w')
    for item,val in ToDo_Dict.items():
        ItemStr = str(item) + " ==> " + str(val)+"\n"
        fileToDo.write(ItemStr)
    #Close the file at the end of program

def SaveDoneList():
    fileDone = open("Done.txt",'w')
    for item,val in Done_Dict.items():
        ItemStr = str(item) + " ==> " + str(val)+"\n"
        fileDone.write(ItemStr)
    #Close the file at the end of program
        
def ReadToDo():
    try:
        fileToDo = open(ToDoFileName,'r')
    except:
        print("You should save any data first")
        return
    Dict = {}
    string = ''
    LinesList = fileToDo.readlines()
    for i in LinesList:
        words = i.strip().split()
        
        TaskName = CleanWord(words[0])
        Priority = CleanWord(words[4])
        Hour     = CleanWord(words[8])
        Minutes  =CleanWord(words[10])
        
        Dict     = {
        "Task"          : TaskName,
        "Task priority" : Priority,
        "Hour"          : Hour,
        "Minutes"       : Minutes
        }
        ToDo_Dict[TaskName] = Dict


def ReadDone():
    try:
        fileDone = open(DoneFileName,'r')
    except:
        print("You should save any data first")
        return
    Dict = {}
    Line = fileDone.readlines()
    for i in Line:
        words    = i.strip().split()
        TaskName = CleanWord(words[0])
        Priority = CleanWord(words[4])
        Hour     = CleanWord(words[8])
        Minutes  =CleanWord(words[10])
        
        Dict     = {
        "Task"          : TaskName,
        "Task priority" : Priority,
        "Hour"          : Hour,
        "Minutes"       : Minutes
        }
        Done_Dict[TaskName] = Dict

def CloseFiles():
    fileToDo = open(ToDoFileName)
    fileDone = open(DoneFileName)
    fileToDo.close()
    fileDone.close()