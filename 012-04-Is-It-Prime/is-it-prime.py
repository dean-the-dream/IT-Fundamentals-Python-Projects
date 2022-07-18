while True:
  user_choice = input("Enter a number to see if it's prime: ")
  if (user_choice == "Q") or (user_choice == "q"):
    print("Goodbye!")
    break
  else:
    if not (user_choice.isdigit() and (int(user_choice) > 1)):  # the user's choice 1) must be an integer 2) must be greater than negative one.
      print("Only integers greater than one are allowed.\n")
    else:
      user_choice = int(user_choice)
      prime = "is"
      count = 2
      while count < user_choice:
        if user_choice % count == 0:
          prime = "is not"
          break
        count += 1
      print(user_choice, prime, "a prime number.\n")
      print("Type 'Q' to quit.")