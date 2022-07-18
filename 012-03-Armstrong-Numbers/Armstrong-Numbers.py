user_number = input("""Is your number an armstrong number???\nLet's find out!\nEnter your number!\n
Please only enter whole numbers:   """)
num_list = list(range(10)) #this list will be used to check each character of user_input to make sure it's only number
contains_char = False #this will become true if somthing other than an int is located in the user input
match = False #this will become true when there is a match between 1 character from the user input and 1 number in num_list


#the following loop goes through each character of the user input and checks it against the digits 0-9
for i in user_number: #check each character in the user input
  match = False  #assume the user entered an invalid character
  for numlist_counter in num_list: #compare the character with 0-9
    if i == str(num_list[numlist_counter]): #if a match is found stop checking the numbers
      match = True
      break
  if match == False: #if there was no match after checking 0-9 then stop checking
    contains_char = True
    break
  
    

if contains_char:
  print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
else:
  print("Thank you for entering a whole number!\n")
  exponent = len(user_number)
  digits = list(user_number)
  num_product = 0
  counter = 0 
  for i in user_number:
    num_product = num_product + int(digits[counter])**exponent
    counter += 1
  if str(num_product) == user_number:
    print(f"{user_number} is an Armstrong Number!")
  else:
    print(f"{user_number} is not an Armstrong Number")