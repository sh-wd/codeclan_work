from modules.bank_account import *

account = {
    "holder_name" : "John",
    "balance":500,
    "type": "business"
}

# print(get_account_name(account))


bank_account1 = BankAccount('John', 500, 'business')
bank_account2 = BankAccount('Steve', -800, 'personal')

# print(bank_account1.balance)
# bank_account1.balance = 600
# print(bank_account1.balance)

# bank_account1.holder_name = "Deirdre"
# print(bank_account1.holder_name)

# bank_account1.pay_in(100)
# print(bank_account1.balance)

bank_account1.pay_monthly_fee()
print(bank_account1.balance)