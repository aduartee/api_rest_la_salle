# Importa as bibliotecas necessárias
from flask import Flask, request, jsonify
from flask_cors import CORS
import pymongo
from jsonschema import validate, ValidationError as JSONSchemaValidationError

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


question_schema = {
    "type": "object",
    "properties": {
        "title": {"type": "string"},
        "questions": {
            "type": "array",
            "items": {"type": "string"},
            "minItems": 3,
            "maxItems": 3
        },
        "response": {"type": "integer", "minimum": 0, "maximum": 2}
    },
    "required": ["title", "questions", "response"]
}

@app.route('/questions', methods=['GET'])
def get_questions():
    questions = list(collection.find())
    
    for question in questions:
        question['_id'] = str(question['_id'])
        
    return (jsonify(questions), 200)
    
@app.route('/questions', methods=['POST'])
def add_question():
    try:
        question = request.get_json()
        validate(instance=question, schema=question_schema)
    
    except JSONSchemaValidationError as e:
        return jsonify({"error": str(e)}), 400

    result = collection.insert_one(question)
    return jsonify({"id": str(result.inserted_id)}), 201
    

@app.route('/questions/<question_id>', methods=['GET'])
def get_question_by_id(question_id):
    question = collection.find_one({"_id": pymongo.ObjectId(question_id)})
    
    if not question:
        return jsonify({"error": "Not Found this Question in Colletion"}), 404

    question['_id'] = str(question['_id'])
    return jsonify(question), 200

if __name__ == "__Main__":
    app.run()