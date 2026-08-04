'''
usage of else with for --> the else keyword


longest_sreak =0 #target variable
current_streak =0
for day in work_log:
    if day == 1:
        #print(day)
        current_streak = current_streak + 1
        if current_streak > longest_steak:
            longest_streak =current_steak
            print(f'longest_streak is {longest_streak}')
            else:
            current_streak = 0 #streak breaks
            else:
            print (f'longest_streak is {longest_sreak}')
            break
        else:
            current_streak =0 #streak breaks

#in this case when the entire loop execution is done we get result of
#else block


notifications = [0,0,0,0]
notifications =list(map(int,input("enter the values --> 0 or 1:").split(',')))
print (notifications)
for notifiacation in notifications:
    if notification ==1:
        print('unread notification')
        break
    else:
        print('all caught up')


syntax while:
while <condition>:
    statement(s)......
    ......

while True :
    print("yes")

i=10
while i>=1:
    print(i)
    i=i-1 #counter

i=0
while i<=10:
    print(10-i)
    i=i+1
'''
pin = "2612"
max_attempts = 3
current_attempt = 0
while current_attempt <= max_attempts:
    entered_pin = input("enter the ATM PIN:")
    if entered_pin == pin:
        print("login sucessful")
        break
    print("entered PIN is wrong..try again carefully")
    current_attempt +=1
else:
    print("account locked,try after 24hours...")
        
    





















            
            
