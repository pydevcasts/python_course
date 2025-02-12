import sqlite3

con = sqlite3.connect("sqlite.db")
# con.execute("""
# CREATE TABLE person (id, name, family, age);
# """)

# con.execute("""
# INSERT INTO person (id, name, family, age) VALUES (3, "siyamak", "abs", "20");
# """)
# con.commit()

result = con.execute("""
SELECT * FROM person WHERE id = 2;
""")

# for i in result:
#     print(i)
x = result.fetchall()
print(x)

#############################################################

import sqlalchemy
from sqlalchemy import String, Column, Integer,create_engine, or_,and_,text
from sqlalchemy.orm import sessionmaker, session, aliased
from sqlalchemy.ext.declarative import declarative_base

db = "sqlite:///file.db"
engine = create_engine(db, echo = True)
Base = declarative_base()
Session = sessionmaker(bind = engine)
session = Session()

class User(Base):
  __tablename__ = "users"
  id = Column(Integer, primary_key = True)
  name = Column(String)
  fullname = Column(String)
  password = Column(String)

  def __init__(self,name, fullname, password, *args, **kwargs):
    self.name = name
    self.fullname = fullname
    self.password = password
  
  def __repr__(self):
    return "f<User({self.name} -{self.fullname} - {self.password})>"

Base.metadata.create_all(engine)
fake = User("ariyana", "mohamadi",123456789)
# session.add(fake)
# session.commit()
# users = session.query(User).filter(User.fullname=="abasi").order_by(User.name)[1:3]
# users = session.query(User).from_statement(text(r"SELECT * FROM users WHERE password=:password").params(password=123456789)).all()
for i in users:
  print(i.name)
# =========================================================
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine


# Create an engine instance
engine = create_engine('sqlite:///example.db', echo=True)  # echo=True will log all the SQL queries
# Create a session
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'  # Name of the table

    id = Column(Integer, primary_key=True)  # Primary key
    name = Column(String)  # Name column
    age = Column(Integer)  # Age column

    def __repr__(self):
        return f"<User(name={self.name}, age={self.age})>"
# Create a new user
new_user = User(name='Alice', age=30)
session.add(new_user)
session.commit()  # Commit the transaction

# Read users
users = session.query(User).all()  # Get all users
print(users)

# Update a user
user_to_update = session.query(User).filter_by(name='Alice').first()
if user_to_update:
    user_to_update.age = 31
    session.commit()  # Commit the transaction

# Delete a user
user_to_delete = session.query(User).filter_by(name='Alice').first()
if user_to_delete:
    session.delete(user_to_delete)
    session.commit()  # Commit the transaction

# Close the session
session.close()
