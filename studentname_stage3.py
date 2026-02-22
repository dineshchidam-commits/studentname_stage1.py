#Stage3
name = input("Enter Student Name: ")
mark1=float(input("Enter Mark1: "))
mark2=float(input("Enter Mark2: "))
mark3=float(input("Enter Mark3: "))

total = mark1+mark2+mark3
percentage = (total/300)*100

#GRADE CALCUKATION
if percentage >= 70:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "F"

print("\n-----Result-----")
print(name)
print ("Total: ", total, "/300")
print ("Percentage: ", percentage, "%")
print ("Grade: ", grade)
