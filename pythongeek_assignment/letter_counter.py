word = input("Please enter a word: ")

letter_count = {}

for letter in word:
    if letter in letter_count:
        letter_count[letter] += 1
    else:
        letter_count[letter] = 1

print("\nLetter count")
for letter, count in letter_count.items():
    print(f"{letter}: {count}")

