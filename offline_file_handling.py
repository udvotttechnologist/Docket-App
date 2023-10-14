import os


def create_and_insert_file(data):
    file_name = "user_data"
    with open(file_name, mode='w', newline='') as file:
        file.write(data[1])

    file_name2 = "user_name"
    with open(file_name2, mode='w', newline='') as file:
        file.write(data[2])

    file_name3 = "user_device"
    device_info = data[8]
    if isinstance(device_info, dict):  # Check if device_info is a dictionary
        formatted_dict = "<br>".join(f"{key}: {value}" for key, value in device_info.items())
    else:
        formatted_dict = "Error fetching Device info!"

    html_content = "<html><body><p>" + formatted_dict + "</p></body></html>"
    with open(file_name3, mode='w', newline='') as file:
        file.write(html_content)


def check_error():
    file_path = "user_data"
    file_path2 = "user_name"
    if os.path.exists(file_path):
        if os.path.exists(file_path2):
            return "exist"
        else:
            return "error"
    else:
        return "error"


def read_uid():
    file_name = "user_data"  # Replace with the path to your CSV file
    if check_error()=="exist": # Open the file for reading
        with open(file_name, mode='r') as file:
            file_contents = file.readline()
            return file_contents
    else:
        return "Error"
def read_uname():
    file_name = "user_name"  # Replace with the path to your CSV file
    if check_error() == "exist":  # Open the file for reading
        with open(file_name, mode='r') as file:
            file_contents = file.read()
            return file_contents
    else:
        return "Error"

def check_db_error():
    file_path = read_uid()
    if os.path.exists(file_path+".db"):
        return "exist"
    else:
        return "error"

