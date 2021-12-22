#how to find the highest score from a List of scores. 
# [78, 65, 89, 86, 55, 91, 64, 89]


student_scores = input("input a list of student score \n").split(',')

print(student_scores)
print(type(student_scores))




for n in range(0, len(student_scores)):
  #print(n, student_scores[n])
  student_scores[n] = int(student_scores[n])

print(student_scores)
#print(min(student_scores))
#print(max(student_scores))



print("Start loop")

# hightest scores
highest_score = 0

for scores in student_scores:
  print("Current score : ", scores)
  if scores > highest_score: 
    print(scores, ">", highest_score)
    highest_score = scores
    print("now high score is ", highest_score)
  else:
    print("False")

print(f"The highest score in the class is : {highest_score}")





  







