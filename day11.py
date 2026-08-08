'''
pin = "2612"
max_attempts = 7
current_attempt = 0
while current_attempt <= max_attempts:
    entered_pin = input("enter the phone PIN:")
    if entered_pin == pin:
        print("login sucessful")
        break
    print("entered PIN is wrong..try again carefully")
    current_attempt +=1
else:
    print("account locked")

secrect= 123
guess =int(input())
while guess != secrect:
    if guess < secrect:
        print("too low")
    else:
        print("too high")
    guess=int(input())
print("correct guess")

food= input()
count=0
while food != "exit":
    count+=1
    food=input()
print("total number of items ordered",count)
'''
secrect="python"
current=0
max_attempt=3
while current < max_attempts:
    a=input()
    if (a== secrect):
        print("access again")
        break
    else:
        remaining=max_attepmts_current
    print(f"wrong guess and you have only")
    current!=1
    else:
        print("the access over")











        
