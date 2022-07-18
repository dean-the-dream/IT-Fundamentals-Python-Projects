fibonacci = list()
for i in list(range(10)):
  if len(fibonacci) < 2:
    fibonacci.append(1)
  else:
    fibonacci.append(fibonacci[ - 2] + fibonacci[i - 1])

print(f"Fibonacci Sequence = {fibonacci}")
