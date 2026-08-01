'''
age= int(input('enter the age:'))
print(age)
print (type(age))



name= input ("enter the name:")
print(name)
print(type(name))

marks = int(("enter the marks")).split()

a=input("enter the values").split(',')
print(a)



marks =list(map(int,input("enter the values").split(',')))
print(marks)

age,salary = map(int,input("enter the values").split(','))
print(age)
print(salary)


age,salary = map(float,input("enter the values").split(','))
print(age)
print(salary)


print(5+3)
print(5-3)
print(5*3)
print(5/3)
print(5//3)
print(5%3)
print(5**3)

length,breadth = map(int,input("enter the values").split(','))
area = length * breadth
print(area)

a=45
print(a)
a=a+5
print(a)
b=35
b+=a
print(b)

#task: *=,/=,//=,%=,**= workout


# comparsion operators
age =25
print(age==25)
print(age !=35)
print(age<=25)
print(age>35)
print(age>=35)
print(-5< -1)

#membership operators -->in,not in-->boolean
#it cheaks for the existence of an object in a collection

marks = [56,75,45,85]
print(35 in marks)

print(25 not in marks)
print('code'in 'codegnan')
print('$'in 'abc$frg')

a=(25 in [25,45,65])and 45<56
print(a)
b=45>56 or 25 <=45
print(b)
c= not(True)
print(c)
'''
a=35
b=35
print(id(a))
print(id(b))
print (a is b)
c=a
print(id(c))
print(c is a)

a= [1,3,4,5]
print(id(a))




















































































