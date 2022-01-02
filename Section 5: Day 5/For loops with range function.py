#for Loop 
# sometimes using lists completely 
#add up ; 1+2+3+... 100 
# 100 + 99 + 98 + ...1
#range() function 
#for loop with Range: numbers inside range --> 
#for number in range(a,b):

for number in range(1,11,3):
  print(number)


total = 0
for number in range(1,101):
  total += number
print(f"add up the total numbers {number} --> {total}")

