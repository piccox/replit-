#difficult challenge
# love score <10 or >90, your score is x, go together like coke and mentos
# love score >= 40 and <= 50, your score is y, you are alright together
# otherwise your score is z 
#using .lower()
#count(), calculate for the love score 

print("Welcome to the Love Calculator!")
name1 = input("what is your name? \n")
name2 = input("what is their name? \n")



#combining strings ; name1 + name2
combining_string = name1 + name2 
print(combining_string)

#not use double quotes when printing 
#combining_string2 = "name1" + "name2"
#print(combining_string2)

lower_case_string = combining_string.lower()
print(lower_case_string)

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")
true = t + r + u + e 
print(true)

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")
love = l + o + v + e
print(love)

#combing love_score & convert love score,str,into int()
love_score = int(str(true) + str(love))
print(f"love_score: {love_score}")


x = "coke and mentos"
y = "alright together"

if (love_score < 10) or (love_score >90):
  print(f"your score is{love}, you go together {x} ")

elif(love_score >= 40) and (love_score <= 50):
  print(f"your score is {love_score}, you go {y} ")

else:
  print(f"your score is {love_score} ")












