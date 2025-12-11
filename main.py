import grads

students = {
    
    "omar": [90,80,88,78,100],
    "mohamed": [80,50,60,30,100],
    "abdullah": [90,82,88,78,95],
    "yousif": [80,77,60,50,100],    

for student, grades in students.items():
    print(grads.get_student_summary(student, grades))


print(f"class average: {grads.class_average(students)}")

