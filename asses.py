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

#sets the infomation lists
nations = ['Yankuntjatjara', 'Anguragu', 'Wik', 'Badulgal', 'Ngaanyatjarra', 'Ngemba', 'Ayapathu', 'Bardi', 'Meriam Mer', 'Kaurareg', 'Gamilaraay', "Kuuku Ya'u", 'Yolŋu people']    

state = ['South Australia', 'Northern Territory', 'Queensland', 'Queensland', 'Northern Territory', 'New South Wales', 'Queensland', 'Western Australia', 'Northern Territory', 'Queensland', 'New South Wales', 'Queensland', 'Northern Territory']

Fact = ['population of 455', '80 per cent of there annual rainfall occurs in the wet season', 'Population of 1,269', 'they live on the Torres Strait islands', 'population 153', 'The majority of the town that the Ngemba are located at are aboriginal', '', 'There region has been involved in mining by rio tinto', 'They are near the Great Barrier Reef', 'population 374', 'located in Lightning Ridge', 'Located 800 kilometres north of cairns', '']

language = ['Yankunytjatjara', 'Anindilyakwa', 'Wilk mungkan', 'Kala Lagaw Ya', 'Ngaanyatjarra', 'Ngemba', 'Ayapathu', 'Bardi', 'Meriam Mer', 'Kala lagaw Ya', 'Gamilaraay', "Kuuky Ya'u", 'Yolngu Matha']  

while True:#a loop that will keep runing intill i break it
    main()#prints the main menu
    slect = int(input("enter 1-6\n"))#gets a input from the user  
   
    if slect == 1:#an if statment that if one is selected it will do what is indented below it 
        page = 1#sets the variables needed
        pos = 0
        nextpage = ""
        pages = len(nations)#get the lingth of the list 
        pages5 = pages/5#devides it by 5 to get the amount of pages
        trupages = math.ceil(pages5)#rounds up


        print("page 1")
        while nextpage != "0":#lets you be able to quit the page
            try:
                while pos < page*5:#the pos is what position of the list it being printed if this is less pages times 5 then it will get that position in the list                    
                    nat = (nations[pos])
                    sta = (state[pos])
                    lan = (language[pos])
                    fac = (Fact[pos])

                    print("----------\n" + nat + "\n" + sta + "\n" + lan + "\n" + fac + "\n----------\n")#prints all of the variables
                    pos += 1# adds one to the pos
            except IndexError:
                print("end of list")#when it gets to the end of the list an the index error gets rased it stops

            print("to quit press 0")
            nextpage = input("< " + str(page) + " >")#gets a input for < 1 > 
            if nextpage == ">" and page < trupages:#if next page = > and and page is smaller the truepages then 1 is added to page and page with the next page number is printed
                page += 1
                print ("Page " + str(page))
            elif nextpage == "<" and page > 1:#if the first option and nextpage = < and page is not one 
                page -= 1# it mines 1 from page and 10 from pos and prints 
                pos -= 10
                print ("Page " + str(page))#prints the next page heada 
            else:
                    print ("can not do this")#if every thing it false this prints
            print("\n")#prints a few new line

    elif slect == 2:# if option 2 is selected
        n = ""#sets variables
        f2 = ""
        n = input("what is the name of the nation:\n")#gets a input for the nation
        nations.append(n)# adds it to nations list
        n = input("what is the state:\n")#gets a input for the state 
        state.append(n)#adds the state list
        n = input("what is there langage:\n")#gets a input for the langage
        language.append(n)#adds the unput to the list
        n = input("a fact:\n")#gets a input for a fact
        while True:#a loop
            more = input("any other facts? Y/N")#sees if the person wants to add another fact
            if more.upper() == "Y":#if yes then it gets a nother input and adds it to the first one
                f2 = input("a fact\n")
                n = n, f2
            elif more.upper() == "N":#if not it breaks the loop
                break
            else:#it will ask again if none are true
                print("please enter Y/N")
        Fact.append(n)#adds the fact or facts to the list

    elif slect == 3:
    	
        stat1 = input("what state do you want to serch? New South Wales, Queensland, South Australia, Tasmania, Victoria, and Western Australia\n")#gets a input for what state to search for
        print("---", stat1, "---\n")#prints --- Queensland --- for example
        positions = []# sets position variable
        for i in range(len(state)):#for each item in range of length of state
            if state[i] == stat1:#if state item = the input then we get the position
                positions.append(i)

        if positions:#if one is found then 
                for pos in positions:#for every item in positions we get there poitions then we print that  same position in nations
                    print(nations[pos] + "\n")
        else:#if no items in the list nations match stat1 then this prints
            print("no nations in " + stat1 + " listed")
        time.sleep(1)#waits 1 second

    elif slect == 4:
        page = 1#sets variables
        pos = 0
        printstr = ""
        nextpage = ""
        pages = len(nations)#gets the linght of nations
        pages5 = pages/5#divides pages by 5
        trupages = math.ceil(pages5)#rounds up
        
        print("page 1")#print the header for page 1
        while nextpage != "0":#while pages don't equal 0
            try:#trys this
                while pos < page*5:#while pos is smaller then pages times 5
                    nat = (nations[pos])#sets the variables with the item in the lists that coresponds to the pos
                    fac = (Fact[pos])

                    print("\n" + nat + "\n" + fac + "\n")#prints it
                    pos += 1#adds 1 to the pos
            except IndexError:#when the error ecurs then we know it is the end of the list
                print("end of list")

            print("to quit press 0")
            nextpage = input("< " + str(page) + " >")#prints < page > and gets a input
            if nextpage == ">" and page < trupages:#if nextpage = > and page is smaller then turnpages then  1 is added to page
                page += 1
                print ("Page " + str(page))#it prints the page number
            elif nextpage == "<" and page > 1:#if next page = < and page is bigger then 1
                page -= 1#we -1 from page
                pos -= 10#we -10 form pos
                print ("Page " + str(page))#it prints the page number
            else:
                print ("can not do this")#if non applie then this is printed
            print("\n")#add 2 new lines
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