user_input = input("Please enter a number: ")
while not user_input.isdigit():
  user_input = input("\nYou may only enter whole numbers: ")
user_input = int(user_input)

prime_numbers = []

for i in range(1, user_input):
  prime = True
  count = 2
  while count < i:
    if i % count == 0:
      prime = False
      break
    count += 1
  if prime:
    prime_numbers.append(i)
    
    
    




print("\nPrime Numbers")
count = 0
space = 0
previous_num = 0
for i in range(len(prime_numbers)):
  if (previous_num == 0) and (space < 6):
    print(("   " * space) + str(prime_numbers[count]))
    space += 1
  elif (previous_num == 6) and (space > 0):
    print(("   " * space) + str(prime_numbers[count]))
    space -= 1
  elif (previous_num == 0) and (space == 6):
    print(("   " * space) + str(prime_numbers[count]))
    previous_num = 6
    space -= 1
  else:
    print(("   " * space) + str(prime_numbers[count]))
    previous_num = 0
    space += 1
    
  count += 1
print("\n", prime_numbers)
    