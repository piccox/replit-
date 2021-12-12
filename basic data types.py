# Data Types: s
### tring, int, float, booleans

# Strings
"Hello"[0]
"world"[1]
"hello world"[2]

# concatinate;
print("123" + "World")

#integer;
12345

# Float ;
3.14159

# Booean ; True or False
True
False



#Coding excercise ;

two_digit_number = input("type a two digit ")
print(type(two_digit_number))



first_digit = (two_digit_number[0])
#print("[",first_digit,"]")
print(first_digit)

second_digit = (two_digit_number[1])
print(second_digit)
#print("[",second_digit,"]")
# a number eight concatinated to the seven  
#result = first_digit + second_digit
#print(result)





#Data Type conversion; string to int -- meaning will be changed 

first_digit = int(two_digit_number[0])
print(first_digit)

second_digit = int(two_digit_number[1])
print(second_digit)

result = int(first_digit) + int(second_digit)
print(result)
print(type(result))

