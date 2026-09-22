from curses.ascii import isdigit

str = "I am a Gir45ls"
print(str.endswith("ls"))
print(str.capitalize())
print(str.replace("ls","op"))
print(str.find("am"))
print(str.count("am"))
print(str)# as string are immutable we need to change in original strings
print(str.isdigit())