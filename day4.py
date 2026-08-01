'''
identity operators -->checks the identity of an object -->id()
#is,is not

a=5
b=a
print(id()a)
print(id(b))
c=5
print(id(c))
print(a is c)
print(5==5)

a=[1,3,5,6]
b=a
print(id(a))
print(id(b))
c=[1,3,5,6]
print(id(c))

print(c is a)
print(c==a)
print(a is not c)

#Bitwise operaators
#$(and), | (or),^(XOR),shifting operators (<<,>>)

print(5&3)
print(5|3)
print(5^3)
print(5 and 3)
print(5 or 3)


print(5<1)
print(5<<1)
print(5>>1)
print(15<<2)
print(15>>2)

names = input("enter the names:").split(',')
print(names)

name1,name2=map(str,input("enter the friends names:").split(,))
print(name1,name2)


syntax:

if <condition>:
    statement(s)...
    .....

age=15
age= int(input("enter the age:"))
if age >=18:
    print('your age is:',age)

age= int(input("enter the age is:"))
if age>=18 and age in [19,21,20]:
    print ('your age is'age)
    print(age)


#else keyword --> if-else

else:
      #statement(s)..
if else usage below:
if <condition>:
    statement(s)...
    ....
 else:
     statement(s)....
     ....


age= int(input("enter the age:"))
if age>=18:
    print("you have voter eligibility and age is",age)
    print("acess granted")
else:
    age=18-age
    print("you need to wait for more",age,"years")

if age>0:
    if age>=18:
    print("you have voter eligibility and age is",age)
    print("acess granted")
else:
    age=18-age
    print("you need to wait for more",age,"years")
else:
    print("you have entered -ve values /zero enter only +ve")


task :student marks and grade analyzer
90-100 -->'A'
80-89 -->'B'
70-79 -->'C'
60-69 -->'D'
>60 --> fail


marks = int(input("enter the marks"))
if marks >=90:
    print("the grade is: A")
else:
if marks >=80:
print("the grade is: B")
else:
if marks >=70:
print("the grade is: C")
else:
if marks >=60:
print("the grade is : D")
else:
print("the grade is: fail")
'''
marks = int(input("enter the marks:"))
if marks >= 90:
    print("The grade is: A")
else:
    if marks >= 80:
        print("The grade is: B")
    else:
        if marks >= 70:
            print("The grade is: C")
        else:
            if marks >= 60:
                print("The grade is: D")
            else:
                print("The grade is: fail")                      
            
 
    
    
    




































