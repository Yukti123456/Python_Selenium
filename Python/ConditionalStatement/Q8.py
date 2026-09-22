# 10. File Extension
#
# Take a file extension:
#
# py
# java
# js
# html
# css
#
# Print the type of file.

file = input("Enter file name: ")

match file:
    case "py":
        print("Python file")
    case "java":
        print("Java file")
    case "js":
        print("JS file")
    case "html":
        print("html file")
    case "css":
        print("CSS file")
