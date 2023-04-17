from models.transaction import Transaction
from models.tag import Tag
from models.merchant import Merchant

from repositories import transaction_repository, tag_repository, merchant_repository

tag_repository.delete_all()
merchant_repository.delete_all()
transaction_repository.delete_all()


merchant_1 = Merchant("Miss Piggy iPlayer")
merchant_repository.save(merchant_1)

merchant_2 = Merchant("Rizzo Gyms")
merchant_repository.save(merchant_2)

merchant_3 = Merchant("Rowlf the Dog's Instruments")
merchant_repository.save(merchant_3)

merchant_4 = Merchant("Scooter Furnishings")
merchant_repository.save(merchant_4)


tag_1 = Tag("Entertainment")
tag_repository.save(tag_1)

tag_2 = Tag("Personal Care")
tag_repository.save(tag_2)

tag_3 = Tag("Shopping")
tag_repository.save(tag_3)



transaction_1 = Transaction(13.99, merchant_1, tag_1)
transaction_repository.save(transaction_1)

transaction_2 = Transaction(22.99, merchant_2, tag_2)
transaction_repository.save(transaction_2)

transaction_3 = Transaction(500.00, merchant_3, tag_3)
transaction_repository.save(transaction_3)

transaction_4 = Transaction(995.00, merchant_4, tag_3)
transaction_repository.save(transaction_4)
