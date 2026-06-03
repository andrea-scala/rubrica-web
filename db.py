import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection(config=None):
    """
    Questa funzione esegue la connessione al database utilizzando, come parametri, quelli ottenuti da file config se esiste altrimenti da env vars.
    """
    
    if config:
        host     = config.get('DB_HOST', os.getenv('DB_HOST'))
        port     = int(config.get('DB_PORT', os.getenv('DB_PORT')))
        database = config.get('DB_NAME', os.getenv('DB_NAME'))
        user     = config.get('DB_USER', os.getenv('DB_USER'))
        password = config.get('DB_PASSWORD', os.getenv('DB_PASSWORD'))
    else:
        host     = os.getenv('DB_HOST')
        port     = int(os.getenv('DB_PORT'))
        database = os.getenv('DB_NAME')
        user     = os.getenv('DB_USER')
        password = os.getenv('DB_PASSWORD')

    return mysql.connector.connect(
        host=host,
        port=port,
        database=database,
        user=user,
        password=password
    )
