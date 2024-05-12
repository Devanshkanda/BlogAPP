from pymongo import MongoClient
from pymongo.server_api import ServerApi

def get_db_connection(url: str, db_name: str):
    try:
        print("before connecting to mongodb")

        client = MongoClient(url, server_api=ServerApi('1'))
        
        print("After connecting to mongodb")

        print("Successfully connected to mongodb")

        db = client[db_name]

        return db
    
    except Exception as e:
        print(f"Error Connecting To MongoDB Atlas: {str(e)}")


if __name__ == "__main__":
    get_db_connection()