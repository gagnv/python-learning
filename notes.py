#using the str function to make the game to find what would be your name without any vowel but strip is only applicable in the end and start
name = input("What is your name: ")
print ("hello,", name. strip("aeiou"))

# I will write every other function which I learn in the python class here.

#print function, also these greyish lines are known as pseudocode, you can save them as comments to guide you in the process
note = input("z")
print ("z")

#input=string, basically strings are words, also for quotes do the following
print ('"This is a quote"')

#multiple function arguments for concatenation or anything in general
name = input ("What is your name: ")
surname = input ("What is your surname: ")
print (name + " " + surname)

#multiple function argument but using the comma method
name = input ("Haa oye naa ki ae tera? ")
surname = input ("Je naa dass reha, surname bhi dass de: ")
print (name, surname)

#Saying hello to the user while using the sep function
name = input("What is your name? ")
print ("hello", name, sep=("SUPRA"))

#format string one of the most important concept
name = input("What is your name: ")
print ("hello,", f"{name}")

#using the capitalize, split and lower functions
name = input ("What's your name huh: ")
print ("hello,", name.capitalize())
print ("hello,", name.title())
print ("hello,", name.lower())

#using title, lower and strip
name = input("Input your name mr/ms: ")
surname = input("Input your surname mr/ms: ")
name = name.strip("gn").title()
surname = surname.strip("h").lower()
print (f"hello, {name} {surname}")

#using the split function
name = input("What is your name: ")

first, last = name.split(" ")
print (f"hello, {first}")

#THIS METHOD SHOWS INCONSISTENT DECIMAL DISPLAY, TO SHOW CONSISTENT DECIMAL DISPLAY REMOVE THE ROUND AND 2, instead do the below thing
X = float(input("Value of x: "))
Y = float(input("Value of y: "))
Z = round(X+Y, 2)

print (f"{Z:,}")

#by using formatting string
X = float(input("Value of x: "))
Y = float(input("Value of y: "))
Z = X+Y

print (f"{Z:,.2f}")