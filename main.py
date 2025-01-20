from user_authentication import Register,Login
from task_opern import task_manager
def main():
    while True:
        choice=input("1. Register\t 2. Login\t 3. Exit\n")

        if choice=="1":
            Register()
        elif choice=="2":
            username=Login()
            if username:
                task_manager(username)
        elif choice=="3":
            print("Exiting the application !")
            break
        else:
            print("Invalid choice. Please try again.")
main()