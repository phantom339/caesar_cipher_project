#importing modules 
from art import logo
#list of alphabets 
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#creating a function that can encrypt as well as decrypt message:
def caesar(plain_text, shift_amount, cipher_direction):
  changed_text=""
  if cipher_direction=="decode":
    shift_amount*= -1
  for letter in plain_text:
    if letter in alphabet:
      position = alphabet.index(letter)
      new_position = position + shift_amount
      if cipher_direction=="encode":
        if new_position>26:
            while new_position > 52:
              new_position-=26
            new_position-=26  
      else:
         if new_position<0:
           while new_position< -52:
            new_position+=26
           new_position+=26 
      new_letter = alphabet[new_position]
      changed_text += new_letter
    else:
      changed_text+=letter
  print(f"The {cipher_direction}d text is {changed_text}")
 

should_continue=True
while should_continue:
  #taking input to know what the user wants to do:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  #calling the cipher function :
  caesar(plain_text=text, shift_amount=shift, cipher_direction=direction)
  result=input("do you want to continue ciphering : Y/N ").lower()
  if result=="n":
    should_continue=False
    print("Good Bye!")
  
