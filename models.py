# Svg frontend
# MySQL topics in sqlalchemy
# Stored procedures creation in sqlalchemy, alembic vcs
# S3 from python, lambda
# Lambda deployment in s3
# Generated columns, json, indexes and columns aggregation
# How to call lambda, debugging

from sqlalchemy.dialects.mysql import JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine, Boolean, select, insert, Computed

import pymysql

# from sqlalchemy_utils import create_view
from sqlalchemy_json import MutableJson

pymysql.install_as_MySQLdb()

Base = declarative_base(bind=create_engine("mysql://user:password@127.0.0.1:3306/db"))

metadata = Base.metadata


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(60))
    fullname = Column(String(60))
    premium_user = Column(Boolean, default=False)


class Department(Base):
    __tablename__ = "departments"
    id = Column(Integer, primary_key=True)
    name = Column(String(60))
    attributes = Column(JSON)
    employeesCount = Column(Integer, Computed("`attributes` ->> '$.employeesCount'"), index=True)


# defining stored procedure
# maybe to replace it with sa objects
insert_user = """
    BEGIN
	INSERT INTO users(name) values ('Mike');
    END;
"""

# insert to Department table
# insert(Department).values([None, "sales", {"employeesCount": 10}]).execute()


# defining view
premium_members = select([User]).where(User.premium_user == True)

# create_view('premium_users', premium_members, metadata)

# metadata.create_all()

# print(Column(Integer, Computed("id" * 2)))
