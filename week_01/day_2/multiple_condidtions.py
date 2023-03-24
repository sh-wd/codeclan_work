has_sufficient_funds = True
account_active = False

if has_sufficient_funds and account_active:
    print("Tx approved")

if has_sufficient_funds or account_active:
    print("At least one thing was true")