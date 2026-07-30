'''
token -->variable,punctuators

variables --> Name memory location,its a placholder for data
#rules are to be followed

#multiassignment of variables

name,age,place,='codegnan',7,'hyderabad'
print(name,age,place)
print(name,age,place,sep=',')
print(name,age,place,sep='----->')

#a,b=2,4,5 #valueerror as too many values to unpack
#reaassigning variables

name="codegnan"
a,b=45,1.5
print(a,b)
a,b=b,a
print(a,b,sep=',')


a,b=b,c #nameerror as c is not defined
#print(a,b)

#deleting the variable-->del
#del a
#print(a)
del a,b
print(a,b)

punctuators --> [](lists),()(tuples),{}(dict,sets)
name='codegnan';age=7;course='data_analysis'
print(name,age,course)
'''
#datatypes -->numeric (int,float,complex),boolean,none,
            #-->sequences -->lists,tuples,sets,strings,
            #  forzensets,mapping(dict)

#numeric type -->int,float,complex

#int datatype --> quantity,age..
age =7
print(age)
print(type(234))
'''
#quantity=03 #it is not allowed
#print(quantity)

#float datatype--> temp,salary,price
price =750.24;discount)
print(type(price))

#complex -->combination of rael and imag
i2=4
data =5+i2
print(data)

data=5+2j #j is imag repreasentation
print(data)
print(type(data))

#boolean -->True/False

valid =True
print(type(valid))

error =False
print(type(error))


#typecasting -->converting one type to another type
#python by default follows implaict type (we need not mention the datatype)

age=35
print(type(age))
b=float(age)
print(b)
c=complex(age)
print(c)
d=bool(age)
print(d)
e=bool(0)
print(e)

price=750.45
print(type(price))
d=int(price)
print(d)
print(type(d))
e=complex(price)
print(e)
print(type(e))
f=bool(price)
price(f)


#complex -->typecasting-->int,float,bool
data=2+5j
print(type(data))
#b=int(data))


'''
e= int(float(bool(45)))

print(e)

f =45+2.5+2+3j+False
print(f)






























               
               
               







