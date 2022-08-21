print('-----------------------------------------------------------------')
print('* INSTRUCTIONS')
print('----------------------------------------------------------------')
print("* TO GET BONUS YOUR SERVICE YEAR MUST GREATER THAN 5 YEAR")
print('----------------------------------------------------------------')
user_salary=int(input('* ENTER YOUR SLARY: '))
user_service_year=int(input('* ENTER YOUR SERVICE YEAR: '))
bonus_amount=(5/100)*user_salary
final_amount=bonus_amount+user_salary
if (user_service_year>5):
    print(final_amount)
else:
    print('• Sorry Your Service Year Is Less Than 5 Year')
    print('• Your Do Not Get Any Bonus')
