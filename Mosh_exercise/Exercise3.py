sentence = input("Enter the sentence: ")

char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

highest_repeated= list(sorted(char_frequency.items(), key=lambda kv:kv[1],reverse=True))
print("The char which is repeated the most is: ",highest_repeated[0])


