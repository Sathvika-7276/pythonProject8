"""
Word Occurrences
Estimate: 30 minutes
Actual:   1 hour
"""

dictionary = {}
text = input("Text:")
total_words = text.split()
for word in total_words:
    if word in dictionary:
        dictionary[word] += 1
    else:
        dictionary[word] = 1

words_in_dictionary = list(dictionary.keys())
words_in_dictionary.sort()

max_length = max((len(word) for word in words_in_dictionary))
for word in words_in_dictionary:
    print(f"{word:{max_length}} : {dictionary[word]}")
