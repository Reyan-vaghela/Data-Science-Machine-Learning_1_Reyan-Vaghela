import numpy as np

student_dtype = np.dtype([
    ('name', 'S17'),  
    ('age', 'i4'),    
    ('grade', 'f4')   
])

students = np.array([
    (b'joseph', 21, 78.5),    
    (b'shivam', 22, 95.2),     
    (b'reyan', 20, 89.1)  
], dtype=student_dtype)

print("Student Records Array:")
print(students)

print("\nRange Find:")
print("Names:", students['name'])  
print("Ages:", students['age'])    
print("Grades:", students['grade']) 

print("\nFirst Student Record:")
first_student = students[0]  
print("Name:", first_student['name'].decode('utf-8'))  
print("Age:", first_student['age'])                    
print("Grade:", first_student['grade'])                


