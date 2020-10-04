Admins = [["Eslam","123456"],["Admin","admin123"]]

def AdminLogIn():
    UserCheck = 0
    while(UserCheck == 0):
        Name = input("\nEnter user name\n")
        Name = Name.capitalize()
        for i in Admins:
            if Name == i[0]:
                Password = input("Enter password\n")
                if(Password == i[1]):
                    print(f"Hello {i[0]}")
                    UserCheck = 1
                    break
                else:
                    print("Wrong password")
                    break
            else:
                print("Wrong user name")
                break
