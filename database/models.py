from sqlalchemy.orm import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import Date

Base = declarative_base()

class Sales(Base):

    __tablename__ = "sales"

    id = Column(Integer, primary_key=True)

    order_date = Column(Date)

    product_name = Column(String)

    category = Column(String)

    region = Column(String)

    quantity = Column(Integer)

    unit_price = Column(Float)

    revenue = Column(Float)


class Forecast(Base):

    __tablename__ = "forecast"

    id = Column(Integer, primary_key=True)

    product_name = Column(String)

    actual_sales = Column(Float)

    predicted_sales = Column(Float)