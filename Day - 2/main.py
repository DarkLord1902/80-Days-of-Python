print("Welcome to the Tip Calculator!")

bill = float(input("What is the total bill amount?:\n$ "))
tip = int(input("How much tip would you like to give?:\nPercent: "))
people = int(input("How many people to split the bill?:\nPeople: "))

total = ("{:.2f}".format((((bill * (tip / 100)) + bill) / people)))

print(f"Each person should pay: $ {total}")