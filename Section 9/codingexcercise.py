#a program that converts their scores to grades. 

student_scores = {"Harry" : 81, "Ron": 78,"Hermione":91,"Draco":74,"Neville":62}

student_grades = {}
for student in student_scores: 
  print("scores --> ",student_scores,'\n')
  
  scores = student_scores[student]
  if scores > 90: 
    student_grades[student] = "Outstanding"

  elif scores > 80: 
    student_grades[student] = "Exceeds Expectations"

  elif scores < 80: 
    student_grades[student] = "Acceptable"

  else: 
    student_grades[student] = "Fail"
print(student_grades)
    
     
