## Input we need from the user
# Total Rent
# Total food ordered for food Snacking
# Electricity units spend
# Charger per unit
# person living in room / flat

## output
#Total amount you have to pay




rent=int(input("Enter the House/Flat rent ="))
food=int(input("Enter the amount of food ordered ="))
electricity=int(input("Enter the  total electricity units spend="))
charger=int(input("Enter the total charger per unit ="))
person=int(input("Enter the number of person living in room / flat ="))

Total_bill= electricity*charger

Output=(rent+food+Total_bill )// person
print("Each person has to pay =", Output)