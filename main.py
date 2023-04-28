'''
== DOCUMENTATION == 

    == OVER VIEW ==
    The main page is code that interacts with a server and was inspired by education perfect. You have features like classes that allow you to see their score and chat with them. 
    You can also make quizzes that you can upload to a server for others to play. When you get a question right you can level up, you also have a login system so all your data is saved. 

    == HOW TO FIX ==
    1. Import Error: this could be because of a library is not installed
        1.1. Fix pip install package_name
        1.2. Or install package_name --upgrade 

    2. requests.exceptions.ConnectionError: happens because code could not connect to the server 
        2.2. Fix check that the server is running on a local host port should be on http://localhost:5000 

    3. password or name is incorrect please try again or make an account: 
        3.1. Fix create new w account and delete other accounts 
        3.2. check that you password is in the password.txt file and check 	that it does not have any ^: or # in it could create some errors 

    4.You might get error when downloading a quiz just check that the name matches you don’t have to include the #	 
  
'''

try:#imports the libarys if the libary is not installed there will be a ImportError and it will print that that libary is not installed
    import requests
    print ("\033[32mrequests installed ✔\033[0m")
except ImportError:
    print("\033[31mThe requests library is not installed ✘\033[0m")

try:
    import ast
    print ("\033[32mast installed ✔\033[0m")
except ImportError:
    print("\033[31mThe ast library is not installed ✘\033[0m")

try:
    import sys
    print ("\033[32msys installed ✔\033[0m")
except ImportError:
    print("\033[31mThe sys library is not installed ✘\033[0m")

try:
    import time
    print ("\033[32mtime installed ✔\033[0m")
except ImportError:
    print("\033[31mThe time library is not installed ✘\033[0m")

import wikipedia

try:#trys to connect to the server on local host
    response = requests.get("http://localhost:5000/ping")
    server = response.text
    print("\033[32m" + server, "\033[32m✔\033[0m")
except:
    print("\033[31mcannot connect to server ✘\033[0m")


print("^_^")

while True:#a while true loop that the account login is inbeted in
    hasacc = input("Do you have an account Y/N? ")#asks if the user have a account 
    if hasacc.upper() == "Y":#if the user hase a account then this code will run
        time.sleep (1)#waits for one minute
        name = input("What is your name? ")#asks for there name
        password = input("What is your password? ")#asks for there password
        data_P = {#loads the infomation in to a variable
            "name": name,
            "password": password
        }
        response = requests.post("http://localhost:5000/send_data_log", json=data_P)#send that variable to the server with a post request
        if response.status_code == 200:# if a code 200(all good) has been returned from the server then  it will print that the password is valid
            print("Password validation status received")
            # You can extract the password validation status from the response text
            password_validation_status = response.text
            print (password_validation_status)
            break#breaks so you can move on to the next stage
        else:#if password is not vaild or a conection could not be astablished then this will print
            print ("password or name is incorrect please try again or make a account")
        time.sleep (1)#stops for 1 second
    elif hasacc.upper() == "N":# if the user does not have a account then this will play
        while True:# a while True loop that deals with any not vaild answers
            WAP = input("Do you want to make an account? Y/N? ")#asks if a account wants to be made
            if WAP.upper() == "Y":#if they do want to make a account
                name_new = input("What is your name? ")#asks for there name
                password_new = input("What would your password be? ")#asks for a password
                data_P_New = {#loads it in to a variable
                    "name": name_new,
                    "password": password_new
                }
                response = requests.post("http://localhost:5000/send_data_log_new", json=data_P_New)#send it to the server
                password_validation_status = "succses"#sets the validation status to true can be a issue as you can spoof this 
                break#breaks so that the user can continue
            elif WAP.upper() == "N":#if the user does not want to make a account then it will let them go on but most feachers wont work
                print("most functions will break work")
                break
            else:
                print("enter Y/N")#if y or n is not entered
            
    else:
        print("Enter Y/N")#if y or n is not entered

if password_validation_status == ("succses"):#checks if the password is vaild 
    lev0 = ("[░░░░░░░░░░]")# settis the progress bare vals
    lev1 = ("[█░░░░░░░░░]")
    lev2 = ("[██░░░░░░░░]")
    lev3 = ("[███░░░░░░░]")
    lev4 = ("[████░░░░░░]")
    lev5 = ("[█████░░░░░]")
    lev6 = ("[██████░░░░]")
    lev7 = ("[███████░░░]")
    lev8 = ("[████████░░]")
    lev9 = ("[█████████░]")
    lev10 = ("[█████████]")


    while True:# a while true loop to alow the code to go back to the main menue
        WhatToDo = input("-------------------------------\nUSER OPTIONS\n-------------------------------\n1:profile\n2:join class\n3:view class members\n4:make quiz\n5:download/play quiz\n6:quit\n7:chat\n")#prints the main menue
        if WhatToDo == ("1"):# if the user select the first option
            data_N = {#sets the data val
                "name": name,
                "password": password
            }
            response = requests.post("http://localhost:5000/send_data_level", json=data_N)#send the name and the password to the server (is used as a id)

            level = response.text#gets the respones from the server and makes it in to a progress bare
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

            print ("-------------------------------\nPROFILE\n-------------------------------\n""name: " + name, "password " + password, "level " + level + " progres to goal(level 10)" + levelprogres + "\n")#prints all of the infomation
        
        elif WhatToDo == ("2"):# if the user selects the second option
            newclass = input ("what is your class code ")#asks for a class code difalt is just a random number
            data_C = {#sets the val with the new class code
                "name": name,
                "password": password,
                "class": newclass
            }
            response = requests.post("http://localhost:5000/send_data_new_class", json=data_C)#sends it to the server

        elif WhatToDo == ("4"):# if the user selects the 4 option
            output = ("\n")#clears the var and gives it a new line

            while True:#a loop that we can break
                questionamount = input("how many questions do you want (limit of 5 and hole numbers)? ")# sees how many questions that need to be generated
                questionamount = int(questionamount)#make it in to a interga
                if questionamount >= 1 and questionamount <= 5 and isinstance(questionamount, int):#if question amount is lager or equle to 1 and smaller then 6 and question amount is a int
                    break# breaks the loop
                else:
                    print("between 1 and 5")# if not satisifed

        
            for i in range(questionamount):#will do it as many times as the amount of questionamount
                question = input("what is the question?...")#asks for what is the question
                answer = input("what is the answer to this question?...")#asks what the ansewer to the question is
                outputadd = ('\nquestion_1 = "' + question + '"\nanswer_1 = "' + answer + '"\nprint(question_1)\nuser_answer_1 = input("Your answer: ")\nif user_answer_1 == answer_1:\n    print("Correct!")\n    score += 1\nelse:\n    print("Incorrect. The correct answer is", answer_1)\nprint ("score " + str(score))')# basic code for a python quiz, adds the variables to the code
                output = (str(output) + "\n" + str(outputadd))#adds the out put the the other outputs

            output = ('score = 0' + output + '\ndata_S = {\n            "name": name,\n            "password": password,\n            "score": str(score)\n        }\nprint (data_S)\nresponse = requests.post("http://localhost:5000/send_data_score", json=data_S)\n')#adds server intergration

            wantstoseethecode = input("do you want to see the code?Y/N...")#asks if the code should be printed
            if wantstoseethecode == ("Y"):#if yes prints the code
                print("start of code\n-------------------------------\n" + output + ("\n\n-------------------------------\nend of code\n"))
            
            runcode = input ("would you like to run this code?Y/N...")#asks if the quiz should be run

            if runcode.upper() == ("Y"):#if yes
                code = output#code is loaded
                parsed = ast.parse(code)#code is ast scanned 
                exec(compile(parsed, "<string>", "exec"))#code is executed and compiled
            
            wanttoupload = input("do you want to uplaod you quiz?Y/N...")#asks if the code should be uploded

            if wanttoupload.upper() == ("Y"):#if yes
                whatisthename = input("what do you want the name of the quiz to be?...")#asks for the name
                data_Q = {#loads the data
                    "name":"#" + whatisthename + "^",
                    "code": output
                }            
                response = requests.post("http://localhost:5000/send_data_new_quiz", json=data_Q)#sends the data to the server

        elif WhatToDo == ("5"):#if 5 is slected
            response = requests.get("http://localhost:5000/send_data_ask_quiz")#ask the server for all of the quizes
            contents = response.json()#the response is resived
            formatted_list = [item[1:] for item in contents]  # remove "#" from each string because of the way the names are stored eg #Assinment^:
            formatted_string = ", ".join(formatted_list)  # join strings with comma separator
            whatquiz = input('\nplease one of the names below\n-------------------------------\n' + formatted_string + '\n-------------------------------\n')#gets a input
            whatquiz = ("#" + whatquiz)#adds th #
            data_WQ = {#loads it in to a var
                "quiz":whatquiz
            } 
            response = requests.post("http://localhost:5000/send_data_quiz", json=data_WQ)#sends the equest to the server
            code = response.text#get the return form the server
            print(code)#prints the quiz
            runcode = input ("would you like to run this quiz?Y/N...")#asks if the quiz should be run
            if runcode.upper() == ("Y"):#if the code should be run
                result = exec(code)#executs the code does not scan it because to be uploaded to the server the code is scaned
                print("The result is:", result)# prints the executed code

        elif WhatToDo == ("3"):#if 3 is slected
            data_VC = {#loads the name and password
                "name": name,
                "password": password
            }
            response = requests.post("http://localhost:5000/send_data_view_class", json=data_VC)# sends the data to the server
            poepleinclass = response.text#gets the response
            print ("\n-------------------------------\n" + "class\n-------------------------------\n" + poepleinclass)#prints the people in the class

        elif WhatToDo == ("6"):#if option 6
            sys.exit()#quits
        
        elif WhatToDo == ("7"):#if 7 selected
            data_CH = {# loads the name and password
                "name": name,
                "password": password
            }
            response = requests.post("http://localhost:5000/class_chat_open", json=data_CH)#sends it to the server
            printstat = response.text#gets the response
            if printstat == "servers full pleses wait":#if the servers are full 
                print (printstat)
                time.sleep(4)#waits so that the user can try again
            else:
                print ("you are in server", printstat)#prints the server they have been assined to
                URL = "http://localhost:5000/" + printstat#sets what the new url will be
                print (URL)#prints it for error checking
                URL2 = URL + "r"#sets the read url
                retur = "joined"#tells the server that you have joined 
                data_CHN = {#gives the server your name and the joined status
                    "user": name,
                    "mess": retur
                }
                txt = ""#clears the text var
                while True:#a loop that we can break
                    print("\n-------------------------------" + txt + "\nto exit type 1 2 to refresh" + "\n-------------------------------")#prints the text varible
                    retur = input()
                    if retur == "1":#if the user wants to exit
                        data_CHD = {#loads the data
                            "name": name,
                            "password": password
                        }
                        response = requests.post("http://localhost:5000/class_chat_close", json=data_CHD)#tells the server that you have left that server and if there is no one left then it can be closed
                        break#breaks the loop
                    elif retur == "2":#if 2 selected 
                        response = requests.get(URL2)#it will request a refresh from the server
                        txt = response.text#gets the response
                    else:
                        data_CHN = {#will load what has been sent in to a var
                            "user": name,
                            "mess": retur
                        }
                        response = requests.post(URL, json=data_CHN)#sends the new mesage
                        txt = response.text#gets the response
                    
else:
    sys.exit()