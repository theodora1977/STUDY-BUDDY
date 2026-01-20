from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

# Create a test database file
DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL)
Base = declarative_base()

# Create all tables (this will create the test.db file)
Base.metadata.create_all(bind=engine)

print("Test database created successfully!")
print("Database file: test.db")