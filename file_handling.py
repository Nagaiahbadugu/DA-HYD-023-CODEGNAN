'''
File Handling in python: Files are mainly used to store the data
It supports -->>r,w,a(read,write,append) using open()
'''

#first lets understand how we can access.txt files using python
'''
import os
if os.path.exists('sample.txt'):
    file = open('sample.txt','r')
    print('file is loaded successfully')
else:
    print('file not present')

#Now let us access the content from the file
import os
file=open('sample.txt','r')
#print(file)
#print(file.read())
#print(type(file.read()))
#print(len(file.read()))
#a=file.read()
#print(a)
#print(len(a))
print(file)
#print(file.readline()) #reads single line from the file
print(file.readlines()) #reads all lines from the file in a list

#'w' mode --> it automatically creates a new file,if the file is exist
#it overrides the content in it

file = open('data.txt','w')
print(file)
#as the is automatically create lets write content to it
file.write("good afternoon guys,how are you doing?")
file.write("today is wednesday..")
file.close()

#we can also with keyword to avoid close()
with open ('data.txt','w')as f:
    f.write("now checking what happened")


#'a' --> it also automatically creates a file ,but if the files is already
#existing it appends the content to the previous file
with open ('data.txt','w')as g:
    g.write('\n okay let us see how its going')

#+ --> read and write
with open('data.txt','r+')as h:
    print(h.read())
    h.write("today is wednesday")
'''
#file operations size and path
import os
file = open('data.txt')
if os.path.exists('data.txt'):
    print("file size is",os.path.getsize('data.txt'),"bytes")
    print("file absolute path is",os.path.abspath('data.txt'))
else:
    print("file is not present")






