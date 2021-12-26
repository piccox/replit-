#average height rounded to the nearest whole number

#[180,124,165,170,189,169,146]


student_heights = input("input a list of student heights \n").split(',')
#print(student_heights)


for n in range(0,len(student_heights)):
  #print(n, student_heights[n])
  student_heights[n] = int(student_heights[n])
print(f"A list of student_heights: \n{student_heights}")


print("----------------")




#print("total student heights")
total_student_heights = 0

for height in student_heights: 
  total_student_heights += height

  print(f"Total sum of student heights {height}: {total_student_heights}")
print(total_student_heights)




#number of students in the list
number_of_students = 0

for students in student_heights:
  number_of_students += 1

  print(f"Nuber of students in the list {number_of_students} --> {students}")
print(number_of_students)




#print("Average of each student in the list")
average_students_heights = round(total_student_heights/number_of_students)
print(f"Average Heights : {average_students_heights}")
  




