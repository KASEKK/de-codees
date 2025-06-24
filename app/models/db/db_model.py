from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String(120), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    nom = Column(String(100))
    prenom = Column(String(100))
    role = Column(String(20), default='contributrice')  # admin / contributrice / visiteuse

    profil = relationship('Profil', uselist=False, back_populates='user')

class Profil(Base):
    __tablename__ = 'profil'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    biographie = Column(Text)
    motivations = Column(Text)
    annee_reconversion = Column(Integer)
    region = Column(String(100))

    user = relationship('User', back_populates='profil')
    formations = relationship('Formation', back_populates='profil', cascade="all, delete")
    competences = relationship('Competence', back_populates='profil', cascade="all, delete")
    ressources = relationship('Ressource', back_populates='profil', cascade="all, delete")
    temoignages = relationship('Temoignage', back_populates='profil', cascade="all, delete")

class Formation(Base):
    __tablename__ = 'formation'

    id = Column(Integer, primary_key=True)
    profil_id = Column(Integer, ForeignKey('profil.id'), nullable=False)
    nom = Column(String(255), nullable=False)
    organisme = Column(String(255))
    date_debut = Column(String(50))
    date_fin = Column(String(50))
    format = Column(String(50))  # en ligne / présentiel
    type = Column(String(50))    # certif / bootcamp...

    profil = relationship('Profil', back_populates='formations')

class Competence(Base):
    __tablename__ = 'competence'

    id = Column(Integer, primary_key=True)
    profil_id = Column(Integer, ForeignKey('profil.id'), nullable=False)
    nom = Column(String(100), nullable=False)
    type = Column(String(50))  # "hard" ou "soft"
    niveau = Column(String(50))  # "débutante", etc.

    profil = relationship('Profil', back_populates='competences')


class CompetenceSuggestion(Base):
    __tablename__ = 'competence_suggestion'

    id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False, unique=True)
    type = Column(String(50))  # hard / soft

class Ressource(Base):
    __tablename__ = 'ressource'

    id = Column(Integer, primary_key=True)
    profil_id = Column(Integer, ForeignKey('profil.id'), nullable=False)
    type = Column(String(50))    # lien / vidéo / contact...
    titre = Column(String(255))
    url = Column(String(255))
    commentaire = Column(Text)

    profil = relationship('Profil', back_populates='ressources')

class Temoignage(Base):
    __tablename__ = 'temoignage'

    id = Column(Integer, primary_key=True)
    profil_id = Column(Integer, ForeignKey('profil.id'), nullable=False)
    contenu = Column(Text, nullable=False)
    publier = Column(Boolean, default=False)

    profil = relationship('Profil', back_populates='temoignages')
