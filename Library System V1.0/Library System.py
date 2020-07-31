import functions

functions.library.initialize()
name = functions.library.getname()
year = functions.library.getyear()
print("Welcome", name, year)
option = functions.library.options()

if option == "1":
    file = open("log.txt", "a")
    bookout = input("What book would you like to take out?")
    out = name + " from year " + year + " took out " + bookout
    print(out)
    file.write(out)
    file.close()

elif option == "2":
    file = open("log.txt", "a")
    bookin = input("What book would you like to put back?")
    out = name + " from year " + year + " put back " + bookin
    print(out)
    file.write(out)
    file.close()

elif option == "3":
    file = open("log.txt", "r")
    print(file.read())
