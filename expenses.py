import csv

totals = {}
total_trans = {}
highest_amt = 0
highest_cat = ''
highest_trans = 0
highest_trans_cat = ''

with open("expenses.csv", mode='r') as file:
  reader = csv.DictReader(file)
  for row in reader:
    category = row['category']
    amount = float(row['amount'])
    totals[category] = totals.get(category, 0) + amount
    total_trans[category] = total_trans.get(category, 0) + 1
    if amount > highest_amt:
      highest_amt = amount
      highest_cat = category

for key, value in total_trans.items():
  if value > highest_trans:
    highest_trans = value
    highest_trans_cat = key


print(f"Spend by category: {totals}")
print(f"The highest single expenditure is £{highest_amt:.2f} within the category of {highest_cat}")
print(f"The category with the highest amount of transactions is {highest_trans_cat} with {highest_trans} transactions!")