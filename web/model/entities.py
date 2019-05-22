from sqlalchemy import Column, Integer, String, Sequence, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import connector

class User(connector.Manager.Base):
    __tablename__ = 'users'
    codigo = Column(Integer, Sequence('users_id_seq'), primary_key=True)
    nombre = Column(String(13))
    apellido = Column(String(13))
    password = Column(String(16))
