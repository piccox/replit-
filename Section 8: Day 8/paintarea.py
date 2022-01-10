#instructions: painting a wall. 
'''
> 1 can of paint can cover 5 square meters of wall
> random height
> random width of wall 
  - calculate how many cans of paint you'll need to buy 

e.g. number of cans = (height x width) /coverage per can 

e.g. 
height = 2
width = 4
coverage = 5
number of cans = (2x4)/5 = 1.6cans 

'''

# using keyword arguments
import math

def paint_calc(height,width,cover):
  area = height * width
  number_of_cans = math.ceil(area/cover)
  print(f"You'll need {number_of_cans:.2f } cans of paint.")

wall_height = int(input("Height of wall : "))
wall_width = int(input("Width of wall: "))
coverage = 5
paint_calc(height=wall_height,width = wall_width,cover=coverage)


