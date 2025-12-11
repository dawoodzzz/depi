
def calculate_average(grades):
    return sum(grades)/len(grades)

def assign_grade(avrage):
    if avrage>=90:
        return "A"
    elif avrage>=80:
        return "B"
    elif avrage>=70:
        return "C"
    elif avrage>=60:
        return "D"
    else:
        return "F"
    
def get_student_summary(student_name, grades):
    average = calculate_average(grades)
    grade = assign_grade(average)
    return f"{student_name} \n average: {average} \n grade: {grade}"

def class_average(students):
    averages = []
    for student,grads in students.items(): 
        averages.append(calculate_average(grads))
    
    return calculate_average(averages)      

