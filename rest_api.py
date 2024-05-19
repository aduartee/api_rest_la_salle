# Importa as bibliotecas necessárias
from flask import Flask
from flask import request, jsonify
from flask_cors import CORS
import pymongo

# Conexão com o MongoDB usando pymongo
# myclientName é uma instância do cliente MongoDB, conectando-se ao servidor MongoDB rodando em localhost na porta 27017
myclientName = pymongo.MongoClient("mongodb://admin:password@localhost:27017")

# Seleciona o banco de dados 'laSalleDb' do cliente MongoDB
dbClient = myclientName['laSalleDb']

# Seleciona a coleção 'collection' dentro do banco de dados 'laSalleDb'
collection = dbClient['collection']

# Cria a instância do Flask
app = Flask(__name__)

# Habilita Cross-Origin Resource Sharing 
# Isso permiite que os recursos da API sejam acessados por páginas web de diferentes domínios
cors = CORS(app)

# Configura o cabeçalho de CORS
app.config["CORS_HEADERS"] = "Content-type"

@app.route('/Push', methods=['Post', 'GET'])
def Push():
    content = request.get_json()
    collection.insert_one(content) 
    
@app.route('/Update', methods=['Post', 'GET'])
def Update():
    content = request.get_json()
    collection.insert_one(content) 
    
@app.route('/Delete', methods=['Post', 'GET'])
def Delete():
    content = request.get_json()
    collection.insert_one(content) 
    
@app.route('/Pulling', methods=['Post', 'GET'])
def Pulling():
    content = request.get_json()
    collection.insert_one(content) 
    
if __name__ == "__Main__":
    app.run()