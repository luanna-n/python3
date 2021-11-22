#filter OUT some values => if TRUE, stays // if FALSE, goes out
#filter(function, data)

grades = ['A', 'B', 'F', 'F', 'C', 'A']

#using filter function
def remove_fails(grade):
    return grade != 'F'
print(list(filter(remove_fails, grades)))

#using for loop
better_grades = []
for grade in grades:
    if grade != 'F':
        better_grades.append(grade)
print(better_grades)

#using list comprehension
comp_grades = [ grade for grade in grades if grade != 'F']
print(comp_grades)