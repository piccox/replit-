# the interpretation of the BMI based on the value.
# under 18.5kg ;  underweight 
# over 18.5kg and below 25kg; normal weight
#over 25kg and below 30kg; overweight
#over 30kg and below 35kg; obese
#above 35kg; clinically obese. 

height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
bmi = float(weight) / int(height) ** 2

if bmi <= 18.5: 
  print(f"your BMI is {bmi}, you are underweight.")

elif bmi > 18.5 and bmi <= 25: 
  print(f"your {bmi}, you are normal weight")

elif bmi > 25 and bmi <= 30: 
  print(f"your BMI is {bmi}, you are overweight.")

else:
  if bmi > 30 and bmi <= 35: 
    print(f"your BMI is {bmi}, you are obese.")
  elif bmi > 35: 
    print(f"your BMI is {bmi}, you are clinically obese.")

  








