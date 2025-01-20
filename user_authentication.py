
import pandas as pd
import bcrypt

def save_users(users):
    # Save user data to CSV file
    csv_file_name='Users.csv'
    df=pd.DataFrame(users)
    df.to_csv(csv_file_name,index=False)
    print("User data saved successfully !")

def load_users():
    # Load user data from CSV file
    csv_file_name='Users.csv'
    try:
        df=pd.read_csv(csv_file_name)
        users=df.to_dict('records')
        print("User data loaded successfully !")
        return users
    except FileNotFoundError:
        print("No user found.")
        return []
    
def Register():
    # Load existing users
    users=load_users()

    # Prompt user to enter username and password
    username=input("Username : ")
    password=input("Password : ")

    # Check if the input username is already present
    if any(user['Username']==username for user in users):
        print("Username not available !")
        return
    
    # Hash/crypt the password
    hashed_password=bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    # Add new user to the list
    users.append({'Username':username, 'Password':hashed_password})

    # Save the new input to the CSV file. 
    # Save updated user list to CSV

    save_users(users)
    print("Registration Successful")


def Login():
    # Prompt user to enter username and password
    username=input("Username : ")
    password=input("Password : ")

    try:
        # Read the existing user data from CSV instead of excel
        df=pd.read_csv("Users.csv")
    except FileNotFoundError:
        # If file does not exist return a message
        print("No user registered !")
        return None
    
    # Check if username exist in the data
    check_user=df[df['Username']==username]
    if check_user.empty:
        print("User not registered")
        return None
    
    # If user exists, check if the password entered is correct

    check_password=check_user.iloc[0]['Password']
    if bcrypt.checkpw(password.encode('utf-8'), check_password.encode('utf-8')):
        print("Login Successfully !")
        return username
    
    else:
        print("Wrong Credentials !")
        return None