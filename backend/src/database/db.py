from sqlalchemy import Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

from sqlalchemy.schema import Column

SQLALCHEMY_DB_URL = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"

engine = create_engine(
    SQLALCHEMY_DB_URL,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class BaseModel(Base):
	__abstract__ = True
	__allow_unmapped__ = True

	id = Column(Integer, primary_key=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
