from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    date = Column(Date)
    products = relationship("Product", back_populates="order")

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    order_id = Column(Integer, ForeignKey('orders.id'))
    order = relationship("Order", back_populates="products")