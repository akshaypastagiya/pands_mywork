# 3.2.4_convert.py
# This program is to enterd the amount in float
# convert this amount in to cent
# Display the amount

amount = float(input('Please enter an amount : '))

amountincent = int(abs(amount * 100))

print("The amount in cent is : {}".format(amountincent))