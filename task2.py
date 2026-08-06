#Task 1-->observe +ve +ve,-ve -ve, +ve -ve,all possibilities

name='nagaiah'
#1.(+ve +ve) indexing-->
print(len(name))
print(name[0:3])
print(name[1:5])
print(name[2:6])
print(name[3:5])
print(name[0:9])

#2.(-ve -ve) indexing-->
name='raghuramulu'
print(len(name))
print(name[-5:-1])
print(name[-8:-5])
print(name[-7:-2])
print(name[-6:-2])
print(name[-9:-4])

#3.(+ve -ve) indexing-->
name='eralaxmi'
print(len(name))
print(name[0:-1]) 
print(name[1:-2]) 
print(name[2:-5]) 
print(name[3:-1])
print(name[0:-4])

#Task: A B C D E F G H I J K L M O P Q R S T U V W X Y Z
#use loops and strings to return A to Z

def get_alphabet():
    result = ""
    for i in range(26):
        result += chr(65 + i) + " "
    return result
print(get_alphabet())
