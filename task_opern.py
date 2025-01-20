from task_manager_fns import load_tasks,add_task,save_tasks,delete_task,view_tasks,mark_task_complete

def task_manager(username):
    df=load_tasks(username)

    while True:
        print(f"\nWelcome, {username}! Select an option : ")
        manage=int(input("1. Add Task\t 2. View Tasks\t 3. Mark Task Complete\t 4. Delete Task\t 5. Logout\n"))

        if manage==1:
            df=add_task(df,username)
            save_tasks(df,username)
        elif manage==2:
            view_tasks(df)
        elif manage==3:
            mark_task_complete(df,username)
            save_tasks(df,username)
        elif manage==4:
            df=delete_task(df,username)
            save_tasks(df,username)
        elif manage==5:
            print("Logging out.")
            break
        else:
            print("Invalid !")