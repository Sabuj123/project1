from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/training"
DATABASE_URL = "postgresql+psycopg2://test_9v9v_user:WlpyvxnmGqLFBep1UICMNqiDbnJomiYx@dpg-dc383h8m7kps73dg602g-a.oregon-postgres.render.com/test_9v9v"

engine = create_engine(DATABASE_URL)
session_local = sessionmaker(autocommit = False, autoflush= False, bind=engine)
base = declarative_base()
