from sqlalchemy import Column, String, Integer,VARCHAR,Text

from base import Base


class Article(Base):
    __tablename__ = 'articles'

    id = Column(VARCHAR(32), primary_key=True)
    body = Column(Text)
    title = Column(Text)
    newspaper_uid = Column(Text)
    host = Column(Text)
    n_tokens_title = Column(Integer)    
    n_tokens_body = Column(Integer)    
    url = Column(Text)

    def __init__(self, uid, body,title, newspaper_uid, host, n_tokens_title, n_tokens_body, url):
        self.id = uid
        self.body = body
        self.title = title
        self.newspaper_uid = newspaper_uid
        self.host = host    
        self.n_tokens_title = n_tokens_title
        self.n_tokens_body = n_tokens_body
        self.url = url

