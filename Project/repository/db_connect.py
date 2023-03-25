from mongoengine import connect
from dotenv import dotenv_values
import certifi
ca = certifi.where()


"""Settings"""
config = dotenv_values('.env')
username = config['MONGODB_LOGIN']
password = config['MONGODB_PASSWORD']
cluster = config['MONGODB_CLUSTER']
db_name = config['MONGODB_DB_NAME']

"""Підключення за допомогою ODM mongoengine"""
connect(host=f"mongodb+srv://{username}:{password}@{cluster}/{db_name}?authSource=admin&ssl=true", tlsCAFile=ca)
