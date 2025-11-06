# connect database use sql.alchemy

from sqlalchemy import * 
from fastapi import FastAPI
import os
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_USER_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_POST = os.getenv("DB_OORT")
DB_NAME = os.getenv("DB_NAME")

app = FastAPI(title="CRUD APPLICATION ")
DATABASE_URL = "mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)


@app.get("/")
def root():
    return{'Message':'your app is working'}

@app.get("/test-db")
def test_db():
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SHOW DATABASE"))
            return{"status":"error","message":str(e)}
    except Exception as e:
        return {"stauts":f"error{e}"}