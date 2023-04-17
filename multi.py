import threading
import time
import requests
from flask import Flask, request, jsonify


def function_1():
    for i in range(1):
        try:
            from flask import Flask, request, jsonify, make_response
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
            createfile = input("This code needs to make two files on your computer: one to hold passwords and profiles, and one to save quizzes that people upload. This server can only be accessed from your computer and cannot be seen by other computers. Do you want to proceed? (Y/N)")
            if createfile.lower() == "n":
                sys.exit()
            elif createfile.lower() == "y":
                break
            else:
                print("Invalid input. Please enter Y or N.")

        CS_1 = 0
        CS_2 = 0
        CS_3 = 0
        CS1class = ""
        CS2class = ""
        CS3class = ""
        chats1 = ""
        chats2 = ""
        chats3 = ""

        app = Flask(__name__)
        CORS(app)

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
            
        @app.route("/send_data_log_new", methods=["POST"])
        def send_data_NA():
            data_P_New = request.get_json()
            formatted_string = "{}: {}".format(data_P_New['name'], data_P_New['password'])
            print(formatted_string)
            random_number = random.randint(100, 1000)
            with open("passwords.txt", "a") as f:
                f.write("\n" + formatted_string + "; 0^ " + str(random_number))
            return "Data received and written to file", 200


        @app.route("/send_file")
        def send_file():
            with open("scoretest.txt", "r") as f:
                contents = f.read()
            return contents

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

        @app.route("/send_data_new_quiz", methods=["POST"])
        def send_data_Q():
            data_new_Q = request.get_json()
            formatted_string = "{}: {}".format(data_new_Q['name'], data_new_Q['code'])
            filename = "quiz.txt"
            print (formatted_string + '|')
            with open(filename, "a") as f:
                f.write('\n' + formatted_string + '\n|')
            return "succses", 200

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
            results = []
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
            results = []
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

        if __name__ == "__main__":
            app.run()

def function_2():
    for i in range(1):
        try:
            import requests
            print ("\033[32mrequests installed ✔\033[0m")
        except ImportError:
            print("\033[The requests library is not installed ✘\033[0m")

        try:
            import ast
            print ("\033[32mast installed ✔\033[0m")
        except ImportError:
            print("\033[The ast library is not installed ✘\033[0m")

        try:
            import sys
            print ("\033[32msys installed ✔\033[0m")
        except ImportError:
            print("\033[The sys library is not installed ✘\033[0m")

        try:
            import time
            print ("\033[32mtime installed ✔\033[0m")
        except ImportError:
            print("\033[The time library is not installed ✘\033[0m")

        #checks to see if they are new or not
        #problem you only need one charater in a paswerd

        response = requests.get("http://localhost:5000/ping")
        server = response.text
        print("\033[32m" + server, "\033[32m✔\033[0m")


        print("^_^")

        while True:
            hasacc = input("Do you have an account Y/N? ")
            if hasacc.upper() == "Y":
                time.sleep (1)
                name = input("What is your name? ")
                password = input("What is your password? ")
                data_P = {
                    "name": name,
                    "password": password
                }
                response = requests.post("http://localhost:5000/send_data_log", json=data_P)
                if response.status_code == 200:
                    print("Password validation status received")
                    # You can extract the password validation status from the response text
                    password_validation_status = response.text
                    print (password_validation_status)
                    break
                else:
                    print ("password or name is incorrect please try again or make a account")
                time.sleep (1)
            elif hasacc.upper() == "N":
                while True:
                    WAP = input("Do you want to make an account? Y/N? ")
                    if WAP.upper() == "Y":
                        name_new = input("What is your name? ")
                        password_new = input("What would your password be? ")
                        data_P_New = {
                            "name": name_new,
                            "password": password_new
                        }
                        response = requests.post("http://localhost:5000/send_data_log_new", json=data_P_New)
                        password_validation_status = "succses"
                        break
                    elif WAP.upper() == "N":
                        print("most functions will break work")
                        break
                    else:
                        print("enter Y/N")
                    
            else:
                print("Enter Y/N")

        if password_validation_status == ("succses"):
            lev0 = ("[░░░░░░░░░░]")
            lev1 = ("[█░░░░░░░░░]")
            lev2 = ("[██░░░░░░░░]")
            lev3 = ("[███░░░░░░░]")
            lev4 = ("[████░░░░░░]")
            lev5 = ("[█████░░░░░]")
            lev6 = ("[██████░░░░]")
            lev7 = ("[███████░░░]")
            lev8 = ("[████████░░]")
            lev9 = ("[█████████░]")
            lev10 = ("[██████████]")


            while True:
                WhatToDo = input("-------------------------------\nUSER OPTIONS\n-------------------------------\nprofile\njoin class\nview class members\nmake quiz\ndownload/play quiz\nquit\nchat\n")
                if WhatToDo == ("profile"):
                    data_N = {
                        "name": name,
                        "password": password
                    }
                    response = requests.post("http://localhost:5000/send_data_level", json=data_N)

                    level = response.text
                    levelprogres = lev0
                    if response.text == "1":
                        levelprogres = lev1
                    elif response.text == "2":
                        levelprogres = lev2
                    elif response.text == "3":
                        levelprogres = lev3
                    elif response.text == "4":
                        levelprogres = lev4
                    elif response.text == "5":
                        levelprogres = lev5
                    elif response.text == "6":
                        levelprogres = lev6
                    elif response.text == "7":
                        levelprogres = lev7
                    elif response.text == "8":
                        levelprogres = lev8
                    elif response.text == "9":
                        levelprogres = lev9
                    else:
                        levelprogres = lev10

                    print ("-------------------------------\nPROFILE\n-------------------------------\n""name: " + name, "password " + password, "level " + level + " progres to goal(level 10)" + levelprogres + "\n")
                
                elif WhatToDo == ("join class"):
                    newclass = input ("what is your class code ")
                    data_C = {
                        "name": name,
                        "password": password,
                        "class": newclass
                    }
                    response = requests.post("http://localhost:5000/send_data_new_class", json=data_C)

                elif WhatToDo == ("make quiz"):
                    output = ("\n")

                    while True:
                        questionamount = input("how many questions do you want (limit of 5 and hole numbers)? ")
                        questionamount = int(questionamount)
                        if questionamount >= 1 and questionamount <= 5 and isinstance(questionamount, int):
                            break
                        else:
                            print("between 1 and 5")

                
                    for i in range(questionamount):
                        question = input("what is the question?...")
                        answer = input("what is the answer to this question?...")
                        outputadd = ('score = 0\nquestion_1 = "' + question + '"\nanswer_1 = "' + answer + '"\nprint(question_1)\nuser_answer_1 = input("Your answer: ")\nif user_answer_1 == answer_1:\n    print("Correct!")\nelse:\n    score += 1\n    print("Incorrect. The correct answer is", answer_1)\ndata_S = {\n            "name": name,\n            "password": password,\n            "score": str(score)\n        }\nprint (data_S)\nresponse = requests.post("http://localhost:5000/send_data_score", json=data_S)\nprint ("score " + str(score))')
                        output = (str(output) + "\n" + str(outputadd))

                    wantstoseethecode = input("do you want to see the code?Y/N...")
                    if wantstoseethecode == ("Y"):
                        print("start of code\n-------------------------------\n" + output + ("\n\n-------------------------------\nend of code\n"))
                    
                    runcode = input ("would you like to run this code(the code will be run inside with ast or Abstract Syntax Trees witch provides a way to parse and analyze Python code in a more controlled and secure manner)?Y/N...")

                    if runcode == ("Y"):
                        code = output
                        parsed = ast.parse(code)
                        exec(compile(parsed, "<string>", "exec"))
                    
                    wanttoupload = input("do you want to uplaod you quiz?Y/N...")

                    if wanttoupload == ("Y"):
                        whatisthename = input("what do you want the name of the quiz to be?...")
                        data_Q = {
                            "name":"#" + whatisthename + "^",
                            "code": output
                        }            
                        response = requests.post("http://localhost:5000/send_data_new_quiz", json=data_Q)

                elif WhatToDo == ("download/play quiz"):
                    response = requests.get("http://localhost:5000/send_data_ask_quiz")
                    contents = response.text
                    print('\nplease one of the names below (includ the # but not the " and other stuff\n-------------------------------\n' + contents + '-------------------------------')
                    whatquiz = input()
                    data_WQ = {
                        "quiz":whatquiz
                    } 
                    response = requests.post("http://localhost:5000/send_data_quiz", json=data_WQ)
                    contents_quiz = response.text
                    loadedquiz = contents_quiz
                    print(loadedquiz)
                    runcode = input ("would you like to run this quiz in AST?Y/N...")
                    if runcode == ("Y"):
                        code = loadedquiz
                        parsed = ast.parse(code)
                        exec(compile(parsed, "<string>", "exec"))

                elif WhatToDo == ("view class members"):
                    data_VC = {
                        "name": name,
                        "password": password
                    }
                    response = requests.post("http://localhost:5000/send_data_view_class", json=data_VC)
                    poepleinclass = response.text
                    print ("\n-------------------------------\n" + "class\n-------------------------------\n" + poepleinclass)

                elif WhatToDo == ("quit"):
                    sys.exit()
                
                elif WhatToDo == ("chat"):
                    data_CH = {
                        "name": name,
                        "password": password
                    }
                    response = requests.post("http://localhost:5000/class_chat_open", json=data_CH)
                    printstat = response.text
                    if printstat == "servers full pleses wait":
                        print (printstat)
                        time.sleep(4)
                    else:
                        print ("you are in class", printstat)
                        URL = "http://localhost:5000/" + printstat
                        print (URL)
                        URL2 = URL + "r"
                        retur = "joined"
                        data_CHN = {
                            "user": name,
                            "mess": retur
                        }
                        txt = ""
                        while True:
                            print("\n-------------------------------" + txt + "\nto exit type 1 2 to refresh" + "\n-------------------------------")
                            retur = input("")
                            if retur == "1":
                                data_CHD = {
                                    "name": name,
                                    "password": password
                                }
                                response = requests.post("http://localhost:5000/class_chat_close", json=data_CHD)
                                break
                            elif retur == "2":
                                response = requests.get(URL2)
                                txt = response.text
                            else:
                                data_CHN = {
                                    "user": name,
                                    "mess": retur
                                }
                                response = requests.post(URL, json=data_CHN)
                                txt = response.text
                            
        else:
            sys.exit()


thread_1 = threading.Thread(target=function_1)
thread_2 = threading.Thread(target=function_2)

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()

print("Both functions finished executing")