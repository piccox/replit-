# age is str 
age = input("what is your current age?")




#write code ; 
# converting from str to int
# excute the codes of the number remaining; yrs, months, weeks,days 

#current age;
age_as_int = int(age)
print(age_as_int)
#remaining years, if not more than max 100 yrs 
years_remaining = 100 - age_as_int
print(years_remaining)
#remaining days
days_remaing = years_remaining * 365
print(days_remaing)
#remaining weeks 
weeks_remaining = years_remaining  * 52
print(weeks_remaining)
#remaining months
months_remaining = years_remaining * 12 
print(months_remaining)





# using f'string ; 
messege = f"you have {days_remaing} days, {weeks_remaining} weeks, {months_remaining} months, {years_remaining} years"
print(messege)






