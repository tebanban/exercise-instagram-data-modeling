import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    Nickname = Column(String(15))
    Correo = Column(String(30))
    Telefono = Column(Integer)
    Sexo = Column(Integer)
    Estado_Cuenta = Column(Integer, ForeignKey('Login.Estado_Cuenta'))
    Nombre_Usuario = Column(Integer, ForeignKey('Login.Nombre_Usuario'))
    Primer_Apellido = Column(Integer, ForeignKey('Login.Primer_Apellido'))
    Segundo_Apellido = Column(Integer, ForeignKey('Login.Segundo_Apellido'))
    Password = Column(Integer, ForeignKey('Login.Password'))
    Confirmacion_Password = Column(Integer, ForeignKey('Login.Confirmacion_Password'))
    

class Like(Base):
    __tablename__ = 'like'
    id = Column(Integer, primary_key=True)

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')