from pymongo import MongoClient

connection_string = "mongodb://admin:password@localhost:27017/?authSource=admin"
client = MongoClient(connection_string)
db_conection = client["laSalleDb"]

collection = db_conection.get_collection("colletion")

search_filter = {
    "teste": "Arthur"
}

response = collection.find(search_filter)

for indice in response:
    print(indice)