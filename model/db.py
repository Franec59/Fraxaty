from mysql.connector import (
    connect,
    errorcode, 
    Error as ConnectorError,
    errors as connector_errors
)
import os
from dotenv import load_dotenv

class DB ():
    """
        Classe de connexion à la DB
    """
  
    def __init__(self, **kwargs):   
        self.loadEnv()
        self.options = {}  
        self.options['host']        = kwargs.get('host', os.getenv('DB_HOST'))
        self.options['user']        = kwargs.get('user', os.getenv('DB_USER'))
        self.options['port']        = kwargs.get('port', os.getenv('DB_PORT'))
        self.options['password']    = kwargs.get('password', os.getenv('DB_PWD'))
        self.options['database']    = kwargs.get('database', os.getenv('DB_NAME'))
        self.options['autocommit']  = kwargs.get('autocommit', bool(int(os.getenv('DB_AUTOCOMMIT'))))
        
        self.connection = self._connect(self.options)

        
    def _connect(self, options) :
        try :
            connection = connect(**options)
            connection.autocommit = bool(options.get("autocommit"))             
        except connector_errors.ProgrammingError as err :
            raise(err)  
        return connection

           
    def getCursor(self, dictionnary=True, buffered=False ):
        try:
            cursor = self.connection.cursor(dictionary=dictionnary, buffered=buffered)
        except ConnectorError as err :
            raise(err)
        return cursor


    def use(self, db_name):
        try:
            cursor = self.getCursor()
            cursor.execute(f"USE {db_name}")
        except ConnectorError as err :
            if err.errno == errorcode.ER_BAD_DB_ERROR:                
                raise(err)    

    
    def query(self, sql):
        cursor = self.getCursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result
           
     
    def info(self):
        if self.connection.is_connected():
            version = self.connection.get_server_info()
            database = self.query("SELECT database() DB")[0].get('DB')
            msg =  f"Vous êtes connecté à MySQL.\n"
            msg += f"Version du serveur: {version} \n"
            msg += f"Aucune DB selectionnée" if database is None else f"Base de donnée actuelle : {database}"
            print(msg)
        else :
            print("Vous n'êtes pas connecté à MySQL")

           
    def loadEnv(self):       
        try:
            if not load_dotenv() :
                raise ValueError("Fichier de configuration de la BD non chargé")                     
        except ValueError as err :
            print("Avertissement : "+ err)
            
            
            