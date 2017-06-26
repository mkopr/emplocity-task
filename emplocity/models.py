from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text

from emplocity import database


class FileData(database.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True)
    pages = Column(Integer)
    text = Column(Text)
    characters = Column(Integer)
    words = Column(Integer)
    lines = Column(Integer)

    def __repr__(self):
        return '<Name %r>' % self.name
