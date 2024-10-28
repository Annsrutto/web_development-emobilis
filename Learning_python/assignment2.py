score = int(input("Please enter your score: "))

if score < 0 or score > 100:
    print("Please enter a value between 0 and 100")
else:
    if score >= 90:
        print("You got an A🤩")
    elif score >= 80:
        print("You got a B")
    elif score >= 70:
        print("You got a C")
    elif score >= 60:
        print("You got a D")
    else:
        print("You got an F🥲")

