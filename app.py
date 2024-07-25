from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World !!!"}

@app.get("/test")
async def test():
    return {"message": "cool !"}

# Supprimez ou commentez le bloc suivant dans votre fichier app.py
#if __name__ == "__main__":
#    uvicorn.run(app, host="localhost", port=8003)