from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Cloud Cost Optimisation Tool API is running"}