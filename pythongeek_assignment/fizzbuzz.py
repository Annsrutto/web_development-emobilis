for number in range(1, 51):
    if number % 3 == 0 and number % 5 == 0:
        print("Fizzbuzz!\nNumber is divisible by both 3 and 5")
    elif number % 3 == 0:
        print("Fizz!\nNumber is only divisible by 3")
    elif number % 5 == 0:
        print("Buzz!\nNumber is divisible by 5")
    else:
        print(number)

