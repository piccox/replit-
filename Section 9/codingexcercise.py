#a program that converts their scores to grades. 

student_scores = {"Harry" : 81, "Ron": 78,"Hermione":91,"Draco":74,"Neville":62}
print("student scores",student_scores)


student_grades = {}
for student in student_scores: 

  scores = student_scores[student]
  print(scores)
  
  if scores > 90: 
    student_grades[student] = "Outstanding"

  elif scores > 80: 
    student_grades[student] = "Exceeds Expectations"

  elif scores < 80: 
    student_grades[student] = "Acceptable"

  else: 
    student_grades[student] = "Fail"

print(student_grades)
 

 



    
     
