print('Enter a word: ')
word = raw_input()

num_letters = 0
num_vowels = 0
vowels = "aeiou"

for letter in word:
    if letter.isalpha():
        num_letters += 1
    if letter.lower() in vowels:
        num_vowels += 1

num_consonants = num_letters - num_vowels

print "Number of letters: ", num_letters
print "Number of vowels: ", num_vowels
print "Number of consonants: ", num_consonants
