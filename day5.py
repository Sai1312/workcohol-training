from module.bill import bill_amount

amount = int(input("Enter amount: "))
print("Bill amount: ", bill_amount(amount))


import pandas as pd

dt = pd.DataFrame(['a', 'b', 'c', 'd'])
print(dt)