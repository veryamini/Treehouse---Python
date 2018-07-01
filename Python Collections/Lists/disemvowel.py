def disemvowel(word):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    word_list = list(word)
    print(word_list)
    for vowel in vowels:
        if vowel in word_list:
            try:
                word_list.remove(vowel)
            except ValueError:
                pass

    word = "".join(word_list)
    return word

print(disemvowel("BiEH"))
