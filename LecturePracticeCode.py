"""
Title: Lecture Practice Code
"""

"""
words = ["great", "oolong", "apple", "panda", "igloo", "banana"]
vowels = ["a", "e", "i", "o", "u"]

for word in words:
    if word[0] in vowels:
        words.insert(0, words.pop(words.index(word))) 

print(words)
"""

words3 = ["tel", "bob", "cat", "dog", "huh", "pol", "num"]
for word in words3:
    if word[0] == word[-1]:
        print(word)