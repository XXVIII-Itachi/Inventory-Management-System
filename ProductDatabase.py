from sqlalchemy import Column, String, Numeric, Integer
from sqlalchemy.orm import relationship

from Database import Base


class Stock(Base):
    __tablename__ = "Product Database"

    Product_ID = Column(Integer, primary_key=True, index=True)
    Product_Name = Column(String, unique=True, index=True)
    Description = Column(String)
    Stock = Column(Numeric, default=True)
    Price = Column(Integer, primary_key=True)
    
