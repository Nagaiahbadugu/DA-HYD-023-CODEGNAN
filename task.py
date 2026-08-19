Marks=int(input("Enter Marks:"))
if Marks>100:
    print("Invaild,Enter the marks")
elif Marks>=90 and Marks<=100:
    print("Grade:A")
    print("Outstanding!")
elif Marks >=80 and Marks <=89:
    print("Grade:B")
    print("Excellent")
elif Marks >=70 and Marks <=79:
    print("Grade:C")
    print("Good")
elif Marks >=60 and Marks <=69:
    print("Grade:D")
    print("Fair,needs to improvement!")
elif Marks >=50 and Marks <=59:
    print("Grade:E")
    print("Fair,needs to improvement!")
else:
    print("Grade:F")
    print("Failed,needs to reppear!")

num=int(input("Enter a number:"))
if num==0:
   print("Zero is neither even nor odd")
elif num<0:
    if num%2==0:
        print("Negtive Even Number")
    else:
        print("Negative odd nUmber")
else:
    if num%2==0:
        print("even number")
    else:
        print("odd")

months=int(input("Enter a month number:"))
if months>12:
    print("Invalid month entred")
elif months==12 or months ==1 or months == 2:
    print("Winter")
elif months ==3 or months ==4 or months ==5:
    print("Spring")
elif months==6 or months ==7 or months ==8:
    print("Summer")
else:
    print("autumun")
        







































                                                
