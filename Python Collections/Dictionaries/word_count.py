# E.g. word_count("I do not like it Sam I Am") gets back a dictionary like:
# {'i': 2, 'do': 1, 'it': 1, 'sam': 1, 'like': 1, 'not': 1, 'am': 1}
# Lowercase the string to make it easier.

def word_count(new_string):
    words = list(new_string.lower().split())
    dictionary = {}
    for word in words.copy():
        count = 1
        temp = word
        print(word)
        for new_word in words:
            if  new_word == temp:
                count  += 1
        dictionary[word] = count-1
    return dictionary

print(word_count("I do not like it Sam I Am"))

# Sort the list and delete the variables which are duplicates and check the loop from 0
