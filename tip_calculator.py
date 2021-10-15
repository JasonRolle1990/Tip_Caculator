# Creating a Tip Calculator
# TODO get amount of bill
# TODO get number of party
# TODO get tip percentage
# TODO add tax to the bill
# TODO total bill tax and tip

# bill*tip
# bill*tax
# bill + tip + tax/ party

##Creating variable for the amount bill
amount_bill = 0.0
##Creating variable for the number party
number_party = 0
##Creating variable for the tip percentage
tip_percentage = 0.0
##Creating variable for the bill tip
bill_tip = 0.0
##Creating variable for the bill tax
bill_tax = 0.0
##Creating variable for the bill total
bill_total = 0.0
##Creating variable for the each separete person own bill
individual_bill = 0.0

#What input will be asked on bill amount, as A Float
amount_bill = float (input('How much is the bill amount'))
#What input will be asked on number of the party, as an Integer
number_party = int (input('How many people are in our party'))
#What input will be asked on tip amount, as A Float
tip_percentage = float (input('How much will the tip percentage be'))

bill_tip = round(amount_bill * (bill_tip/ 100),2)
bill_tax = round(amount_bill * .1,2)
bill_total = round(amount_bill + bill_tip + bill_tax,2) 
individual_bill = round(bill_total / number_party,2)


print(f'the total bill {bill_total}')
print(f'the individual bill {individual_bill}')
