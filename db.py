from pymongo import MongoClient

# 172.20.144.1 because of WSL, you can change to "localhost"
client = MongoClient('172.20.144.1', 27017)
