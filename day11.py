code = "python"
total_attempts = 3
current_attempt = 0

while current_attempt < total_attempts:
    entered_code = input("Enter the code: ")

    current_attempt = current_attempt + 1
    remaining = total_attempts - current_attempt

    if entered_code == code:
        print("Code success")
        print("You have", remaining, "more chances")
        break
    else:
        print("Incorrect code")
        print("You have", remaining, "more chances")

if current_attempt == total_attempts and entered_code != code:
    print("You lost the game")
































        
