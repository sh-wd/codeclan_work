from models.user import User
from models.transaction import Transaction
from models.tag import Tag
from models.merchant import Merchant

from repositories import user_repsository
from repositories import transaction_repository
from repositories import tag_repository
from repositories import merchant_repository

tag_repository.delete_all()
merchant_repository.delete_all()
transaction_repository.delete_all()

user_1 = User("Kermit the Frog")
user_repsository.save(user_1)

transaction_1 = Transaction(13.99, user_1)