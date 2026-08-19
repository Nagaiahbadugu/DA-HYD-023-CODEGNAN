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

#formatted student report

text='STUDENT REPORT'
print(text.center(40))
b='name'
print(b.ljust(10),end='\t')
c='marks'
print(c.rjust(10),end='\t')
d='grade'
print(d.rjust(10),end='\t')
for i in range(3):
'''


for i in range(3):
    name=input('name:')
    marks=int(input('marks'))
    
    if marks >= 80 and marks <=100:
        Grade = 'A'
    elif marks >=60 and marks <=79:
        Grade = 'B'
    elif marks >=40 and marks <=59:
        Grade = 'C'
    elif marks < 40:
        Grade = 'fail'
    else:
        print('Invalid number')
    print(f"{name.ljust(10)}{str(marks).rjust(10)}{Grade.rjust(10)}")
print(name)
print(marks)
print('student report'.center(50))
print(f"{'name'.ljust(10)}{'marks'.rjust(10)}{'Grade'.rjust(10)}")
    
#star printing pattern

'''
for i in range(3):
    for j in range(5):
        if i==2 or j==2 or i==1 and j==1 or i==1 and j==3:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
'''
'''
for i in range(3):
    for j in range(5):
        if i==0 or j==2 or i==1 and j==1 or i==1 and j==3:
            phgrint("*",end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#character and text analyser
'''
text=input('enter the text:')
count=0
for i in text:
    if i.isalpha():
        count=count+1
print(count)
'''

'''
text=input('enter the text:')
#operations=['Letters','digits','spaces','printable','title case']
letters=digits=spaces=printable=0
for i in text:
    if i.isalpha():
        letters += 1
    elif i.isdigit():
        digits += 1
    elif i.isspace():
        spaces += 1
    elif i.isprintable():
        printable += 1
  
        
        
print('letters:',letters)
print('digits:',digits)
print('space:',spaces)
print('printable:',printable)
#print('title_case:',title_case)

































