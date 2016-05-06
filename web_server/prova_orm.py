from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_declarative import Posts, comments, albums, photos, todos, Base

path_to_db = "mydatabase.db"
engine = create_engine('sqlite:///' + path_to_db)
Base.metadata.create_all(engine)

DBSession = sessionmaker(bind = engine)
session = DBSession()

#searching users
user = session.query(Posts).all()
list_of_lists=[]
for row in user:
    list_of_lists.append((row.id,row.title,row.body))

print list_of_lists

user = session.query(comments).all()
list_of_lists=[]
for row in user:
    list_of_lists.append((row.id,row.name,row.email))

print list_of_lists
