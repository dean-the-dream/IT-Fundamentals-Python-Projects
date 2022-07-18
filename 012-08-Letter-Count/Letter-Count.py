sentence = input("Type any sentence: ")
letter_count = dict()
for i in sentence:
    if (i not in letter_count):
        number = sentence.count(i)
        letter_count[i] = number
print(letter_count)
