
payment = int(input("Enter your payment: "))
rate = float(input("Enter your rate: "))
numberOfMonths = 12
time = int(input("Enter your years of payment: "))
result = (payment*(rate/numberOfMonths)) / (1-(1+rate/numberOfMonths)**(-numberOfMonths*time))

paymentLeft = payment - result

print(f"Your monthly payment is: {int(result)}")
print(f"You have left to pay: {int(paymentLeft)}")