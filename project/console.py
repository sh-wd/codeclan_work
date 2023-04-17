from models.user import User
from models.transaction import Transaction
from models.tag import Tag
from models.merchant import Merchant

from repositories import user_repository
from repositories import transaction_repository
from repositories import tag_repository
from repositories import merchant_repository

tag_repository.delete_all()
merchant_repository.delete_all()
transaction_repository.delete_all()

user_1 = User("Kermit the Frog")
user_repository.save(user_1)


transaction_1 = Transaction(13.99, user_1)
transaction_repository.save(transaction_1)

transaction_2 = Transaction(22.99, user_1)
transaction_repository.save(transaction_2)

transaction_3 = Transaction(500.00, user_1)
transaction_repository.save(transaction_3)

transaction_4 = Transaction(995.00, user_1)
transaction_repository.save(transaction_4)


merchant_1 = Merchant("Miss Piggy iPlayer", transaction_1)
merchant_repository.save(merchant_1)

merchant_2 = Merchant("Rizzo Gyms", transaction_2)
merchant_repository.save(merchant_2)

merchant_3 = Merchant("Rowlf the Dog's Instruments", transaction_3)
merchant_repository.save(merchant_3)

merchant_4 = Merchant("Scooter Furnishings", transaction_4)
merchant_repository.save(merchant_4)


tag_1 = Tag("Entertainment", transaction_1)
tag_repository.save(tag_1)

tag_2 = Tag("Personal Care", transaction_2)
tag_repository.save(tag_2)

tag_3 = Tag("Shopping", transaction_3)
tag_repository.save(tag_3)

tag_4 = Tag("Shopping", transaction_4)
tag_repository.save(tag_4)