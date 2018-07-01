def sillycase(given_string):
    new_string = given_string[: len(given_string) // 2].lower()
    new_string += given_string[(len(given_string) // 2) :].upper()
    return new_string
    


print(sillycase("Treehouse"))
