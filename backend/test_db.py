# This code check whether fastAPI can sucessfully connects to PostgresSQL or not.

from sqlalchemy import text 
from sqlalchemy.exc import SQLAlchemyError
from app.database import engine


def test_database_connection():
    try:
        # Step 1: Establish a connection with PostgreSQL
        with engine.connect() as connection:

            # Step 2: Execute a simple SQL query
            result = connection.execute(text("SELECT 1"))

            # Step 3: Retrieve the query result
            value = result.scalar_one()

            # Step 4: Verify the result
            if value == 1:
                print("===================================")
                print("DATABASE CONNECTION SUCCESSFUL!")
                print("PostgreSQL is connected to FastAPI.")
                print("Database:", engine.url.database)
                print("===================================")

    except SQLAlchemyError as error:
        print("===================================")
        print("DATABASE CONNECTION FAILED!")
        print("Error:", error)
        print("===================================")


if __name__ == "__main__":
    test_database_connection()
