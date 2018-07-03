def combo(*args):
     l = len(args[0])
     list_of_tuples = []
     for i in range(l):
        list_of_tuples.append((args[0][i], args[1][i]))
     return list_of_tuples

print(combo([1, 2, 3], 'abc'))
