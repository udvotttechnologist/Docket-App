import psycopg2
from firebase_admin import credentials, storage, initialize_app
import string
import secrets
import requests
import database_handling
import offline_file_handling as ofh
import os
import random

#gmail account login credentials for mail sending process
sender_email = "docketauthority@gmail.com"
sender_password = "dcktqcfzxihadsyv"

#firebase account authentication file(json format)
service_account_dict = {
    "type": "service_account",
    "project_id": "docket-d857d",
    "private_key_id": "07e2acb4a10d66b230ccbcb6087bcaabc2aca094",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCVD5L3eIFOv1Pu\nnvoi+KhSH8mnFNWAXwX8D+OSf5PNGupHxzjg4jwdbyT27+G11w7KOqTpVoS3uDp1\n1rgCNdYGgjGVb7tOHr1KKWIIzZBsd9rM6QqU+iz6lmpcS51hVdx36urgDu/Fk0Uw\n7Fg2KeSdSDmxV7Ny7VYENyT5X4gMqydGPC4LzA2HL7urrBEFFQGqHWRGM+U29chP\n6YcFh6Jxn5lPakhr94diRSZLryJq6Q3wtVG6lEK/ealQGsMVT9sYAh1Qh2gk+otP\ne3EdssHbthYJPddg5qbC5oUKlvMhI5/ASUwNZsevuqB0ijhdzBCb6fRU1BhqAjDC\nZCdMQKF7AgMBAAECggEAK5VEKWtok3fJuKlvBa6iuHBm651h14jxHQQgTANVWdEW\n0yni7Y34ebq3miQFYL+iqWqAMWGEqJsLLM09PBg1ne2PRdxHbc37FqYG7f/8zFo2\n9VbmKy0C3boBGz9Yos8SCVX8msqDPMeUoXtZR2z0VTB6/elgpKfUUKM3Alr2Uo1+\nInhPUju6TDHs63XzrEYJg0TRCCHOMWT4inQ5Y48qep8Mi//2g9Cfy8ygAtHBhAo9\nrDdHPzHx60/IeD0Z4kDBmwWeLYRLEJ8hPujxS384o+C2TxuyejjOz2opSK1A7RWY\nSTolx60f/npajaSzflkvT6/FD7MtlGNncpqZRidOcQKBgQDOnvyFmtpNHf+1ltpq\nEnDlrWM1C4q6MdZFWWpZE+GAF/4HoMkFZlq1rv5TcXZ3udFK0+gw13Vd76XGsAZN\nRzk0YIMjLyPR37tGFqd84WyRIamkFRmjjd+5Gq3imkPl00cXEjPtoyL+eFBFAtH3\nXFqzACMtGh0TN+b/u5uzOiUAzwKBgQC4rxJRVAUQEBoEx7+FaWnPZDwCwVDvjZB0\nuqKBO06uOtRtb7mtNVhebS+G171TKUfVn4AoGFtYYkE5fYK0EflsBFM4nL8zV65Y\nZ/VuT6pp3XzFiOpwuCFJaLj8ZG1SlVsjuPqwckuXrwjDfXx+a3vRSuHIHkFiPS6D\nDi8ICJaHlQKBgQCKDVgTvJ9XH1AW+C/+50tfajX63zdVqK7NryyLT+k/OMiWOCuX\n3AeHlOCAyDKrVBAuut9MoujcVp6g3kOXpprmEAYOoBSCycXK0qAdpFBxt9gstZxn\n1wdAGj9MRF5RVJUPKS5g/LsI40Jemb/IUoCXUOQv4l7C1HsXKzagzZyjqQKBgQCq\nHWFDFqB/NkWxJ4kry3iSdyKr6wOxVPW9//gWD9oetMPddi9S87NNb0d67phO1NR9\nWqlCxYTGeeLYoNrXIUNdkvJRUFjyYw6OElxJWwp+72yxy7cfUwweQV875QmqKzdD\nRW1tQCqPMsRgxeL50+m+VDp7Chtx8Sc5wsPho398rQKBgBsckBS8GA06o9+66+WY\nOdHJX7ypkFPtt/u/vs2kawSYDRMfOSGmuc5xoGEh0lR/EFvz+6Mispv+fPYFIXFI\n8OndfZ9Fed1RXgDzKsuLFQ9mdNnU0y8fJKKemqDugllZT9KeLxjUBptAr//uq7mQ\nFQlunY/USw+omMFmMwrLSpAM\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-rsdjf@docket-d857d.iam.gserviceaccount.com",
    "client_id": "103053631239698156398",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-rsdjf%40docket-d857d.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
}
cred = credentials.Certificate(service_account_dict) #connecting the firebase authentication into firebase-sdk module

#Calling the storage bucket
initialize_app(cred, {
    'storageBucket': 'docket-d857d.appspot.com'})

#the user authentication database of supabase platform which have the PostgreSQL
host = "db.zchhatbxymoarixuwoqn.supabase.co"
port = 5432
database = "postgres"
user = "postgres"
password = "Docket+Access+Database+*2345#"

def get_time(): #getting the device time which is used for 'sign in' and 'sign out' info
    import datetime

    # Get the current date and time
    current_datetime = datetime.datetime.now()
    # Format the current date and time
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_datetime


def security_key(length):
    characters = string.ascii_letters + string.digits  # Include both letters and digits
    random_key = ''.join(random.choice(characters) for _ in range(length))
    return random_key


def security_check(otp_phrase, check_phrase): #checks the otp phrase, currently not using in this python code, same thing is being used in registration_ui.py
    if otp_phrase == check_phrase:
        return 'succeed'
    else:
        return 'failed'


def mail_send(sub, mail, message): #Function to send mail to desired email that user has used
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    receiver_email = mail
    subject = sub

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'html'))

    # Connect to Gmail's SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    # sign_in_login to your Gmail account
    server.login(sender_email, sender_password)

    # Send the email
    server.sendmail(sender_email, receiver_email, msg.as_string())

    # Quit the server
    server.quit()

    return "A mail sent to :" + mail + "  Kindly Check your Mail."


def check_exist(mail): # Checks if the email does exist or not in our user database
    connect = psycopg2.connect(
        host=host,
        port=port,
        database=database,
        user=user,
        password=password
    )
    cursor = connect.cursor()
    q = "SELECT COUNT (*) FROM user_list WHERE email = %s;"
    cursor.execute(q, (mail,))
    result = cursor.fetchone()
    return result[0]

def check_exist_uid(uid): # Checks if the uid does exist or not in our user database
    connect = psycopg2.connect(
        host=host,
        port=port,
        database=database,
        user=user,
        password=password
    )
    cursor = connect.cursor()
    q = "SELECT COUNT (*) FROM user_list WHERE uid = %s;"
    cursor.execute(q, (uid,))
    result = cursor.fetchone()
    return result[0]


def register_user(name, email, psswrd): #Function that registers user
    exist = check_exist(email)
    otp = security_key(8)

    if exist == 0:
        sub = 'User Verification'
        message = """"<h2>Welcome to DOCKET - A daily planner</h2> 
        <h3>Here is your One Time Password, <b>OTP::</b></h3>
        <h2>
        """ + otp + """</h2><br><br>
        <p>Use it for user verification.</p>
        <p><br><b>Are you not "User"?</b> Then simply ignore this mail or complain to us.</p>
        <br>Thanks in Advanced!</br>
        """
        mail_send(sub, email, message)
        chek_otp = input("Enter the OTP:")
        verify = security_check(otp, chek_otp)

        if verify == 'succeed':
            uid = security_key(30)
            connect = psycopg2.connect(
                host=host,
                port=port,
                database=database,
                user=user,
                password=password
            )
            cursor = connect.cursor()
            query = """
            INSERT INTO user_list (name, email, pass, uid)
            VALUES (%s, %s, %s, %s,%s);"""
            val = (name, email, psswrd, uid)
            cursor.execute(query, val)
            connect.commit()

            return_value = ["User created!", "Your user id(UID) authentication code is: " + uid,
                            "Save it for future purpose"]

            confirmation_sub = "Welcome to Docket - A Daily Planner"
            confirmation_mail = """<h2 style = "color:blue">Hello """ + name + """</h>
            <br><br><h2>Your account has been created successfully. Your Docket user id(UID) authentication code is: """ + uid + """</h2>
            <br><h2>Save it for further uses.<br> </h2>
            <br> <h2 style="color:red">it may be necessary during the security purpose.</h2> 
            <br><h2>Thanks for using Docket! </h2>"""

            mail_send(confirmation_sub, email, confirmation_mail)

            return return_value

        elif verify == 'failed':
            return 'Authentication Failed! Please try again!'

    else:
        return "The same email already exist in our database, try with another email"


def check_new_user(mail): #Checks if the user is new or not(mainly checks the user is logging first time or not)
    # calling the postgresql database
    connect = psycopg2.connect(
        host=host,
        port=port,
        database=database,
        user=user,
        password=password
    )
    cursor = connect.cursor()
    q = "SELECT status FROM user_list WHERE email = %s;"
    cursor.execute(q, (mail,))
    result = cursor.fetchone()
    return result[0]


def login_user(email, psswrd): #Function that logs in an existing user
    count = check_exist(email)
    # calling the postgresql database
    connect = psycopg2.connect(
        host=host,
        port=port,
        database=database,
        user=user,
        password=password
    )
    cursor = connect.cursor()
    if count == 1:
        query = "select pass from user_list where email=%s;"
        cursor.execute(query, (email,))
        stored_hash = cursor.fetchone()
        if (stored_hash[0] == psswrd):
            time = get_time()
            query = "UPDATE user_list SET sign_in_log = %s WHERE email =%s;"
            cursor.execute(query, (time, email,))
            connect.commit()
            return "Succesfully logged in"

        else:
            return "Login Failed! Try with different Email or Password"
    else:
        return "This email does not exist. Please Register."

def sign_in_status(email): #Set the user sign in status into the database
    # calling the postgresql database
    connect = psycopg2.connect(
        host=host,
        port=port,
        database=database,
        user=user,
        password=password
    )
    cursor = connect.cursor()
    query = "UPDATE user_list SET status= 'Signed In' WHERE email =%s;"
    cursor.execute(query, (email,))
    connect.commit()


def sign_out_status(uid): #Set the user sign out status into the database
    # calling the postgresql database
    connect = psycopg2.connect(
        host=host,
        port=port,
        database=database,
        user=user,
        password=password
    )
    cursor = connect.cursor()
    query = "UPDATE user_list SET status= 'Signed Out' WHERE email =%s;"
    connect.commit()
    time = get_time()
    query = "UPDATE user_list SET sign_out_log = %s WHERE uid =%s;"
    cursor.execute(query, (time, uid,))
    connect.commit()


def fetch_user_data(email): #Fetches all user data using email from the database
    # calling the postgresql database
    connect = psycopg2.connect(
        host=host,
        port=port,
        database=database,
        user=user,
        password=password
    )
    cursor = connect.cursor()
    query = "select * from user_list where email =%s;"
    cursor.execute(query, (email,))
    count = cursor.fetchone()
    return count

def fetch_user_info(uid):
    # calling the postgresql database
    connect = psycopg2.connect(
        host=host,
        port=port,
        database=database,
        user=user,
        password=password
    )
    cursor = connect.cursor()
    query = "select * from user_list where uid =%s;"
    cursor.execute(query, (uid,))
    count = cursor.fetchone()
    return count

def set_new_user_log(uid): #Sets the user log as new user after registration
    # calling the postgresql database
    connect = psycopg2.connect(
        host=host,
        port=port,
        database=database,
        user=user,
        password=password
    )
    cursor = connect.cursor()
    query = "UPDATE user_list SET status = 'New_User' WHERE uid =%s;"
    cursor.execute(query, (uid,))
    connect.commit()


def check_internet(): #Checks if the internet connection does exist or not
    try:
        # Send a GET request to a well-known website (e.g., google.com)
        response = requests.get("http://www.google.com", timeout=5)
        # If the response status code is 200, the internet connection is available
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.ConnectionError:
        # If an exception is raised, there is no internet connection
        return False


def sync_online(file_name): #uploads the whole offline database(sqlite3) into firebase bucket using the unique id of each user
    bucket = storage.bucket()
    blob = bucket.blob(file_name)
    blob.upload_from_filename(file_name)


def download_online(file_name): #Downloads the whole offline database(sqlite3) from firebase bucket using the unique id of each user
    bucket = storage.bucket()
    blob = bucket.blob(file_name)
    if blob.exists():
        blob.download_to_filename(file_name)

    #os.makedirs('resources', exist_ok=True)
    #download()


def download():
    # Initialize Firebase Storage client
    bucket = storage.bucket()

    # Define the Firebase Storage folder to download from
    folder_name = 'resources/'

    # Define the local folder where you want to save the downloaded files
    local_folder = './resources/'

    # List files in the Firebase Storage folder
    blobs = bucket.list_blobs(prefix=folder_name)

    # Download each file to your local folder
    for blob in blobs:
        # Extract the file name from the full path
        file_name = blob.name.split('/')[-1]


        # Download the file to your local folder
        blob.download_to_filename(file_name)
        print(f"Downloaded: {file_name}")

    print("All files downloaded successfully.")

def change_password(email,password_text):
    # calling the postgresql database
    connect = psycopg2.connect(
        host=host,
        port=port,
        database=database,
        user=user,
        password=password
    )
    cursor = connect.cursor()
    query = "UPDATE user_list SET pass = %s WHERE email =%s;"
    cursor.execute(query, (password_text,email,))
    connect.commit()


def push_device_info(email): #Pushes the device info into our user database
    import platform
    import json
    #gets the system info
    system_info = platform.uname()
    #creating a dictionary variable
    device_info ={
        'System': system_info.system,
        'Node': system_info.node,
        'Release': system_info.release,
        'Version': system_info.version,
        'Machine': system_info.machine,
        'Processor': system_info.processor
    }
    #appending the dictionary variable into json format
    platform_data = json.dumps(device_info)

    #calling the postgresql database
    connect = psycopg2.connect(
        host=host,
        port=port,
        database=database,
        user=user,
        password=password
    )
    cursor = connect.cursor()
    #SQL syntax to push the json variable into the 'platform' column for dedicated email
    query= "UPDATE user_list SET platform = %s WHERE email =%s;"

    #Executing the SQL query
    cursor.execute(query, (platform_data,email))
    # Commit the transaction
    connect.commit()
    # Close the cursor and connection
    cursor.close()