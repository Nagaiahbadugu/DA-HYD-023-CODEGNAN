'''
control statements --> flow of execution of the program
                -->coditions statements --> if,elif,else...
        --> repetition statements(loops) -->for,while,(for with else)
                                                  (while with else)
                                                  
          -->jumping statements --> break,continuous,pass

#loops --> loops are helpful for repetition(automative tasks)
# for keyword will be helpful to iterate over a sequence /range
#syntax for (for keyword):

for< temp_var> in sequence/ range:
     statements(s).....
     ......

#range(start,stop,step)
for i in range(10):
     print(i)
#in above case we got 10 iterations
    
for i in range(1,10):
    if i > 5:
        print(f' value of i is --> {i}')


if i>5 and i%2 ==0:
        print(f'final value of i is -->{i}')

for i in range(1,10,2):
    print(i)
    print("done")

for i in range(-10,0,1):
    print(i)
    print("done")

names= ['saketh','sairam','akash']
print(len(names))
for name in names:
    print(name)
    print (f'student name is {name}')
if name == "sairam":
    print(f"student name is{name}")

result = 0 #target variable
for i in range(11):
    #print(i)
    #print(f'result is {i+i})
    result = result + i #result +=i
    print(f'now the result is {result}')
    print(f'sum of 10 numbers is {result}')


result = 0
for i in range(21):
    if i%2 ==0 :
        result = result + i 
    print(f'now the result is {result}')
    print(f'sum of 10 numbers is {result}')
'''
work_log =[0,1,1,1,0,1,0]
longest_sreak =0
current_streak =0
for day in work_log:
    if day == 1:
        #print(day)
        current_streak = current_streak + 1
        if current_streak > longest_sreak:
            longest_streak =current_sreak
    else :
            current_streak = 0 #streak breaks
            print (f'longest_streak is {longest_sreak}')
            






























