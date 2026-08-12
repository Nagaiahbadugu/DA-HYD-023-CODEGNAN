'''
a='welcome to PYTHON'

print(a.upper())
print(a.lower())
print(a.title())
print(a.capitalize())
print(a.swapcase())
print(a.isupper())
print(a.islower())
print(a.istitle())
print(a.casefold())
'''
'''
a='PYTHON IS FUN and Learning python'
print(a.upper())
print(a.lower())
print(a.title())
print(a.capitalize())
print(a.swapcase())
print(a.isupper())
print(a.islower())
print(a.istitle())
print(a.casefold())

#PYTHON IS FUN and Learning python

text = input("Enter a sentence: ")

methods = ["upper", "lower", "title", "capitalize", "swapcase", "islower", "isupper"]

for method in methods:
    if method == "upper":
        print("Uppercase:", text.upper())

    elif method == "lower":
        print("Lowercase:", text.lower())

    elif method == "title":
        print("Titlecase:", text.title())

    elif method == "capitalize":
        print("Capitalize:", text.capitalize())

    elif method == "swapcase":
        print("Swapcase:", text.swapcase())
    elif method == "islower":
        print("islower:", text.islower())
    elif method == "isupper":
        print("isupper:", text.isupper())


# Describe the original text
if text.isupper():
    print("Original text is uppercase")
elif text.islower():
    print("Original text is lowercase")
elif text.istitle():
    print("Original text is titlecase")
else:
    print("Original text has mixed case")
'''

while True:
    username = input("Enter username (or quit): ")

    if username.lower() == "quit":
        break

    if not username.isalnum():
        print("Invalid: Username must contain only letters and numbers.")

    elif not username[0].isalpha():
        print("Invalid: Username must start with a letter.")

    elif not username.isidentifier():
        print("Invalid: Username is not a valid Python identifier.")

    elif not username.isascii():
        print("Invalid: Username contains non-ASCII characters.")

    else:
        print("Valid username!")


































