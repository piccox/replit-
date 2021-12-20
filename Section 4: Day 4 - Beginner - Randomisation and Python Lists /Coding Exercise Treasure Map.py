row1 = ["* ", "😆", "😆"]
row2 = ["🤓", "🤓", "🤓"]
row3 = ["🤔", "X ", "🤔"]

#nested lists inside a list 
map = [row1, row2, row3]
#print(map)
print(f"{row1} \n{row2} \n{row3}")

position = (input("where do you wanto to put the treasure? \n"))

# colum : 2
# row ; 3
horizontal = int(position[0]) #2
vertical = int(position[1]) #3
#horizontal = position[0]
#vertical = position[1]


print("0",map[0])
print("1",map[1])
print("2",map[2],"\n next line")

#print("2",map[2])
#print("h",map[horizontal -1])
#print("v",map[vertical - 1])


#print("answer", map[vertical-1][horizontal-1])
map[vertical-1][horizontal-1] = "SS"
print(map[vertical-1][horizontal-1])




#selected_row = map[horizontal - 1]
#selected_row[horizontal - 1] = "X"

