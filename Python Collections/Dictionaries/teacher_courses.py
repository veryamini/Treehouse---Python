# The dictionary will look something like:
# {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
#  'Kenneth Love': ['Python Basics', 'Python Collections']}
#
# Each key will be a Teacher and the value will be a list of courses.
#
# Your code goes below here.

# Returns total number of teachers
def num_teachers(dictionary):
    number_of_teachers = 0
    for key in dictionary.keys():
        number_of_teachers += 1
    return number_of_teachers

# Returns totals umber of courses in the dictionary
def num_courses(dictionary):
    number_of_courses = 0
    for value in dictionary.values():
        for course in value:
            number_of_courses += 1
    return number_of_courses

#Returns a list of all courses in the dictionary
def courses(dictionary):
    list_of_courses = []
    for value in dictionary.values():
        for course in value:
            list_of_courses.append(course)
    return list_of_courses

# Returns the name os the teacher with the most courses
def most_courses(dictionary):
    max_count = 0
    for item in dictionary.items():
        if len(item[1]) > max_count:
            max_count = len(item[1])
            teacher = item[0]
    return teacher

# Returns a list of lists with the name of the teacher and number of courses e.g. [["Kenneth Love", 5], ["Craig", 10]]
def stats(dictionary):
    teacher_courses_list = []
    for item in dictionary.items():
        teacher_courses_list.append([item[0], len(item[1])])
    return teacher_courses_list
        
