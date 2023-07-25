alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#creating a function encrypt:

def encrypt(plain_text, shift_amount):
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    
    if new_position>26:
        while new_position > 52:
          new_position-=26
        new_position-=26  
    new_letter = alphabet[new_position]
    cipher_text += new_letter
  print(f"The encoded text is {cipher_text}")  

#creating a function decrypt:
def decrypt(plain_text, shift_amount):
  decrypted_text=""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position - shift_amount
    
    if new_position<0:
        while new_position< -52:
          new_position+=26
        new_position+=26  
    new_letter=alphabet[new_position]
    decrypted_text+=new_letter      
  print(f"The decoded text is {decrypted_text}")     