'''
sequence --> strings,lists,tuples,sets,frozenset
mappling -> dictionary

#sets --> a set is a unique collection of objects,unordered,mutable,
#hashing,unindexed,unique,heterogenous
#set(),{}
#a = {} its an empty dictionary
a = set()
print(type(a))
stud_ids = {123,345,234,564,234}
print(stud_ids)
print(type(stud_ids))
print(len(stud_ids))
print(len(stud_ids))
#print(stud_ids[2]) #typeerror

print(234 in stud_ids)
#print(stud_ids*2) #sets can't be repeated
#print(stud_ids+ stud_ids) #two sets cannot be merged

#data={12,3,4,5,[12,3,4],'saketh'}
#print(data)#no lists inside a set (hashing technique) lists are mutable

data={12,3,4,5,(12,3,4),'saketh'}
print(data)
print(len(data))
for i in data:
    print(i)

#method on sets --> add(),update(),remove(),discard(),pop()

names={'sai','saketh','kiran','codegnan'}
print(len(names))
names.add('python')
print(names)
#names.add('saketh','poll')
#print(names)
names.add(('poll','police'))
print(names)
'''
da_names = {'mani','akash','sai','sonu'}
'''
#update() we can update multiple element(set)
names.update(da_names)
print(names)
print(len(names))
print(da_names)
print(len(da_names))
da_names.update(names)
print(len(names))
print(len(da_names))

#remove(),discard(),pop(),clear()
da_names.remove('sai')
print(da_names)
#da_names.remove('sai')#keyerror
#discard() will remove an element if its present else it ignores
da_names.discard('codegnan')

da_names.pop()
print(da_names)
print(da_names.pop())#removes and returns an arbritary element
print(da_names)
da_names.clear()
print(da_names)
da_names.add('saira')
print(da_names)
da_names.update(['sai','akash'])
print(da_names)

#copy()
d = da_names.copy()
print(d)
d.update({'python','codegnan'})
print(d)
print(da_names)

#mathematical operations --> union(),intersections(),difference(),symmetric_da()
#issubset(),issuperset(),isdisjoint()

da_23 = {12,23,34,45,23,36}
da_24 = {34,46,47,23}

event = da_23.union(da_24)
print(event)
print(len(event))
#common = da_23.intersection(da_24)
common = da_23 & da_24 #& intersection()
print(common)
print(len(common))
common = da_23.intersection_update(da_24)
print(common) #it returns none
print(da_23) #common element are finally stored

print(da_23)
print(da_24)
#difference() removes common elements and prints remaining elements from first selection
#diff = da_23.difference(da_24)
#print(diff)
#f = da_23 - da_24
#print(f)
#symmetric difference() --> removes common elements and print all remaining
#elements from two sets
symm = da_23.symmetric_difference(da_24)
#print(symm)
h = da_23^ da_24
#print(h)

#issubset() --> checks for all elements to be present in other set
da_24.remove(46)
da_24.remove(47)

print(da_24.issubset(da_23))
print(da_23.issuperset(da_24))

#isdisjoint() returns False for sets having common elements
print(da_23.isdisjoint(da_24))
'''






































    
