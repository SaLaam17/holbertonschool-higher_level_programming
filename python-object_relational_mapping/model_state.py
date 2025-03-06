#!/usr/bin/python3
"""Start link class to table in database 
"""
import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Déclaration de la base
Base = declarative_base()

# Définition de la classe State
class State(Base):
    """ State class to link to the 'states' table in the database """
    __tablename__ = 'states'

    # Attributs de la classe qui correspondent aux colonnes de la table
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    # Récupère les arguments passés dans la ligne de commande
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Créer la connexion avec la base de données MySQL
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{db_name}', pool_pre_ping=True)

    # Créer toutes les tables liées à la base (table 'states' incluse)
    Base.metadata.create_all(engine)
