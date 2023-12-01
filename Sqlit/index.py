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
    # with engine.connect() as connection:
    #   connection.execute(text(f"CREATE TABLE {self.__tablename__} (id INTEGER, name VARCHAR(20), password VARCHAR(30))"))
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

