'''
4,6,1,0,2,4,0,6
write a python program to calculate the innings and count the boundries 4,6,1,0,2,4,0,6

total_score = 0
boundaries = 0
dot_balls = 0
balls = int(input("Enter the number of balls faced: "))
for i in range(1, balls + 1):
    runs = int(input(f"Enter runs scored on ball {i}: "))
    total_score += runs
    if runs == 0:
        dot_balls += 1
    if runs == 4 or runs == 6:
        boundaries += 1
print("\n----- Innings Summary -----")
print("Balls Faced :", balls)
print("Total Score :", total_score)
print("Boundaries  :", boundaries)
print("Dot Balls   :", dot_balls)
'''
pin = 1234
max_attempts = 3
current_attempt = 0
while current_attempt <= max_attempts:
    entered_pin = input("enter the phone lock pin:")
    if entered_pin == pin:
        print("login sucessful")
        break
    print("entered PIN is wrong..try again carefully")
    current_attempt +=1
else:
    print("phone locked")
