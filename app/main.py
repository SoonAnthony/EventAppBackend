from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def Hello_world():
    return {"message": "Hello FastAPI"}
