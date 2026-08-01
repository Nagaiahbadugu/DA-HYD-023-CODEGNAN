
'''
marks = int(input("enter the marks (0-100):"))
if mark >o and marks <=100:
    if marks >=90:
        print("user has secured grade A")
    if print >=80 and print <=89: 
        print("user has secured grade B")
     if print >=70 and print <=79:    
        print("user has secured grade C")
     if print >=60 and print <=69:    
        print("user has secured grade D")
     if marks <60:
        print("user has failed,study again ")


marks =int(input("enter the students marks:"))
if marks >100:
    print("entered values should be greater than 1 and less than 100")
elif marks >=90 and marks <=100:
    print("user has secured grade A")
elif marks >=80 and marks <=89:
     print("user has secured grade B")
elif marks >=70 and marks <=79:
     print("user has secured grade C")
elif marks >=60 and marks <=69:
     print("user has secured grade D")
     
   
age= int(input("enter the age:"))
if age>=18 and age <=100:
    print('______ user has vote eligibility_____')
    print('_______ access granted _______')
elif age<18 and age >0:
    print('______user still need to get vote eligiblity____')
    print('______user need to wait for more',(18-age),'year(s)_____')
elif
    print('_____only +ve values and less than 100 acceptable____')
    

a,b =7,9
print(a)
print(b)
print(a,b)
name = "codegnan";batch="data analytics"
print(name,batch)
print(name,batch,sep=',')
print(name,batch,end='------->')

#end='\n', \t --> tab space
print(name,batch,end='\t')
print(a,b,end='')
print("hyderabad")'''

name='codegnan';age=7;batch='DA-023';place='hyderabad'
#usage of commas
print(batch,'is in',name) #variables and msg to be separated by comma
print(name,'is in',place,'age is',age,'years')
#Old style formatting --> %d -->integer,%s-->string,%f-->float
salary = 24253.256
print("His Salary is %d"%(salary))
print("His Salary is %f"%(salary))
print("His Salary is %.1f"%(salary)) #%.1f --> rounding to 1 decimal
'''
#.format() usage
print("{} is in {}".format(name,place)) #order matters

#fstring usage (more recommended)

print(f'{name} is in {place}')
print(f'{"Saketh"} is in {name}')






































