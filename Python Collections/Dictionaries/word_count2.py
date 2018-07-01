# E.g. word_count("I do not like it Sam I Am") gets back a dictionary like:
# {'i': 2, 'do': 1, 'it': 1, 'sam': 1, 'like': 1, 'not': 1, 'am': 1}
# Lowercase the string to make it easier.

def word_count(new_string):
    words = list(new_string.lower().split())
    words.sort()
    print(words)
    dictionary = {}
    while True:
        for i in range(len(words)-2):
            count = 1
            #print(i)
            if words[i] == words[i+1]:
                count += 1
                i += 2
                print(words[i])
                pass
            elif i == len(words) - 2:
                break
            dictionary[words[i]] = count
            print(dictionary)
    return dictionary


print(word_count("I do not like it Sam I Am"))
