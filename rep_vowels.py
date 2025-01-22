sentence = "Python is fun and Python is easy to learn!"
vowels = "aeiou"
for letter in sentence:
    if letter.lower() in vowels:
        print(letter.upper(), end = "")
    else:
        print(letter, end="")
