print ("Let's determine your risk of dying from Corona Virus.", end="\n\n")
print ("Please answer the following questions by typing yes or no", end="\n\n")


age = input("Are you a cigarette addict older than 75 years old?:  ")

while (age != "yes") and (age != "no"):
  print("You must answer by typing 'yes' or 'no'.", end="\n\n")
  age = input("Are you a cigarette addict older than 75 years old?:  ")

chronic = input("Do you have a severe chronic disease?:  ")

while (chronic != "yes") and (chronic != "no"):
  print("You must answer by typing 'yes' or 'no'.", end="\n\n")
  chronic = input("Do you have a severe chronic disease?:  ")

immune = input("Is your immune system too weak?  ")

while (immune != "yes") and (immune != "no"):
  print("You must answer by typing 'yes' or 'no'.", end="\n\n")
  immune = input("Is your immune system too weak?  ")


risk = [age, chronic, immune]
# questions = ("Are you a cigarette addict older than 75 years old?:  ", "Do you have a severe chronic disease?:  ", "Is your immune system too weak?  ")


for i in range(3):
  if risk[i] == "yes":
    risk[i] = True
  else:
    risk[i] = False

if risk.count(True) > 1:
  print("\n You are in risky group!")
else:
  print("\n You are not in risky group!")