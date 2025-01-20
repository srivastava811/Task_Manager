import pandas as pd
def load_tasks(username):
    #Load tasks of a specific user
    csv_file_name=f'tasks_{username}.csv'
    try:
        df=pd.read_csv(csv_file_name)
        print("Tasked loaded successfully !")
    except FileNotFoundError:
        print(f"No saved tasks found for {username}.")
        df=pd.DataFrame(columns=["Task ID","Description","Status"])
    return df

def save_tasks(df,username):
    # Save tasks to the user's CSV file
    csv_file_name=f'tasks_{username}.csv'
    df.to_csv(csv_file_name,index=False)
    print("Task saved successfully !")

def add_task(df, username):
    if not df.empty:
        task_id=df['Task Id'].max()+1
    else:
        task_id=1

    description=input("Enter Task Description : ")
    new_task=pd.DataFrame([[task_id,description,"Pending"]],columns=["Task ID","Description","Status"])
    df=pd.concat([df,new_task],ignore_index=True)
    save_tasks(df,username)
    print(f"Task '{description}' added with Task ID: {task_id}")
    return df

def view_tasks(df):
    if df.empty:
        print("No task found !")
    else:
        print("\nYour Tasks : ")
        print(df[["Task ID","Description","Status"]])

def mark_task_complete(df,username):
    try:
        task_id=int(input("Enter the task ID to be marked as complete : "))
        if task_id in df['Task ID'].values:
            df.loc[df['Task ID']==task_id, 'Status']='Complete'
            # save changes to user's file
            save_tasks(df,username)
            print(f"Task ID {task_id} marked as complete.")
        else:
            print(f"Task ID {task_id} not found.")
    except ValueError:
        print("Invalid Task ID !")
    return df

def delete_task(df,username):
    try:
        task_id=int(input("Enter the task ID to delete : "))
        if task_id in df['Task ID'].values:
            df=df[df['Task ID']!=task_id]
            #save changes to user's task file
            save_tasks(df,username)
            print(f"Task ID {task_id} deleted.")
        else:
            print(f"Task ID {task_id} not found.")
    except ValueError:
        print("Invalid Task ID")
    return df