from fastapi import FastAPI

try:
    from db import db_conn
    from config import EnvConfigSettings

    env = EnvConfigSettings()
    
    db = db_conn.get_db_connection(url=env.mongodb_uri, db_name=env.db_name)

except Exception as e:
    print(f"Error while importing db and config : {e}")
    quit()


app = FastAPI()

@app.get("/")
async def welcome():
    return {
        "welcome to your fastapi project"
    }