def unpack(dictionary):
    return "Hi, I'm {name} and I love to eat {food}!".format(name = dictionary["name"], food = dictionary["food"])

def unpacker(first_name=None, last_name = None):
    if first_name and last_name:
        print("Hi {} {}!".format(first_name, last_name))
    else:
        print("Hi no name!")


def unpacked(**d):
    if name and food:
        return "Hi, I'm {name_a} and I love to eat {food_a}!".format(name_a = name, food_a = food)
    

unpacker({"last_name": "Love", "first_name": "Kenneth"})
print(unpack({"name": "Yamini", "food": "Pasta"}))
print(unpacked({"name": "Yamini", "food": "Pasta"}))

