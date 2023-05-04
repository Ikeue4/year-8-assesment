'''
== DOCUMENTAION == 

    == OVER VIEW == 
    This code sets up a Flask server with several routes for handling user data. It first checks if necessary libraries are installed and prompts the user to create 
    two files for storing data. It then defines routes for sending and receiving user data, including checking passwords, writing new passwords, updating user scores, 
    and changing user classes.

    == HOW TO FIX == 
    1. Import Error: this could be because of a library is not installed
        1.1. Fix pip install package_name
        1.2. Or install package_name --upgrade 

    2. FileNotFoundError: 
        2.1. Check that file names and directories are right  
        2.2. Check that template_folder is right should be where the html files are 

    3. Chat server full 
        3.1. Add new servers by copping the code but the servers should sort clear automatically 
        3.2. You can restart the server to clear the chats or if there is no one in the chat 

    4. Html status errors
        4.1. If 404 end of the address in not right 
        4.2. If 304 Indicates that the resource has not been modified since the version specified by the request headers If-Modified-Since or If-None-Match. In such case, 
             there is no need to retransmit the resource since the client still has a previously-downloaded copy. 
        4.3. If >500 see what the directory is and then see if there is anything wrong 
        4.4. Any other errors go to https://en.wikipedia.org/wiki/List_of_HTTP_status_codes

    == API == 
    How to use the API in your own programs:

        1. Import requests you might need to pip install it

        2.Start off by ping the server with  
            Response = requests.get("http://localhost:5000/ping")
            Server = response.text 
            Print(server) 

        3. Next you need to understand how the servers work. For most of the functions you need to give the name and sometimes the password this allows the server to identify the user. 

        4.Lets say that you want to make see what level a account is first you will have to assine the data that will be sent this can be done like this  
            Data_N = { 
                    "name": name, 
                    "password": password 
                } 
                response = requests.post<strong>("http://localhost:5000/send_data_level", json=data_N)</strong> 
            Server = response.text 
            Print(server) 

        5. This is the basic way that the server work but there are exceptions to this

'''
try:
    """
    This code block is checking if certain libraries are installed. It checks for Flask, sys, random, and flask_cors. If any of these libraries are not installed, it prints a message indicating that the library is not installed. If the library is installed, it prints a message indicating that the library is installed.
    """
    from flask import Flask, request, jsonify, make_response, render_template, send_file, Response
    import io
    print ("flask installed ✔")
except ImportError:
    print("The flask library is not installed ✘")

try:
    import sys
    print ("sys installed ✔")
except ImportError:
    print("The sys library is not installed ✘")

try:
    import random
    print ("random installed ✔")
except ImportError:
    print("The random library is not installed ✘")

try:
    from flask_cors import CORS
    print ("flask_cors installed ✔")
except ImportError:
    print("The flask_cors library is not installed ✘")

print("^_^")

while True:
    """
    This code prompts the user to create two files on their computer, one to hold passwords and profiles, and one to save quizzes that people upload. The user is asked if they want to proceed and if they enter "N", the program exits. If they enter "Y", the program continues. If they enter anything else, they are prompted to enter "Y" or "N" again.
    """
    createfile = input("This code needs to make two files on your computer: one to hold passwords and profiles, and one to save quizzes that people upload. This server can only be accessed from your computer and cannot be seen by other computers. Do you want to proceed? (Y/N)")
    if createfile.lower() == "n":
        sys.exit()
    elif createfile.lower() == "y":
        break
    else:
        print("Invalid input. Please enter Y or N.")

#setts variables
CS_1 = 0
CS_2 = 0
CS_3 = 0
CS1class = ""
CS2class = ""
CS3class = ""
chats1 = ""
chats2 = ""
chats3 = ""


"""
    Create a Flask application instance and enable Cross-Origin Resource Sharing (CORS).
    @param __name__ - the name of the application
    @param template_folder - the folder containing the HTML templates
    @param static_folder - the folder containing the static files (e.g. images, CSS, JS)
    @return The Flask application instance.
    """
app = Flask(__name__, template_folder='templates HTML', static_folder='images')
CORS(app)

"""
    This is a Flask route that receives a POST request with JSON data containing a name and password. It then checks if the name and password combination is present in a file called "passwords.txt". If it is, it returns a success message with a 200 status code. If it is not, it returns a failure message with a 300 status code.
    @return A success or failure message with a status code.
    """
@app.route("/send_data_log", methods=["POST"])
def send_data_P():
    data_P = request.get_json()
    formatted_string = "{}: {}".format(data_P['name'], data_P['password'])
    print(formatted_string)
    filename = "passwords.txt"
    name_to_check = formatted_string
    with open(filename, "r") as f:
        contents = f.read()
    if name_to_check in contents:
        print("{} is present in {}".format(name_to_check, filename))
        passwordvaild = "succses"
        return "succses", 200
    else:
        print("{} is not present in {}".format(name_to_check, filename))
        passwordvaild = "fail"
        return jsonify(passwordvaild), 300
    
"""
    This is a Flask route that receives a POST request with JSON data. The JSON data is expected to have a 'name' and 'password' field. The function extracts these fields from the JSON data, formats them into a string, and prints the string to the console. It then generates a random number between 100 and 1000, appends the formatted string and the random number to a file called "passwords.txt", and returns a success message with a 200 status code.
    """
@app.route("/send_data_log_new", methods=["POST"])
def send_data_NA():
    data_P_New = request.get_json()
    formatted_string = "{}: {}".format(data_P_New['name'], data_P_New['password'])
    print(formatted_string)
    random_number = random.randint(100, 1000)
    with open("passwords.txt", "a") as f:
        f.write("\n" + formatted_string + "; 0^ " + str(random_number))
    return "Data received and written to file", 200

"""
    This is a Flask route that returns the contents of a file named "scoretest.txt" when the "/send_file" endpoint is accessed.
    @return The contents of the file named "scoretest.txt"
    """
@app.route("/send_file")
def send_file():
    with open("scoretest.txt", "r") as f:
        contents = f.read()
    return contents

"""
    This is a Flask route that listens for a POST request to "/send_data_level". The request should contain JSON data with a "name" and "password" field. The function reads a file called "passwords.txt" and searches for a line that contains the formatted string "{name}: {password}". If found, it splits the line by ";" and extracts the last part. It then splits the last part by "^" and extracts the first part. This value is printed and returned. If the search string is not found, the function returns "Not Found".
    """
@app.route("/send_data_level", methods=["POST"])
def send_data_L():
    data_P_N = request.get_json()
    formatted_string = "{}: {}".format(data_P_N['name'], data_P_N['password'])
    filename = "passwords.txt"
    search_string = formatted_string
    with open(filename, "r") as file:
        for line in file:
            if search_string in line:
                parts = line.split(";")
                value = parts[-1].strip()
                parts = value.split("^")
                value1 = parts[0].strip()                
                print(value1)
                return value1
    return "Not Found"

"""
    This is a Flask route that receives a POST request with JSON data containing a name, password, and score. It then formats the data into a string and appends it to a file called "passwords.txt". If the name already exists in the file, it updates the score by adding the new score to the old score. Finally, it returns a success response. 
    @return A Flask response object.
    """
@app.route("/send_data_score", methods=["POST"])
def send_data_NL():
    data_P_NL = request.get_json()
    formatted_string = "{}: {}; {}^".format(data_P_NL['name'], data_P_NL['password'], data_P_NL['score'])
    filename = "passwords.txt"
    s = formatted_string
    result = s.split('; ')[1].split('^')[0]
    result1 = s.split('; ')[0]
    search_string = result1
    with open(filename, "r") as file:
        for line in file:
            if search_string in line:
                parts = line.split(";")
                value = parts[-1].strip()
                parts = value.split("^")
                value1 = parts[0].strip()                
                oldlev = int(value1)
                newlev = int(result)
                newprint = oldlev + newlev
                start = s.index(';') + 2
                end = s.index('^')
                result = s[:start] + str(newprint) + s[end:]
    with open(filename, 'r') as file:
        lines = file.readlines()
    for i in range(len(lines)):
        if result1 in lines[i]:
            # Replace the line with the new line
            lines[i] = result + "\n"
    with open(filename, 'w') as file:
        file.writelines(lines)      
    response = make_response("Success", 200)
    return response

"""
    This is a Flask route that receives data via a POST request and writes it to a file. The data is expected to be in JSON format and contain a name, password, and class. The function reads from a file called "passwords.txt" and searches for a line that matches the name and password in the received data. If a match is found, the class is updated and the file is rewritten with the updated information. The function returns a success message with a status code of 200.
    @return A success message with a status code of 200.
    """
@app.route("/send_data_new_class", methods=["POST"])
def send_data_C():
    data_P_new_C = request.get_json()
    formatted_string = "{}: {}".format(data_P_new_C['name'], data_P_new_C['password'])
    newclass = data_P_new_C['class']
    filename = "passwords.txt"
    search_string = formatted_string
    new_lines = []
    with open(filename, "r") as file:
        for line in file:
            if search_string in line:
                parts = line.split("^")
                value = parts[0].strip()
                new_lines.append("{}^ {}\n".format(value, newclass))
            else:
                new_lines.append(line)

    with open("passwords.txt", "w") as file:
        file.writelines(new_lines)

    return "Data received and written to file", 200

"""
    This is a Flask route that receives a POST request with JSON data containing a name and code for a new quiz. The function then formats the data into a string, writes it to a file named "quiz.txt", and returns a success message with a 200 status code.
    @return A success message with a 200 status code.
    """
@app.route("/send_data_new_quiz", methods=["POST"])
def send_data_Q():
    data_new_Q = request.get_json()
    formatted_string = "{}: {}".format(data_new_Q['name'], data_new_Q['code'])
    filename = "quiz.txt"
    print (formatted_string + '|')
    with open(filename, "a") as f:
        f.write('\n' + formatted_string + '\n|')
    return "succses", 200

"""
    This is a Flask route that reads data from a file named "quiz.txt" and searches for lines that start with the "^" character. It then extracts the first part of each line (before the "^" character) and appends it to a list called "values". If "values" is not empty, it returns the list. Otherwise, it returns the string "error".
    @return a list of values or the string "error"
    """
@app.route("/send_data_ask_quiz", methods=["GET"])
def send_data_AQ():
    filename = "quiz.txt"
    search_string = ("^")
    values = []
    with open(filename, "r") as file:
        for line in file:
            if search_string in line:
                parts = line.split("^")
                value = parts[0].strip()
                values.append(value)
    if values:
        return values
    else:
        return "error"

"""
    This is a Flask route that receives a POST request with JSON data containing a quiz. The quiz is extracted from the JSON data and formatted into a string. The quiz is then compared to a text file containing quizzes. If a matching quiz is found, the lines between the matching quiz and the next quiz (indicated by a "|" character) are extracted and returned as a string. The string is returned with a 200 status code.
    @return The quiz and a 200 status code
    """
@app.route("/send_data_quiz", methods=["POST"])
def send_data_WQ():
    data_new_WQ = request.get_json()
    formatted_string = "{}".format(data_new_WQ.get("quiz", "not found"))
    formatted_string = (formatted_string + ("^:"))
    print (formatted_string)
    filename = "quiz.txt"
    text = []
    with open(filename, "r") as file:
        for line in file:
            text.append(line)
    start_index = -1
    end_index = -1
    sendback_lines = []
    for line in text:
        if formatted_string in line:
            start_index = text.index(line)
        if "|" in line:
            end_index = text.index(line)
            if start_index != -1:
                for i in range(start_index + 1, end_index):
                    sendback_lines.append(text[i])

                start_index = -1
                sendback = '\n'.join(sendback_lines)
    return sendback, 200

"""
    This is a Flask route that receives a POST request with JSON data. It then extracts the name and password from the JSON data and searches for a matching entry in a file called "passwords.txt". If a match is found, it extracts a value from the line and uses it to search for another line in the file. If a match is found for the value, it extracts a substring from the line and appends it to a list of results. Finally, it returns a comma-separated string of the results.
    @return a comma-separated string of the results
    """
@app.route("/send_data_view_class", methods=["POST"])
def send_data_VC():
    data_new_VC = request.get_json()
    print(data_new_VC)
    formatted_string = "{}: {}".format(data_new_VC['name'], data_new_VC['password'])
    print(formatted_string)
    filename = "passwords.txt"
    text = []
    with open(filename, "r") as file:
        for line in file:
            text.append(line)  
    results = []
    for line in text:
        if formatted_string in line:
            parts = line.split("^")
            value = parts[1].strip()
            value = "^ " + value
            print(value)
    for line in text:
        if value in line:
            parts = line.split(":")
            people = parts[0].strip()
            s = line
            start = s.index(';') + 1
            end = s.index('^')
            substring = s[start:end]
            ret = people + ' ' + substring
            results.append(ret)
            print(results)
    return ', '.join(results)

"""
    This is a Flask route that receives data from a client and processes it. The data is expected to be in JSON format. The function first reads a file called "passwords.txt" and searches for a line that matches the name and password sent by the client. If a match is found, the function assigns the client to one of three "class servers" (CS_1, CS_2, or CS_3) based on availability and the class associated with the password. The function then increments the count for the chosen class server and returns the name of the server to the client. If all class servers are full, the function returns a message indicating that the servers are full and the client should wait.
    """
@app.route("/class_chat_open", methods=["POST"])
def send_data_CO():
    global CS_1
    global CS_2
    global CS_3
    global CS1class
    global CS2class
    global CS3class
    data_new_CH = request.get_json()
    print(data_new_CH)
    formatted_string = "{}: {}".format(data_new_CH['name'], data_new_CH['password'])
    print(formatted_string)
    filename = "passwords.txt"
    text = []
    with open(filename, "r") as file:
        for line in file:
            text.append(line)  
    for line in text:
        if formatted_string in line:
            parts = line.split("^")
            value = parts[1].strip()
            value
            print(value)
    if CS_1 == 0:
        CS1class = value
        CS_1 = CS_1 + 1
        print(CS_1)
        return "CS_1"
    elif CS1class == value:
        CS_1 = CS_1 + 1
        print(CS_1)
        return "CS_1"
    elif CS_2 == 0:
        CS2class = value
        CS_2 = CS_2 + 1
        print(CS_2)
        return "CS_2"
    elif CS2class == value:
        CS_2 = CS_2 + 1
        print(CS_2)
        return "CS_2"        
    elif CS_3 == 0:
        CS3class = value
        CS_3 = CS_3 + 1
        print(CS_3)
        return "CS_3"
    elif CS3class == value:
        CS_3 = CS_3 + 1
        print(CS_3)
        return "CS_3"
    else:
        print ("servers full")
        return "servers full pleses wait"

"""
    This is a Flask route that listens for POST requests on the "/CS_1" endpoint. When a POST request is received, it checks the global variable `CS_1`. If `CS_1` is 0, it initializes the global variable `chats1` to an empty string. If `CS_1` is not 0, it retrieves the JSON data from the request, formats it into a string, and appends it to the `chats1` variable. Finally, it returns the `chats1` variable.
    """
@app.route("/CS_1", methods=["POST"])
def send_data_CS1():
    global CS_1
    global chats1
    if CS_1 == 0:
        chats1 = ""
    else:
        data_new_chat = request.get_json()
        print (data_new_chat)
        formatted_string = "{}: {}".format(data_new_chat['user'], data_new_chat['mess'])
        print(formatted_string)
        global CS1class
        chats1 = chats1 + "\n" + formatted_string
        print (chats1)
        return chats1

"""
    This is a Flask route that listens for GET requests on the "/CS_1r" endpoint. When a GET request is received, it returns the value of the global variable "chats1".
    """
@app.route("/CS_1r", methods=["GET"])
def send_data_CS1r():
    global chats1
    return chats1

@app.route("/CS_2", methods=["POST"])
def send_data_CS2():
    global CS_2
    global chats2
    if CS_2 == 0:
        chats2 = ""
    else:
        data_new_chat = request.get_json()
        print (data_new_chat)
        formatted_string = "{}: {}".format(data_new_chat['user'], data_new_chat['mess'])
        print(formatted_string)
        global CS1class
        chats2 = chats2 + "\n" + formatted_string
        print (chats2)
        return chats2

@app.route("/CS_2r", methods=["GET"])
def send_data_CS2r():
    global chats2
    return chats2

@app.route("/CS_3", methods=["POST"])
def send_data_CS3():
    global CS_3
    global chats3
    if CS_3 == 0:
        chats3 = ""
    else:
        data_new_chat = request.get_json()
        print (data_new_chat)
        formatted_string = "{}: {}".format(data_new_chat['user'], data_new_chat['mess'])
        print(formatted_string)
        global CS1class
        chats3 = chats3 + "\n" + formatted_string
        print (chats3)
        return chats3

@app.route("/CS_3r", methods=["GET"])
def send_data_CS3r():
    global chats3
    return chats3

@app.route("/class_chat_close", methods=["POST"])
def send_data_COD():
    global CS_1
    global CS_2
    global CS_3
    global CS1class
    global CS2class
    global CS3class
    global chats1
    global chats2
    global chats3
    data_new_CH = request.get_json()
    print(data_new_CH)
    formatted_string = "{}: {}".format(data_new_CH['name'], data_new_CH['password'])
    print(formatted_string)
    filename = "passwords.txt"
    text = []
    with open(filename, "r") as file:
        for line in file:
            text.append(line)  
    for line in text:
        if formatted_string in line:
            parts = line.split("^")
            value = parts[1].strip()
            value
            print(value)
    if CS1class == value:
        CS_1 = CS_1 - 1
        print(CS_1)
        if CS_1 == 0:
            chats1 = ""
        return "bye" 
    elif CS2class == value:
        CS_2 = CS_2 - 1
        print(CS_2)
        if CS_1 == 0:
            chats1 = ""
        return "bye"       
    elif CS3class == value:
        CS_3 = CS_3 - 1
        print(CS_3)
        if CS_1 == 0:
            chats1 = ""
        return "bye"
    else:
        return "something went wrong"
    
@app.route("/ping", methods=["GET"])
def ping():
    ping = "!server up! running on http://127.0.0.1:5000"
    return ping, 200

@app.errorhandler(404)
def page_not_found(e):
    # Render the custom 404.html template with the 404 error message
    return render_template('404.html'), 404

@app.route('/image')
def get_image():
    with open('images/404.png', 'rb') as f:
        img_bytes = io.BytesIO(f.read())
    return send_file(img_bytes, mimetype='image/png')

@app.route('/home')
def htmlhome():
    return render_template('server.html')

@app.route('/doc/home')
def htmldocumentation():
    return render_template('dochom.html')

@app.route('/doc/homepage')
def htmldocumentationhompage():
    return render_template('hompage python.html')

@app.route('/doc/assesment')
def htmldocumentationassesment():
    return render_template('assessment.html')

@app.route('/doc/flask')
def htmldocumentationserver():
    return render_template('serverdoc.html')

@app.route('/doc/homepage/errors')
def htmldocumentationhompageerrors():
    return render_template('homepage errors.html')

@app.route('/doc/assesment/errors')
def htmldocumentationassesmenterrors():
    return render_template('assessment errors.html')

@app.route('/doc/flask/errors')
def htmldocumentationservererrors():
    return render_template('serverdoc errors.html')

@app.route('/doc/flask/api')
def htmldocumentationserverapi():
    return render_template('serverdoc api.html')


if __name__ == "__main__":
    app.run(debug=True)