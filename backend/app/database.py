import os
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy import engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base, sessionmaker

# locate  and load the .env file in the backend directory
BACKEND_DIR = Path(__file__).resolve().parents[1]
load_dotenv(BACKEND_DIR / ".env")

# Retrieve database connection parameters from environment variables
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", "5432"))
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# Validate that all required database connection parameters are provided
if not all([DB_NAME, DB_USER, DB_PASSWORD]):
    raise RuntimeError(
        "Database connection parameters are not fully set in the environment variables. Please ensure DB_NAME, DB_USER, and DB_PASSWORD are defined."
    )



# Create a PostgreSQL connection URL using SQLAlchemy's URL object
DATABASE_URL = URL.create(
drivername="postgresql+psycopg",
username=DB_USER,
password=DB_PASSWORD,
host=DB_HOST,
port=DB_PORT,
database=DB_NAME,
)

# Create a SQLAlchemy engine using the constructed database URL
engine = create_engine(
DATABASE_URL,
pool_pre_ping=True,
)

# Create a session factory for database interactions
SessionLocal = sessionmaker(
bind=engine,
autoflush=False,
expire_on_commit=False,
)

# Create a base class for SQLAlchemy models
Base = declarative_base()

# Provide a database session to fastAPI endpoints using dependency injection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()