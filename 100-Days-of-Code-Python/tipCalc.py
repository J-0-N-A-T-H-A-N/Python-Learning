print("Welcome to TipCalc...")

bill = float(input("What is the total bill? €"))
tip_percent = int(input("What percentage of tip to add on? "))
num_people = int(input("How many people are splitting the bill? "))
total_bill = bill + (bill * (tip_percent/100))
per_person = total_bill / num_people

total_bill_f = "{:.2f}".format(total_bill)
per_person_f = "{:.2f}".format(per_person)

print(f"The total bill, including tip, is €{total_bill_f}, each person paying €{per_person_f}")


