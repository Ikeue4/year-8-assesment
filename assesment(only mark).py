'''
== DOCUMENTAION == 

    == OVER VIEW ==
    The code is an interactive program that allows users to interact with a database of information about various First Nations (Indigenous Peoples of Australia). 
    It presents the user with a menu of options, which include viewing a list of nations, adding a new nation, ordering the nations by their current state, viewing 
    interesting facts about the nations, searching Wikipedia for a nation, and quitting the program.The program initializes several lists of information about each 
    nation, including their name, state, language, and a fact about

    == HOW TO FIX == 
    1. Import Error: this could be because of a library is not installed 
        1.1. Fix pip install package_name
        1.2. Or install package_name --upgrade 

    2. there should not be any

'''
#imports all library's
import time #time so that we can wait
import sys #sys for exiting the program
import math #math for the page math mainly rounding up
import difflib #for the spell check
try: #wikipedia is not a native library's so this lets us see if it is installed with out r
    import wikipedia #so we can access the wikipedia API and search
except:
    print("wikipedia could not be imported (not available on ipad if not on ipad pip install the library)")

print("first nations\n")#prints a heder


def main():#sets the definition of the menu
    print("- menu -")
    print("1. add nation")
    print("2. view all information")
    print("3. sort nations")
    print("4. view interesting facts")
    print("5. search wikipedia for nation")
    print("6. quit")


def match_input(possible_inputs):#sets the definition for the spell check takes a input in for a list of possible inputs
    user_input = input("Enter your input: ")#gets a input form the user
    while user_input not in possible_inputs:#while the input form the user is not in the list of possible inputs
        closest_match = difflib.get_close_matches(user_input, possible_inputs, n=1)#gives the difflib libary the user_input and possiblie_inputs and tells it to give the best input with n=1
        if closest_match:#if a match is found
            suggestion = closest_match[0]#it make the suggestion the first first position in closest_match
            confirm_suggestion = input(f"Did you mean '{suggestion}' instead? Y/N ")#'asks' the user if there input was meant to be the suggestion 
            if confirm_suggestion.lower() == "y":#if yes the it will return the suggestion
                return suggestion
        else:#if there is no closes match it will return the raw user input
            return user_input
    return user_input#if the input is in possible inputs then it will return the raw user input

class Nation:#sets the class of nations
    def __init__(self, nations, state, facts, languages):#defines all of the inputs needed
        self.n = ""#sets all of the inputs needed for the class
        self.facts = ""
        self.nationsli = nations#passes though the lists
        self.stateli = state
        self.factli = facts
        self.languageli = languages

    def get_input(self):#define's get_input in the class
        self.n = input("What is the name of the nation: ")#gets a input for the name
        self.nationsli.append(self.n)#appends nations list with the user input
        self.n = input("What is the state: ")#gets a input for the state
        self.stateli.append(self.n)#appends state list with the user input
        self.n = input("What is their language: ")#gets a input for the language
        self.languageli.append(self.n)#appends language list with the user input
        self.facts = input("A fact: ")#gets a input for the fact

        while True:#starts a loop
            more = input("Any other facts? (Y/N): ")#asks the user if they want to add any other facts
            if more.upper() == "N":#if they don't want to add another fact(upper is used to take a upper case or lower)
                self.factli.append(self.facts)#appends fact list with the user input
                break#break out of the loop
            elif more.upper() == "Y":#if they want to add another fact(upper is used to take a upper case or lower),m
                facts2 = input("A fact: ")#gets a input for the fact
                self.facts = self.facts + " " + facts2#combines the fact list with the user input
            else:#else if the does not put a valid input then Y/N is asked again
                print("Please enter Y/N.")



class Sort:#sets the class of sorting 
    def __init__(self, nations, state, possible_inputs):#defines the inputs form the rest of the code needed
        self.nationsli = nations#sets the variables with the ones passed thought
        self.stateli = state
        self.possible = possible_inputs
        self.result = ""#also sets other variables needed


    def search_state1(self):#defines search state 1
        stateprint = ""#clears state print
        for i in self.possible:#for the items in possible inputs
                stateprint = stateprint + i + ", "#add the item to state print
        print(f"what state do you want to search? {stateprint} \n")#prints what state do you want to search + the possible inputs
        stat1 = match_input(self.possible)#state to search for = output form the spell check function(we also pass though the possible inputs)
        print("---", stat1, "---\n")#prints the state that we searched for
        positions = []#clears the positions list
        for i in range(len(self.stateli)):#Loop through the state list and find all indices where the value is equal to stat1.
            if self.stateli[i] == stat1:#If the state of the object at index i is equal to stat1, append the index i to the positions list.
                positions.append(i)

        if positions:#If there are positions, 
            for pos in positions:#iterate through them
                self.result = (self.nationsli[pos] + "\n")#and set the result to the concatenation of the nation at that position and a newline character.
                self.print_result()#Then, print the result.
        else:#if not positions found
            self.result = ("no nations in " + stat1 + " listed")#set the result to no nations in the state listed
            self.print_result()#Then, print the result with the function


    def search_state2(self):#define the search function 2
        
        sorted_nations = sorted(self.nationsli) # sort the list alphabetically

        prev_letter = None#set the previous letter to none
        for item in sorted_nations:#For each item in a list of sorted nations, 
            first_letter = item[0].upper()#get the first letter of the item and convert it to uppercase.

            # increment the letter only if it's different from the previous one
            if first_letter != prev_letter:#if the first letter is different from the previous one
                letter = first_letter#the letter = the first letter variable
                self.result = (f"{letter}: {item}\n")#then it sets the result to the letter and the nation 
                self.print_result()#Then, print the result
            else:# if the first letter is equal to the previous one
                self.result = (f"  : {item}\n") # prints a blank space for subsequent items with the same first letter
                self.print_result()#then, print the result with the function

            prev_letter = first_letter #set the previous letter to the first letter
    

    def search_state3(self):# define the search function 3
        id = 0# sets the id to 0
        for item in self.nationsli:#Iterate through a list of nations and print each item with an ID number.
            self.result = (f"{str(id)}: {item}")#sets the result to the id and the name of the nation
            self.print_result()#then, print the result with the function
            id += 1#add 1 to the id
    

    def search_state4(self):# define the search function 4
        idf = int(input("id: "))#gets a input form the user for a id
        try:#trys to find the id
            self.result = (self.nationsli[idf])#sets the result to the id
            self.print_result()#then, print the result
        except:#if the id is not found
            self.result = ("a error has occurred")#sets the result to an error has occured
            self.print_result()#then, print the result


    def print_result(self):#define the print function
        try:#trys to print the result
            print(self.result)
        except:#if there is an error
            print("there was an error with the result")# sates that an error has occured



class printpage:#defines the class print page
    def __init__(self, nations, state, fact, language, typegen):#defines the inputs for the rest of the class
        self.result = ""#deffines the variables needed by multiple functions
        self.nationsli = nations
        self.stateli = state
        self.factli = fact
        self.languageli = language
        self.type = typegen
        self.page = 0
        self.nextpage = ""
        self.pos = 0
        self.trupages = 0


    def makepage(self):# defines the make page function
        self.page = 1#sets the variables needed
        self.pos = 0
        self.nextpage = ""
        pages = len(self.nationsli)#get the lingth of the list 
        pages5 = pages/5#devides it by 5 to get the amount of pages
        self.trupages = math.ceil(pages5)#rounds up

        print("page 1")
        while self.nextpage != "0":#lets you be able to quit the page
            try:
                while self.pos < self.page*5:#the pos is what position of the list it being printed if this is less pages times 5 then it will get that position in the list                    
                    nat = (self.nationsli[self.pos])
                    sta = (self.stateli[self.pos])
                    lan = (self.languageli[self.pos])
                    fac = (self.factli[self.pos])

                    if self.type == 1:#if print type 1 has been selected 
                        self.result = ("----------\n" + nat + "\n" + sta + "\n" + lan + "\n" + str(fac) + "\n----------\n")#sets the result
                        self.print_result()#then prints the result
                    elif self.type == 2:#if print type 2 has been selected
                        self.result = ("----------\n" + nat + "\n" + str(fac) + "\n----------\n")#sets the result
                        self.print_result()#then prints the result
                    else:#else
                        self.result = ("print format error")#sets the result to print format error
                        self.print_result()#then prints the result
                    self.pos += 1# adds one to the pos
            except IndexError:#if the exception index is out of range comes up then
                self.result = ("end of list")#we set the result to end of list
                self.print_result()#then prints the result
            if self.pagedeal() == 0:#if pagedeal = 0 we return to the main page
                return
            else:#prints a empty line
                print()


    def pagedeal(self):
        print("to quit press 0")
        nextpage = input("< " + str(self.page) + " >")#gets a input for < 1 > 
        if nextpage == ">" and self.page < self.trupages:#if next page = > and and page is smaller the truepages then 1 is added to page and page with the next page number is printed
            self.page += 1
            self.result =("Page " + str(self.page))
        elif nextpage == "<" and self.page > 1:#if the first option and nextpage = < and page is not one 
            self.page -= 1# it mines 1 from page and 10 from pos and prints 
            self.pos -= 10
            self.result =("Page " + str(self.page))#prints the next page heada 
        elif nextpage == "0":
            return 0# returns a 0 to makepage
        else:
            self.result =("can not do this")#if every thing it false this prints
        self.print_result()
        print("\n")#prints a few new line


    def print_result(self):#define the print function
        try:#trys to print the result
            print(self.result)
        except:#if there is an error
            print("there was an error with the result")# sates that an error has occured


    
possible_inputs = []#clears the list of possible inputs

#sets the infomation lists
nations = ['Yankuntjatjara', 'Anguragu', 'Wik', 'Badulgal', 'Ngaanyatjarra', 'Ngemba', 'Ayapathu', 'Bardi', 'Meriam Mer', 'Kaurareg', 'Gamilaraay', "Kuuku Ya'u", 'Yolŋu people', 'Anathangayth ', 'Barkindji ', 'Martu people ', 'Bagala people ', 'Mantiyupwi Clan ', 'Gunggandji people', 'Gunggandji people']    

state = ['South Australia', 'Northern Territory', 'Queensland', 'Queensland', 'Northern Territory', 'New South Wales', 'Queensland', 'Western Australia', 'Northern Territory', 'Queensland', 'New South Wales', 'Queensland', 'Northern Territory', 'Queensland', 'New South Wales', 'Western Australia', 'Northern Territory', 'Northern Territory', 'Queensland', 'Northern Territory']

fact = ['population of 455', '80 per cent of there annual rainfall occurs in the wet season', 'Population of 1,269', 'they live on the Torres Strait islands', 'population 153', 'The majority of the town that the Ngemba are located at are aboriginal', 'Coen (the community where the treble is located) is a small community situated in central Cape York in Far North Queensland, 580 kilometres north of Cairns. ', 'There region has been involved in mining by rio tinto', 'They are near the Great Barrier Reef', 'population 374', 'located in Lightning Ridge', 'Located 800 kilometres north of cairns', 'Located 800 kilometres north of cairns', 'Population of 3899 in the area they are in', 'Population of 452 in the area they are in', 'Population of 300 in the area they are in', 'Population of 531 in the area they are in, 95.7% Indigenous', 'Population of 1,563 in the area they are in', 'Yarrabah (the community where the treble is located) is an Aboriginal community located 55 kilometres east of Cairns in Far North Queensland', 'Yirrkala (the community where the treble is located) is a coastal community in the East Arnhem region of the Northern Territory and is about 18kms south-east of Nhulunbuy.']

language = ['Yankunytjatjara', 'Anindilyakwa', 'Wilk mungkan', 'Kala Lagaw Ya', 'Ngaanyatjarra', 'Ngemba', 'Ayapathu', 'Bardi', 'Meriam Mer', 'Kala lagaw Ya', 'Gamilaraay', "Kuuky Ya'u", 'Yolngu Matha', 'Anathangayth ', 'Barkindji ', 'Martuwangka ', 'Rembarranga ', 'Modern Tiwi ', 'Gunggandj ', 'Yolngu Matha ']  


while True:#a loop that will keep runing intill i break it
    while True:
        main()#prints the main menu
        try:
            slect = int(input("enter 1-6\n"))#gets a input from the user 
            break 
        except:#if a error occurs with the input then
            print("was not a valid input")#not valid will be returned
            time.sleep(2)#waits 2 seconds
   
    if slect == 1:#an if statment that if one is selected it will do what is indented below it
        
        my_nation = Nation(nations, state, fact, language)# sets my nation to Nation and passes though the variables nations, state, fact, and language
        my_nation.get_input()#calls the get_input function
        

    elif slect == 2:# if option 2 is selected
        
        typegen = 1#sets the type of page generation to be 1
        my_page = printpage(nations, state, fact, language, typegen)# sets my page to printpage and passes the variables nations, state, fact, language, typegen
        my_page.makepage()#calls the make page function

    elif slect == 3:# if option 3 is selected

    	while True:# a while loop that will keep running intill i break it
            try:#trys to get a interger input from the user
                searchm = input(int("search method, 1 search by present nation, 2 A-Z, 3 show ids, 4 search by id: "))
            except:#if an error occurs with the input then
                print("invalid input")# prints input invalid

            if searchm == 1:#if search method 1 is selected
                possible_inputs = []#possible input are cleared
                for i in state:# iterates over state
                    if i not in possible_inputs:#if i is not in possible_inputs
                        possible_inputs.append(i)#we add it to possible_inputs
                my_sort = Sort(nations, state, possible_inputs)# then nations, state, possible_inputs are loaded to my_sort
                my_sort.search_state1()#search state 1 is called with the variables passed in
                time.sleep(1)# waits 1 second
                break# breaks the loop
            elif searchm == 2:#if search method 2 is selected
                my_sort = Sort(nations, state, possible_inputs)# then nations, state, possible_inputs are loaded to my_sort
                my_sort.search_state2()# search state 2 is called with the variables passed in
                time.sleep(1)# waits 1 second
                break# breaks the loop
            elif searchm == 3:# if search method 3 is selected
                my_sort = Sort(nations, state, possible_inputs)# then nations, state, possible_inputs are loaded to my_sort
                my_sort.search_state3()# search state 3 is called with the variables passed in
                time.sleep(1)# waits 1 second
                break# breaks the loop
            elif searchm == 4:# if search method 4 is selected
                my_sort = Sort(nations, state, possible_inputs)# then nations, state, possible_inputs are loaded to my_sort
                my_sort.search_state4()# search state 4 is called with the variables
                time.sleep(1)# waits 1 second
                break# breaks the loop
            else:#else 
                print('enter vaild response')# invalid response is printed

    elif slect == 4:# if 4 is selected
        
        typegen = 2# type generation is set to be 2
        my_page = printpage(nations, state, fact, language, typegen)# sets my page to printpage and passes the variables nations, state, fact, language, typegen
        my_page.makepage()# calls the make page function

    elif slect == 5:#if 5 is selected
        try:#lets us use wikipeadia to search for other tribes but the libary can't be downloaded on all divices
            search = input("what do you want me to serch for? \n")#gets a input for what to search for
            search_results = wikipedia.search(search)#does a basic seach using the wikipeadia api will give you a list of pages
        
            for result in search_results:#prints all of the results
                print(result)
        
            article = wikipedia.page("page\n")#will then request from the api the page that you want and will then print the page
            print(article.content)
        except: 
            print("unavalibe on a ipad or libary not installed")#can not be used with pythonista
    elif slect == 6:#if 6 is slected
        print("quit has been selected")
        sys.exit()#uses system to exit will work on any divice
    else:
        print("enter 1-6")#if 1 to 6 was inputed then it will print this and print the menu again