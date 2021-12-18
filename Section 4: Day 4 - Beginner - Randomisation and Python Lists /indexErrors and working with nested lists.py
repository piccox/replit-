# Working with Nested Lists 
# 50 states in America 
states_of_america = ["Delaware","Pennsylvania","Alaska","hawaii"]
num_of_states = len(states_of_america)
print(states_of_america[-1])




fruits = ['strawberries', 'apple', 'pear', 'kewii', 'mango', 'melon', 'cherries', 'grapes','Orange' ]
vegetables = ['salad', 'potato', 'onion', 'lemon', 'celery', 'kale']

#nested list; 
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)

print(dirty_dozen[0][1])
print(dirty_dozen[1][1])
print(dirty_dozen[1][-1])
