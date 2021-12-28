from operator import itemgetter
def sort_employees(employees, sort_by):
    if sort_by == "name":
        return sorted(employees, key=itemgetter(0))
    if sort_by == "age":
        return sorted(employees, key=itemgetter(1))
    if sort_by == "salary":
        return sorted(employees, key=itemgetter(2))