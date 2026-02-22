#stage1: basic calculator
number1 = float(input("Enter The first Number: "))
number2 =  float(input("Enter The First Number: "))
operator = input("Enter The Operator(+,-,*,-/): ")
#addition
if operator == "+":
  result = number1+number2
  print ("Result: ", result)
  #subtraction
elif operator == "-":
  result = number1-number2
  print ("Result: ", result)
  #multiplicaton
elif operator == "*":
  result = number1*number2
  print ("Result: ", result)
  #division
elif operator == "/":
  if number2 == 0:
    print("Error: divided by 0 is allowed")
  else:
     result = number1/number2
     print ("Result: ", result)
     
else:
  print("Invalid Operation")
