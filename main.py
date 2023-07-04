import json
import os
from googletrans import Translator
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

translator = Translator()

engine = create_engine(f'postgresql://{os.getenv("DB_USERNAME")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_HOST")}:5432/{os.getenv("DB_NAME")}')

Base = declarative_base()


class Auth(Base):
    __tablename__ = "tbl_authorizations"
    id = Column(Integer, primary_key=True)
    code = Column(String)
    title = Column(String)


Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

results = session.query(Auth).all()

liste = []

with open("localizationWords.json", "r+",encoding="utf-8") as file:
    data = json.load(file)
    for index, row in enumerate(results):
        if row.code in data:
            pass
        else:
            example = translator.translate(row.title)
            result = {"tr": row.title, "en": example.text}
            data[row.code] = result
with open("newJsonFile.json","w",encoding="utf-8") as json_file:

    json_file.write(json.dumps(data, sort_keys=True, indent=4))
    print("Saved Successfully")

session.close()
