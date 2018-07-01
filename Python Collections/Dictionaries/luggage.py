def packer(**kwargs):
    print(kwargs)
    

def unpacker(first_name=None, last_name = None):
    if first_name and last_name:
        print("Hi {} {}!".format(first_name, last_name))
    else:
        print("Hi no name!")

        
def unpack(**d):
    return "Hi, I'm {name} and I love to eat {food}!".format(d["name"], d["food"])
    
packer(name = "Kenneth", num = 42, spanish_inquisition=None)
unpacker({"last_name": "Love", "first_name": "Kenneth"})
print(unpack({"name": "Yamini", "food": "Pasta"}))