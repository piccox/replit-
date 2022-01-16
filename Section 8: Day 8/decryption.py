# how to work out Decode; 
'''
e.g. shift = 3 
this works backward and shift backward in the alphabet in order 
  
      ABCDEFG
A B C DEFG

'''

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n")
shift = int(input("Type the shift number: \n"))

#create a function called 'encrypt' that takes 'text' and 'shift' as inputs.

  #todo 2; inside the 'encrypt' function, shift each letter of the 'text' **bacwards in the alphabet by the shift amount and print the encrypted text. 
  #e.g. 

'''
  plain_text = "victoria"
  shift = 5
  cipher_text = "mxxt"
  print output;"the encoded text is mxxt"

'''
def encrypt(plain_text, shift_amount): 
  cipher_text = ""

  for letter in plain_text: 
    print(letter,plain_text)

    position = alphabet.index(letter)
    new_position = position + shift_amount
    cipher_text += alphabet[new_position]
  print(f"cyber_text ---->  {cipher_text}")


def decrypt(cipher_text,shift_amount):
  plain_text = ""
    
  for letter in cipher_text: 
    print(f"this is {letter},{cipher_text}")

    position = alphabet.index(letter)
    print("here is position",position)
    #subtract from position to shift_amount
    new_position = position - shift_amount
    print("new position",new_position)
    
    plain_text += alphabet[new_position]
  print(f"The decoded text is {plain_text}")  
    #plain_text += new_letter
  #print(f"The decoded text is {plain_text}")

#Todo 3; check if the user wanted to encrypt or decrypt the message by checkin gthe 'direction' variable. then call the correct function based on the 'direction' variable. you shoud be able to test the code to encrypt *AND* decrypt a message.

#check direction variable 
if direction == "encode":
  encrypt(plain_text = text, shift_amount = shift)

elif direction =="decode":
  decrypt(cipher_text = text, shift_amount = shift)

#decrypt(cipher_text = text, shift_amount = shift)
