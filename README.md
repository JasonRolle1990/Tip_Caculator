<h1><b><div align="center">~~Tip_Caculator_Repo~~</div></b></h1>

![alt text](calc_pic.jpg)

## Summary


  I created a tip calculator that would basically consist of the number of people, the amount of the bill, the tip percentage, and the tax.
 By creating variables for each of these, I made inputs that would ask the user, in the terminal, the neccassary questions they would need to answer to get the solutions in order to complete their dinner bill, using provided information. I also commented out my work, to explain what im doing. I made sure integers and floats were rounded to the second decimal for each tip calculator mathimatical equation. I  made the proper print statements as formatted strings.
 Also made sure the individual outcomes would be rounded to the 100th. The result shows a formatted version the tip, tax, and individual amounts in the terminal. You can run the tip calculator by typing python tip_calculator.py and answering the prompts.









[Tip_Calculator](https://www.calculatorsoup.com/calculators/financial/tip-calculator.php)


```
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
# Rounding the calculation the amount bill multiplied by the tip percentage, rounded to the second decimal
bill_tip = round(amount_bill * (tip_percentage/ 100),2)
# Rounding the bill tax times 10%, ot the second decimal
bill_tax = round(amount_bill * .1,2)
#the bill total rounded to the second decimal, (amount bill, bill tip, bill tax is added)
bill_total = round(amount_bill + bill_tip + bill_tax,2) 
#the bill total by number party is the individual bill rounded to the second decimal
individual_bill = round(bill_total / number_party,2)
#print statement for the bill tip which is a float ..displayed to second decimal place(formated string)
print(f'the tip is {bill_tip:,.2f}')
#print statement of total bill, which is a float. Displayed to the second decimal place(formated string)
print(f'the total bill {bill_total:,.2f}')
#print statement of the individual bill, which is a float. Displayed to the second decimal place (formated string)
print(f'the individual bill {individual_bill:,.2f}')
#print statement of the bill tax, which is a float. Displayed to the second deciamal place (formated string)
print(f'bill tax {bill_tax:,.2f}')
```
