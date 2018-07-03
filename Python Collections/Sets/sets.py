COURSES = {
    "Python Basics": {"Python", "functions", "variables",
                      "booleans", "integers", "floats",
                      "arrays", "strings", "exceptions",
                      "conditions", "input", "loops"},
    "Java Basics": {"Java", "strings", "variables",
                    "input", "exceptions", "integers",
                    "booleans", "loops"},
    "PHP Basics": {"PHP", "variables", "conditions",
                   "integers", "floats", "strings",
                   "booleans", "HTML"},
    "Ruby Basics": {"Ruby", "strings", "floats",
                    "integers", "conditions",
                    "functions", "input"}
}

def covers(courses):
    list_of_courses = []
    for course in courses:
        for item in COURSES.items():
            if course in item[1]:
                list_of_courses.append(item[0])
    return list_of_courses


def covers_all(courses):
    list_of_all_courses = []
    for item in COURSES.items():
        for course in courses:
            if course not in item[1]:
                try:
                    list_of_all_courses.remove(item[0])
                except ValueError:
                    pass
            else:
                list_of_all_courses.append(item[0])
    return list_of_all_courses
            
