import pymongo

MONGO_CONNECTION_STRING = 'mongodb://10.109.2.63:443/'
MONGO_DATABASE_NAME = 'erickGabrielVictor'

class SalaDeAulaRepository:
    def __init__(self, db):
        self.db = db
        self.collection = db['salas_de_aula']  # Nome da coleção

    def criar_sala_de_aula(self, dados):
        result = self.collection.insert_one(dados)
        return result.inserted_id

def get_database_client():
    client = pymongo.MongoClient(MONGO_CONNECTION_STRING)
    return client[MONGO_DATABASE_NAME]
