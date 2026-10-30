from pathlib import Path

import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DATA_DIR = Path(__file__).parent.parent / "data"
DATA_DIR.mkdir(exist_ok=True)

class Base(DeclarativeBase):
    pass

def get_database_url():
    if "connections" in st.secrets and "postgresql" in st.secrets["connections"]:
        config = st.secrets["connections"]["postgresql"]
        return (
            f"postgresql+psycopg2://{config['username']}:{config['password']}"
            f"@{config['host']}:{config['port']}/{config['database']}"
        )

    return f"sqlite:///{DATA_DIR / 'dates.db'}"


engine = create_engine(get_database_url(), pool_pre_ping=True)

SessionLocal = sessionmaker(autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(engine)
