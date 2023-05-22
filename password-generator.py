#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# ________________________________________________
# password = ""

# for letter in range(nr_letters):
#   index = random.randint(0,len(letters)-1)
#   password += letters[index]

# for symbol in range(nr_symbols):
#   index = random.randint(0,len(symbols)-1)
#   password += symbols[index]

# for number in range(nr_numbers):
#   index = random.randint(0,len(numbers)-1)
#   password += numbers[index]

# print("Your password is:",password)
# ________________________________________________
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# password_list = []

# for letter in range(nr_letters):
#   password_list.append(random.choice(letters))

# for symbol in range(nr_symbols):
#    password_list += random.choice(symbols)

# for number in range(nr_numbers):
#    password_list += random.choice(numbers)

# random.shuffle(password_list) 

# password = ""
# for i in password_list:
#   password += i

# print("Your password is:",password)

characteres = [letters, symbols, numbers]
total_length = nr_letters + nr_numbers + nr_symbols

contx = 0 #letters
conty = 0 #symbols
contz = 0 #numbers

password = ""
letters_length = len(letters) #length of letters list
symbols_length = len(symbols) #length of symbols list
numbers_length = len(numbers) #length of numbers list

for num in range(total_length):
  characteres_index = random.randint(0,2)
  characteres_list = characteres[characteres_index]
  
#atualiza a quantidade de vezes em que cada índice aparece
#para índice igual a 0
  if characteres_index == 0:
    contx += 1
    if contx < nr_letters:
      password += characteres_list[random.randint(0, letters_length - 1)]
    elif conty < nr_symbols:
      conty += 1
      password += symbols[random.randint(0, symbols_length - 1)]
    else: 
      contz += 1
      password += numbers[random.randint(0, numbers_length - 1)]
#para índice igual a 1
  elif characteres_index == 1:
    conty += 1
    if conty < nr_symbols:
      password += characteres_list[random.randint(0, symbols_length - 1)]
    elif contx < nr_letters:
      contx += 1 
      password += letters[random.randint(0, letters_length - 1)]
    else:  
      contz += 1
      password += numbers[random.randint(0, numbers_length - 1)]
#para índice igual a 2
  elif characteres_index == 2:
    if contz < nr_numbers:  
      contz += 1
      password += characteres_list[random.randint(0, numbers_length - 1)]
    elif contx < nr_letters:
      contx += 1 
      password += letters[random.randint(0, letters_length - 1)]
    else:
      conty += 1
      password += symbols[random.randint(0, symbols_length - 1)]
  else: 
    print("Algo deu errado!")
  
print()
print("Your password is:",password)

