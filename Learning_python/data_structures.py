# Lists
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

print(len(days_of_week))

for days in days_of_week:
    print(days)


# print("The second last day of the week is {}".format(days_of_week[-2]))

# print("The weekdays are: {} ".format(days_of_week[-4:1]))

# if "Friday" in days_of_week:
#     print("Yes, Friday is in days of the week")
# else:
#     print("No, its not!")
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
