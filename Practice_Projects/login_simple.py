import getpass


def create_account(userlist):
    username = input("Enter Your Username: ")
    password = getpass.getpass("Enter Your Password: ")
    userlist.append((username, password))
    print(f"Welcome to the community: {username}")
    return True


def login(userlist):
    username = input("Enter Your Username: ")
    password = getpass.getpass("Enter Your Password: ")
    if (username, password) in userlist:
        print(f"Welcome back {username}")
        return True
    else:
        print("Invalid Credentials")
        return False


user_list = [('shadow', '1234')]

print("Welcome User")
while True:
    try:
        option = int(input("1.Login \n"
                           "2.Sign Up\n"
                           "3.Exit: "))
    except ValueError:
        print("Please Enter a valid number")
        continue
    if option == 1:
       if login(user_list):
        break
    elif option == 2:
       if create_account(user_list):
        break
    elif option == 3:
        print("Goodbye")
        break
    else:
        print("Invalid Option, Please enter a valid number")
