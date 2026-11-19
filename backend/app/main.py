from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from .database import get_db
from . import models, schemas


app = FastAPI(
    title="Intelligent Cloud Cost Optimisation Tool",
    description="Cloud cost comparison and optimisation API",
    version="1.0.0",
)


# ROOT ENDPOINT
@app.get("/")
def root():
    return {"message": "Cloud Cost Optimisation Tool API is running"}


# GET ALL CLOUD PROVIDERS
@app.get("/providers", response_model=list[schemas.ProviderResponse])
def get_providers(db: Session = Depends(get_db)):

    providers = db.query(models.Provider).all()

    return providers
