#Caesar Cipher part1 - Encryption 
#how work out Encode; 
'''
shift = 5
A B C D EFG
         ABCDEFG

'''

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n")
shift = int(input("Type the shift number: \n"))

#create a function called 'encrypt' that takes 'text' and 'shift' as inputs.

  #todo 2; inside the 'encrypt' function, shift each letter of the 'text' **forwards in the alphabet by the shift amount and print the encrypted text. 
  #e.g. 

'''
  plain_text = "victoria"
  shift = 5
  cipher_text = "a"
  print output;"the encoded text is mxxt"

'''


''''
def encrypt(plain_text,shift_amount):
  cipher_text = ""

  for letter in plain_text: 
    print(f"\n{letter}  is plain text of : {plain_text}")

    position = alphabet.index(letter)
    print("position --> ",position)

    new_position = position + shift_amount
    print("New position ----> ",new_position)

    # new_position is 7 and shift_amount is 5 
    new_letter = alphabet[new_position]
    print("new letter value ---> ",new_letter,"\n")

    cipher_text += new_letter
  print(f"The encoded text is {cipher_text}")



encrypt(plain_text = text, shift_amount = shift)

'''



def decrypt(memo, shift_num): 
  cyber_text = ""
  print("def decrypt start from .... \n")

  for letter in memo: 
    print(letter,memo)
    position = alphabet.index(letter)
    new_position = position + shift_num
    new_letter = alphabet[new_position]
    
    
    cyber_text += new_letter
    print(f"cyber_text ---->  {cyber_text}")

decrypt(memo = text, shift_num = shift)

















