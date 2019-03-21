"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random

VOWELS = "aeiou#"
CONSONANTS = "bcdfghjklmnpqrstvwxyz%"
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
word_format = ""
rand_int = random.randint(0, 20)

for i in range(0, rand_int):
    word_format += random.choice(ALPHABET)
word = ""

for kind in word_format.lower():
    if kind in CONSONANTS:
        word += random.choice(CONSONANTS)
    else:
        word += random.choice(VOWELS)

print(word)
