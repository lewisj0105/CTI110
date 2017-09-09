# CTl-110
# M2HW2 - Tip Tax Total
# Johnny Lewis
# 9/3/2017

foodCost = float(input(" Enter the charge for the food: "))
tipAmount = foodCost * .18
salesTax = foodCost * .07
totalCost = foodCost + tipAmount + salesTax
# display resultsd 
print(" Food Cost is: ", format(foodCost,".2f"))
print(" Tip Amount is: ", format(tipAmount,".2f"))
print(" Sales Tax is: ", format(salesTax,".2f"))
print(" Total Cost is: ", format(totalCost,".2f"))
