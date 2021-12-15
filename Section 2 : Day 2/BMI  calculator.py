# BMI calsulate:  
## Formula ---> BMI = kg / m**2
### Body Mass Index is a simple calculation using a person's heigh & weight. 




#Given an example;
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
print(type(height))
print(type(weight))


# write code; 
# height and weight are str; converting from str to int 
bmi = int(weight) / int(height) ** 2
print(bmi)

# to print BMI as a whole number ; 
bmi_as_int = int(bmi)
print(bmi_as_int)
















