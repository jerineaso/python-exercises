print("Welcome to the tip calculator.");

bill_amount = float(input("What was the total bill? $"));

percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "));

people = int(input("How many people to split the bill? "));

total_percentage_bill = ((percentage / 100) * bill_amount) + bill_amount

split_amount = total_percentage_bill / people

final = round(split_amount,2);
print(f"Each person should pay :${final}");
