"""
Question 2: Currency Converter (20 points)

Write a program that converts between Thai Baht (THB) and US Dollars (USD).
Requirements:

Ask user to choose conversion direction (THB to USD or USD to THB)
Ask for the amount to convert
Use exchange rate: 1 USD = 35.5 THB
Display result with 2 decimal places
Show the calculation formula used
"""

question = input("Direction 1 = THB to USD or 2 = USD to THB: ")
amount = float(input("Amount: "))

if question == "1" :
    print(f"{amount} THB = {amount / 35.5} USD")

else :
    print(f"{amount} USD = {amount * 35.5} THB")