from sqlalchemy.orm import mapper, relationship, MetaData
from sqlalchemy import MetaData, Table, Column, Interger, String

import model

metadata = MetaData()

post = Table(
    "post",
    metadata,
    Column("id", Interger, primary_key=True, autoincrement=True),
    Column("title", String(255))
)

def start_mappers():
    post_mapper = mapper(model.PostLine, post)