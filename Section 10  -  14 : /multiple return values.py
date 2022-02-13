# more than one return statements 

def format_name(first_name, last_name): 
  # two inputs 
  # convert to string to title() case in python 
  if first_name == "" or last_name == "":
    return
    # using early return without anything afterwards, this is going to escape the function so as to termination the function early

  formated_first_name = first_name.title()
  formated_last_name = last_name.title()
  return f"{formated_first_name} {formated_last_name}" 

print(format_name(input("what is your first name?"),(input("What is your last name?"))))




