alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


#Todo 2: what if the user enters a shift that is greater than the number of letters in the alphabet? 
#try running the program and entering a shift number of 45.
#hHint: Think about how you can use the modulus(%). 


def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""

  if cipher_direction == "decode": 
    #shift_amount *= -1
    shift_amount = shift_amount * -1

    #todo 3 - what happens if the user enters a number/symbol/space?
    #can you fix the code to keep the number/symbol/space when the text is encoded/decoded? 
  
  for char in start_text: 
    if char in alphabet: 
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
      print(f"position --> {position}, new position ----> {new_position}, end text -------> {end_text}")
    else:
      end_text += char
  print(f"here is the cipher direction  {cipher_direction} this is an end text: {end_text }")


#Todo1 : import and print the logo from art.py when the program starts. 

from art import logo 
print(logo)

#Todo 4 : can you figure out a way ask the user if they want to restart the cipher program? e.g. type 'yes' then ask them for the direction/text/shift again and call the caesar() function again? 
#hint: try creating a while loop that continues to execute the program if the user types 'yes'

should_end = False
while not should_end:

  direction = input("Type 'encode' to encypt, Type 'decode' to decrypt \n")
  text = input("Type your message \n").lower()
  shift = int(input("Type the shift amount : \n"))
  shift = shift % 26

#Todo 2 - what if the user enters a shift that is > greater than the number of letters in the alphabet (26)? 
# try running the program and entering a shift number of 45. and Add some code so that the program continues to work even if the user enters a shift number greater than 26.
#hint: think about how you can use the modulus (%). 
  

  caesar(start_text=text, shift_amount=shift,cipher_direction=direction)

  restart = input("type 'yes' if you want to go again. otherwise type 'no'.\n")
  if restart == "no":
    should_end = True
    print("Goodbye")