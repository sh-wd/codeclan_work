customer = {
    "first_name": "Huckelberry",
    "last_name": "Finn",
    "order_description": "Happy Meal",
    "order_no": 23
}

def change_customer_order():
    customer["order_description"] = "Super Size Happy Meal"

change_customer_order()
print(customer)