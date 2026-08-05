'''
tokens
operators
control flow
sequences

#strings --> group of characters ,we use single or double or triple quotes
#for representation of strings...
#strings are immutable,odered,indexed collection

name = "codegnan"
print(name)
print(type(name))
print(len(name))#len --> returns the number of items of container

#index() --> fetch the object (position) starts at 0 and ends at len(obj)
# we use [] representation
print(name[0])
print(name[5])
print(name[25]) #indexerror --> as its out of rangr

#negative indexing --> -1 to len(obj)
print(name[-1]) #it returns last character
print(name[-3])


# slicing --> we can access group of characters(objects)
#we use [start:end]#start default --> 0,start is included,end is excluded
name = "codegnan"
print(name)
print(name[:])
print(name[0:])
print(name[:4])
print(name[1:5])
print(name[4:])

name='python'

print(name[7:3])
print(name[7:3]) #returns empty as strings are immutable
#slicing is applicable from lower to higher index
print(name[:45])
print(name[45:])

print(name[-1:-5])
print(name[-5:-1])

print(name[4:])
print(name[4:6])
print(name[-2:])

print(name[1:-2])
print(name[2:-6])
#observe +ve,+ve,-ve,-ve,+ve-ve all possibilites

#striding --> [start:end:step]

course= 'dataAnalysis'
print(len(course))
#data -->result
print(course[:4])
print(course[4:])
print(course[-3:])

print(course[::1])
print(course[::2])
print(course[1:6:3]) #[1:6] --> [1:6:3] -->aA

print(course[2::3])

print(course[::-1]) #it returns the reverse of a string
print(course[::-2])

#task :workout with all possibilities of slicing and striding on a example

#operations on strings --> indexing, concatenation, repetition

print (name* 3)
print('*'* 25)

#concatenation -> combining strings

data= 'saketh' +'python'+ ''+'database'
print(data)
print('123'*4) #numeric string
print('code' in 'codegnan')

for i in 'codegnan':
    print(i,':')
# in above case we get every character line by line

for i in 'codegnan':
    print(i,end=' ')

name = "dataCodegnan"
#build-in functions --> len(),min(),max(),sorted()
print(len(name))
print(min(name))
print(ord('A'))
print(ord('a'))
print(chr(97))
print(max(name))
print(sorted(name))

#methods on strings --> case-conversations,finding/searching...
name='Codegnan data'
#case-conversations --> upper(),lower(), title(),capitalize()
a= name.upper()
print(a)
b = name.lower()
print(b)

c = name.capitalize()
print(c)
d = name.title()
print(d)
'''
#task : A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# use loops and strings to return A - Z

alphabets= 'A B C D E F G H I J K L M N O Q R S T U V W X Y Z'
letters = alphabets.replace([:26])
for char in letters:
    print(char, end=" ")



























    
          
