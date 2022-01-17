#reorganising the code
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encypt, Type 'decode' to decrypt \n")
text = input("Type your message \n").lower()
shift = int(input("Type the shift amount : \n"))


def caesar(start_text, shift_amount, direction_text):
  end_text = ""

  if direction_text == "decode": 
    #shift_amount *= -1
    shift_amount = shift_amount * -1
  
  for letter in start_text: 
    position = alphabet.index(letter)
    new_position = position + shift_amount
    end_text += alphabet[new_position]
    print(f"position --> {position}, new position ----> {new_position}, end text -------> {end_text}")
  print(f"the final end text is {end_text}")

caesar(start_text=text, shift_amount=shift, direction_text = direction)
