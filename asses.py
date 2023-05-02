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
import time #imports all libarys
import sys
import math
import difflib
try:
    import wikipedia
except:
    print("wikipedai could not be imported (not avalable on ipad if not on ipad pip install the libary)")

print("first nations\n")

def main():#sets the defonition of the menu
    print("- menu -")
    print("1. view lis of nations")
    print("2. add nation")
    print("3. order nations via current day state")
    print("4. view interesting facts")
    print("5. serch wikipedia for nation")
    print("6. quit")

def match_input(possible_inputs):
    user_input = input("Enter your input: ")
    while user_input not in possible_inputs:
        closest_match = difflib.get_close_matches(user_input, possible_inputs, n=1)
        if closest_match:
            suggestion = closest_match[0]
            confirm_suggestion = input(f"Did you mean '{suggestion}' instead? [y/n] ")
            if confirm_suggestion.lower() == "y":
                return suggestion
    return user_input


class Nation:
    def __init__(self, nations, state, facts, languages):
        self.n = ""
        self.facts = ""
        self.nationsli = nations
        self.stateli = state
        self.factli = facts
        self.languageli = languages

    def get_input(self):
        self.n = input("What is the name of the nation: ")
        self.nationsli.append(self.n)
        self.n = input("What is the state: ")
        self.stateli.append(self.n)
        self.n = input("What is their language: ")
        self.languageli.append(self.n)
        self.facts = input("A fact: ")

        while True:
            more = input("Any other facts? (Y/N): ")
            if more.upper() == "N":
                self.factli.append(self.facts)
                break
            elif more.upper() == "Y":
                facts2 = input("A fact: ")
                self.facts = self.facts + " " + facts2
            else:
                print("Please enter Y/N.")

class Sort:
    def __init__(self, nations, state, possible_inputs):
        self.nationsli = nations
        self.stateli = state
        self.possible = possible_inputs
        self.result = ""

    def search_state1(self):
        print("what state do you want to search? New South Wales, Queensland, South Australia, Tasmania, Victoria, and Western Australia \n")
        stat1 = match_input(self.possible)
        print("---", stat1, "---\n")
        positions = []
        for i in range(len(self.stateli)):
            if self.stateli[i] == stat1:
                positions.append(i)

        if positions:
            for pos in positions:
                self.result = (self.nationsli[pos] + "\n")
                self.print_result()
        else:
            self.result = ("no nations in " + stat1 + " listed")
            self.print_result()

    def search_state2(self):
        
        sorted_nations = sorted(self.nationsli) # sort the list alphabetically

        prev_letter = None
        for item in sorted_nations:
            first_letter = item[0].upper()

            # increment the letter only if it's different from the previous one
            if first_letter != prev_letter:
                letter = first_letter
                self.result = (f"{letter}: {item}\n")
                self.print_result()
            else:
                self.result = (f"  : {item}\n") # print a blank space for subsequent items with the same first letter
                self.print_result()

            prev_letter = first_letter
    
    def search_state3(self):
        id = 0
        for item in self.nationsli:
            self.result = (f"{str(id)}: {item}")
            self.print_result()
            id += 1
    
    def search_state4(self):
        idf = int(input("id: "))
        self.result = (self.nationsli[idf])
        self.print_result()

    def print_result(self):
        try:
            print(self.result)
        except:
            print("there was an error with the result")

class printpage:
    def __init__(self, nations, state, fact, language, typegen):
        self.result = ""
        self.nationsli = nations
        self.stateli = state
        self.factli = fact
        self.languageli = language
        self.type = typegen
        self.page = 0
        self.nextpage = ""
        self.pos = 0
        self.trupages = 0

    def makepage(self):
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

                    if self.type == 1:
                        self.result = ("----------\n" + nat + "\n" + sta + "\n" + lan + "\n" + str(fac) + "\n----------\n")#prints all of the variables
                        self.print_result()
                    elif self.type == 2:
                        self.result = ("----------\n" + nat + "\n" + str(fac) + "\n----------\n")#prints all of the variables
                        self.print_result()
                    else:
                        self.result = ("print format error")
                        self.print_result()
                    self.pos += 1# adds one to the pos
            except IndexError:
                self.result = ("end of list")#when it gets to the end of the list an the index error gets rased it stops
                self.print_result()
            if self.pagedeal() == 0:
                return
            else:
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
            return 0
        else:
            self.result =("can not do this")#if every thing it false this prints
        self.print_result()
        print("\n")#prints a few new line

    def print_result(self):
        try:
            print(self.result)
        except:
            print("there was an error with the result")


    
possible_inputs = []

#sets the infomation lists
nations = ['Yankuntjatjara', 'Anguragu', 'Wik', 'Badulgal', 'Ngaanyatjarra', 'Ngemba', 'Ayapathu', 'Bardi', 'Meriam Mer', 'Kaurareg', 'Gamilaraay', "Kuuku Ya'u", 'Yolŋu people']    

state = ['South Australia', 'Northern Territory', 'Queensland', 'Queensland', 'Northern Territory', 'New South Wales', 'Queensland', 'Western Australia', 'Northern Territory', 'Queensland', 'New South Wales', 'Queensland', 'Northern Territory']

fact = ['population of 455', '80 per cent of there annual rainfall occurs in the wet season', 'Population of 1,269', 'they live on the Torres Strait islands', 'population 153', 'The majority of the town that the Ngemba are located at are aboriginal', '', 'There region has been involved in mining by rio tinto', 'They are near the Great Barrier Reef', 'population 374', 'located in Lightning Ridge', 'Located 800 kilometres north of cairns', '']

language = ['Yankunytjatjara', 'Anindilyakwa', 'Wilk mungkan', 'Kala Lagaw Ya', 'Ngaanyatjarra', 'Ngemba', 'Ayapathu', 'Bardi', 'Meriam Mer', 'Kala lagaw Ya', 'Gamilaraay', "Kuuky Ya'u", 'Yolngu Matha']  

while True:#a loop that will keep runing intill i break it
    main()#prints the main menu
    slect = int(input("enter 1-6\n"))#gets a input from the user  
   
    if slect == 1:#an if statment that if one is selected it will do what is indented below it
        
        typegen = 1
        my_page = printpage(nations, state, fact, language, typegen)
        my_page.makepage()
        

    elif slect == 2:# if option 2 is selected
        
        
        my_nation = Nation(nations, state, fact, language)
        my_nation.get_input()

    elif slect == 3:
    	
        searchm = input("search method: ")

        if searchm == "1":
            possible_inputs = ['New South Wales', 'Queensland', 'South Australia', 'Tasmania',' Victoria', 'Western Australia']
            my_sort = Sort(nations, state, possible_inputs)
            my_sort.search_state1()
            time.sleep(1)
        elif searchm == "2":
            my_sort = Sort(nations, state, possible_inputs)
            my_sort.search_state2()
            time.sleep(1)
        elif searchm == "3":
            my_sort = Sort(nations, state, possible_inputs)
            my_sort.search_state3()
            time.sleep(1)
        elif searchm == "4":
            my_sort = Sort(nations, state, possible_inputs)
            my_sort.search_state4()
            time.sleep(1)
        else:
            print('enter vaild response')

    elif slect == 4:
        
        typegen = 2
        my_page = printpage(nations, state, fact, language, typegen)
        my_page.makepage()

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