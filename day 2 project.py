

#what was the total bill? $124.56
#what percentage tip would you like to give? 10,20 or 15? 12 
#how many people to split the bill? 7


print("welcome to the tip calculator!")
bill = float(input("what was the total bill? $"))
tip = int(input("what % tip would you like to give? 10,20 or 15?"))
people = int(input("how many people split to the bill? "))



tip_percentage = tip/100
#print(tip_percentage)
tip_amount = bill * tip_percentage
#print(tip_amount)
total_bill = bill + tip_amount
#print(total_bill)
bill_each_person = total_bill/people
#print(bill_each_person)

final_amount = round(bill_each_person)
#print(final_amount)
# using printing format .format()
final_amount = "{:.2f}".format(bill_each_person)
print(final_amount)
print("the final bill amount is {:.2f}".format(bill_each_person))

print(f"Each person should pay: $ {final_amount}")







 







