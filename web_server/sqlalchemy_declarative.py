from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Posts(Base):
     __tablename__ = 'posts'
     id = Column(Integer, primary_key=True)
     userId = Column(Integer)
     title = Column(String)
     body = Column(String)

     def __repr__(self):
        return "<Posts(id='%s', title='%s', body='%s')>" % (
                             self.id, self.title, self.body)

class comments(Base):
     __tablename__ = 'comments'
     id = Column(Integer, primary_key=True)
     postId = Column(Integer)
     name = Column(String)
     email = Column(String)
     body = Column(String)

     def __repr__(self):
        return "<comments(id='%s', name='%s', email='%s', body='%s')>" % (
                             self.id, self.name, self.email, self.body)
class albums(Base):
     __tablename__ = 'albums'
     id = Column(Integer, primary_key=True)
     userId = Column(Integer)
     title = Column(String)

     def __repr__(self):
        return "<albums(id='%s', title='%s')>" % (
                             self.id, self.title)
class photos(Base):
     __tablename__ = 'photos'
     id = Column(Integer, primary_key=True)
     albumId = Column(Integer)
     title = Column(String)
     url = Column(String)
     thumbnailUrl = Column(String)

     def __repr__(self):
        return "<photos(id='%s', title='%s', url='%s , thumbnailUrl='%s')>" % (
                             self.id, self.title, self.body, self.thumbnailUrl)
class todos(Base):
     __tablename__ = 'todos'
     id = Column(Integer, primary_key=True)
     userId = Column(Integer)
     title = Column(String)
     completed = Column(String)

     def __repr__(self):
        return "<Posts(id='%s', title='%s', completed='%s')>" % (
                             self.id, self.title, self.completed)

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
from sqlalchemy import create_engine
path_to_db = "mydatabase.db"
engine = create_engine('sqlite:///' + path_to_db)
Base.metadata.create_all(engine)
