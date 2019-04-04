string = input("Please enter a string: ")

words = string.lower().split(" ")
words.sort()
word_to_frequency = {}

for word in words:
    word_to_frequency[word] = word_to_frequency.get(word, 0) + 1

longest_word_length = max(len(word) for word in words)

for word in word_to_frequency:
    print("{:{}} : {} times".format(word, longest_word_length, word_to_frequency[word]))
