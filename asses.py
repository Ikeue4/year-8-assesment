import time
import sys
import wikipedia

print("first nations\n")

def main():
    print("- menu -")
    print("1. view lis of nations")
    print("2. add nation")
    print("3. order nations via current day state")
    print("4. view interesting facts")
    print("5. serch wikipedia for nation")
    print("6. quit")


nations = ['Yankuntjatjara', 'Anguragu', 'Wik', 'Badulgal', 'Ngaanyatjarra', 'Ngemba', 'Ayapathu', 'Bardi', 'Meriam Mer', 'Kaurareg', 'Gamilaraay', "Kuuku Ya'u", 'Yolŋu people']    

state = ['South Australia', 'Northern Territory', 'Queensland', 'Queensland', 'Northern Territory', 'New South Wales', 'Queensland', 'Western Australia', 'Northern Territory', 'Queensland', 'New South Wales', 'Queensland', 'Northern Territory']

Fact = ['population of 455', '80 per cent of there annual rainfall occurs in the wet season', 'Population of 1,269', 'they live on the Torres Strait islands', 'population 153', 'The majority of the town that the Ngemba are located at are aboriginal', '', 'There region has been involved in mining by rio tinto', 'They are near the Great Barrier Reef', 'population 374', 'located in Lightning Ridge', 'Located 800 kilometres north of cairns', '']

language = ['Yankunytjatjara', 'Anindilyakwa', 'Wilk mungkan', 'Kala Lagaw Ya', 'Ngaanyatjarra', 'Ngemba', 'Ayapathu', 'Bardi', 'Meriam Mer', 'Kala lagaw Ya', 'Gamilaraay', "Kuuky Ya'u", 'Yolngu Matha']  
                   
while True:
    main()
    slect = input("enter 1-6")
   
    if slect == "1":
        page = 1
        pos = 0
        printstr = ""
        nextpage = ""
        pages = len(nations)
        pages5 = pages/5
        trupages = round(pages5)

        print("you have seletcted option 1\n")
        print("page 1")
        while nextpage != "0":
            try:
                while pos < page*5:
                    nat = (nations[pos])
                    sta = (state[pos])
                    lan = (language[pos])
                    fac = (Fact[pos])

                    printstr = "--------------------\n" + nat + "\n" + sta + "\n" + lan + "\n" + fac + "\n--------------------\n"
                    pos += 1
                    print(printstr)
            except IndexError:
                print("end of list")

            print("to quit press 0")
            nextpage = input("< " + str(page) + " >")
            if nextpage == ">" and page < trupages:
                printstr = ""
                page += 1
                print ("Page " + str(page))
            elif nextpage == "<" and page > 1:
                printstr = ""
                page -= 1
                print ("Page " + str(page))
            else:
                    print ("can not do this")
            print("\n")

    elif slect == "2":
        n = ""
        s = ""
        l = ""
        f = ""
        f2 = ""
        print("you have seletcted option 2")
        n = input("what is the name of the nation")
        s = input("what is the state")
        l = input("what is there langage")
        f = input("a fact")
        while True:
            more = input("any other facts? Y/N")
            if more == "Y":
                f2 = input("a fact")
                f = f + f2
            elif more == "N":
                break
            else:
                print("please enter Y/N")
        nations.append(n)
        state.append(s)
        language.append(l)
        Fact.append(f)

    elif slect == "3":
        print("you have seletcted option 3")

        stat1 = input("what stat do you want to serch? New South Wales, Queensland, South Australia, Tasmania, Victoria, and Western Australia")
        print("---", stat1, "---\n")
        positions = []
        for i in range(len(state)):
            if state[i] == stat1:
                positions.append(i)

        if positions:
                for pos in positions:
                    print(nations[pos] + "\n")
        else:
            print("no nations in " + stat1 + " listed")
        time.sleep(1)

    elif slect == "4":
        print("you have seletcted option 4")
        page = 1
        pos = 0
        printstr = ""
        nextpage = ""
        pages = len(nations)
        pages5 = pages/5
        trupages = round(pages5)

        print("you have seletcted option 1\n")
        print("page 1")
        while nextpage != "0":
            try:
                while pos < page*5:
                    nat = (nations[pos])
                    fac = (Fact[pos])

                    printstr = "\n" + nat + "\n" + fac + "\n"
                    pos += 1
                    print(printstr)
            except IndexError:
                print("end of list")

            print("to quit press 0")
            nextpage = input("< " + str(page) + " >")
            if nextpage == ">" and page < trupages:
                printstr = ""
                page += 1
                print ("Page " + str(page))
            elif nextpage == "<" and page > 1:
                printstr = ""
                page -= 1
                print ("Page " + str(page))
            else:
                    print ("can not do this")
            print("\n")
    elif slect == "5":
        query = input("what nation do you want to serch for?")
        results = wikipedia.search(query)
        print(results)
        reslesc = input("what page do you want")
        page = wikipedia.page(reslesc)
        print(page.content)
    elif slect == "6":
        print("quit has been selected")
        sys.exit()
    else:
        print("enter 1-5")