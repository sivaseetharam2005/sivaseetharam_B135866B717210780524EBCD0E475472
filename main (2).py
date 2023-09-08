num = int(input("Enter a number"))
fact = 1
if num < 0:
  print("Negative")
elif num == 0:
  print("The factorial of a given number is 0")
else:
  for i in range(1, num + 1):
    fact = fact * i
  print(fact)
