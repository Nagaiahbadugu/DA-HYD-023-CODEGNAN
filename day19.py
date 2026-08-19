'''
def sample (*args):
    """simple demo for *args"""
    print(args)
    print(type(args))
sample()
sample(1,3,5,6)
sample('codegnan','saketh',23)
details = [24,45,35,65]
sample(details)
sample(*details)

a,b,c =13,4,'da'
print(a,b,c)
a,b,*c= 'python','codegnan',23,45,9.7,'data'
a,b,*=34 ,'codegnan'
print(a)
print(b)
print(c)
c.extend([23,45,6,7])
print(c)

#task --> we wanted to calculate the sum of given objects using funtion
def add(*a):
    """sum of given objects"""
    print(a)
    print(type(a))
    result = 0
    for i in a:
        if type(i) == int or type(i) == float:
            print(i) 
        result = result + i
    return result
#print(add())
#print(add(12,3,4,5))
#print(add(1,2,3,4.5))
#print(add(3,4,5,'poll','dear',45,4.5))
#print(add(23,4,5.5,2+4j56,'code',23))
b=list(map(int,input("enter the values").split(',')))
print(add(*b))#* is used to unpack the values from collection
print(b)
print(*b)
for i in b:
    print(i,end=' ') #same as here

#keyword variable length argument --> we can pass any number of keyword arguments we use ** representation

def details(**kwargs):
    """usage of **kwargs demo"""
    print(kwargs)
    print(type(kwargs))
details() #returns empty dictionary
#deatils(2,3,4,6,)
details(name="codegnan",place="hyd",batch="da")
batch= {'number':'da23','place':'hyd'}
details(**batch)
'''
def sample (*a,**b):
    """usage of both variable length and keyword variable length args"""
    result = 0
    for i in a:
      if type (i) in (int,float,complex):
          print(result)
    for key ,value in b.items():
        print(f'key is {key}')
        print(f' value is {value}')
sample(2,4,5,'police','codegnan',3.5,
       name="codegnan",
       place="hyd",
       batch="da23")


























