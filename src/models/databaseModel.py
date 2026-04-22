import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

class Database:
    @staticmethod
    def get_connection():
        return mysql.connector.connect(
            host=os.getenv("localhost"),
            user=os.getenv("root"),
            password=os.getenv(""),
            database=os.getenv("tareas")
        )