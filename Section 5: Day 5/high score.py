#how to find the highest score from a List of scores. 
# 78, 65, 89, 86, 55, 91, 64, 89
student_scores = input("input a list of student score \n").split(',')
#print(student_scores)

for n in range(0, len(student_scores)):
  #print(n, student_scores[n])
  student_scores[n] = int(student_scores[n])
print(student_scores)

print("------\n")
highest_score = 0
for score in student_scores: 
  if score > highest_score:
    highest_score = score
    print("new high score", highest_score)
  else: 
    print(False)
print(f"highest_score is {score}, {highest_score}")









  







