#Personal Finance Calculator
#Student: Supanut Chueadee
#Date: 24/07/2568
#Purpose: Calculate monthly budget and savings
monthly_income = float(input("User's monthly income in (THB): ")) #รับค่ารายได้ต่อเดือนจากผู้ใช้
rent_cost = float(input("Monthly rent/housing cost: ")) #รับค่าใช้จ่ายสำหรับค่าเช่า
food_budget = int(input("Monthly food budget in (THB): ")) #รับค่าใช้จ่ายสำหรับอาหาร
transportation_cost = float(input("Monthly transportation expenses: ")) #รับค่าใช้จ่ายสำหรับการขนส่ง
entertainment_budget = int(input("Monthly entertainment budget: ")) #รับค่าใช้จ่ายสำหรับความบันเทิง
emergency_fund_percent = float(input("Percentage to save for emergency (e.g., 10.5): ")) #รับเปอร์เซ็นต์สำหรับกองทุนฉุกเฉิน
investment_percent = float(input("Percentage to invest (e.g., 15.0): ")) #รับเปอร์เซ็นต์สำหรับการลงทุน

Total_Fixed_Expenses = rent_cost + transportation_cost #รวมค่าใช้จ่ายคงที่
Total_Variable_Expenses = food_budget + entertainment_budget #รวมค่าใช้จ่ายผันแปร
Total_Expenses = Total_Fixed_Expenses + Total_Variable_Expenses #รวมค่าใช้จ่ายทั้งหมด
Remaining_Income = monthly_income - Total_Expenses #คำนวณรายได้ที่เหลือหลังจากหักค่าใช้จ่ายทั้งหมด
Emergency_Fund_Amount = monthly_income * (emergency_fund_percent / 100) #คำนวณจำนวนเงินสำหรับกองทุนฉุกเฉิน
Investment_Amount = monthly_income * (investment_percent / 100) #คำนวณจำนวนเงินสำหรับการลงทุน
Available_for_Savings = Remaining_Income - Emergency_Fund_Amount - Investment_Amount #คำนวณจำนวนเงินที่สามารถเก็บออมได้

Expense_Ratio = (Total_Expenses / monthly_income ) * 100 #คำนวณอัตราส่วนค่าใช้จ่ายต่อรายได้

print("\n=== MONTHLY BUDGET REPORT ===") #รายงานงบประมาณรายเดือน
print(f"Income: {monthly_income:.2f} THB") #แสดงรายได้
print(f"Fixed Expenses: {Total_Fixed_Expenses:.2f} THB") #แสดงค่าใช้จ่ายคงที่
print(f"Variable Expenses: {Total_Variable_Expenses:.2f} THB") #แสดงค่าใช้จ่ายผันแปร
print(f"Total Expenses: {Total_Expenses:.2f} THB") #แสดงค่าใช้จ่ายทั้งหมด
print(f"Remaining: {Remaining_Income:.2f} THB") #แสดงรายได้ที่เหลือ

print("\n=== SAVINGS BREAKDOWN ===") #แสดงรายละเอียดการออม
print(f"Emergency Fund ({emergency_fund_percent}%): {Emergency_Fund_Amount:.2f} THB") #แสดงจำนวนเงินสำหรับกองทุนฉุกเฉิน
print(f"Investment ({investment_percent}%): {Investment_Amount:.2f} THB") #แสดงจำนวนเงินสำหรับการลงทุน
print(f"Available for Savings: {Available_for_Savings:.2f} THB") #แสดงจำนวนเงินที่สามารถเก็บออมได้

print("\n=== ANALYSIS ===") #วิเคราะห์งบประมาณ
print(f"Expense Ratio: {Expense_Ratio:.2f}%") #แสดงอัตราส่วนค่าใช้จ่ายต่อรายได้ 