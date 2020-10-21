# Svg frontend
# MySQL topics in sqlalchemy
# Stored procedures creation in sqlalchemy, alembic vcs
# S3 from python, lambda
# Lambda deployment in s3
# Generated columns, json, indexes and columns aggregation
# How to call lambda, debugging

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
import alembic

import pymysql

from sqlalchemy import Table, MetaData
from sqlalchemy.sql import text
from sqlalchemy_views import CreateView, DropView

pymysql.install_as_MySQLdb()

Base = declarative_base(bind=create_engine("mysql://user:password@127.0.0.1:3306/db"))


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(60))


view = Table('products_view', Base.metadata)
definition = text("SELECT name FROM products")
create_view = CreateView(view, definition, or_replace=True)
# print(str(create_view.compile()).strip())

Base.metadata.create_all()
