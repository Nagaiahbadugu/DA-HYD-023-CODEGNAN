'''
squence --> strings,lists,tuple,sets
Maping--> dictionary


#lists --> collection of heterogenous elements(items)
#lists --> indexed,ordered,mutable,heterogenous, we use [] to store the data

marks=[35,25,21,45]
print(marks)
print(len(marks))
print(type(marks))
print(45 in marks)

#operations : indexing,slicing,striding,membership,merging,repetition

#nested lists --> a list inside another list

names = ['codegnan',25,4.6,[45,35,25,65],'DA23',34]
print(len(names))
print(names[0])
print(names[3])
print(names[-3])
print(type(names[0]))
print(names[0][:4])#it returns code
print(names[0][4:])
print(names[0][::2])
names[0] = names[0][::-1]
print(names)

print(names[3])
print(len(names[3]))
print(names[3][2])
#indexing,slicing -->mutable
names[2]='python'
print(names)
#by indexing if we change the elements, length of collection will remain same

names[4] = ['codegnan','PFS','JFS','DA','AAA','DS']
print(names)
print(len(names))
print(names[4][0][4:])

names[2:4]= 'abhiram','sai','saketh','sairam'
print(names)

#in slicing whatever elements u pass as per the logic length keeps on increase
names[2:4]= 'abhiram','python','saketh','java'
print(names)


(names[3:6:2])=['python','java']
print(names)
#create a nested list with strings,lists and work on indexing,slicing,striding
#added advantage if u could add string functions also to it
#lists functions --> append(),insert(),extend(),pop(),remove(),clear()
#index(),count(),copy(),sort(),reverse()
'''
names=['codegnan','saketh']
#append() --> inserts single elements to the end of the list
names.append('data')
print(names)
names.append(['analysis','agents'])
print(names)
#append() will always increment the length of list by 1
print(names[3])
names[3].append('chatgpt')
print(names)
print(names[3])

#extend() --> inserts multiple elements to the end of lists

names.extend('analysis') #string will be splitted
print(names)
names.extend(['analysis'])
print(names)
names.extend([45,75,24,56])
print(names)
#names.extend(35,45) typeerror
#print(names)

















