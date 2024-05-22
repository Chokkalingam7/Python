from sqlalchemy.orm import DeclarativeBase
class Base(DeclarativeBase):
    pass
class User(Base):
    __tablename__="users"
    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]=mapped_column(nullable=False)
    age:Mapped[int]
class Comment(Base):
    __tablename__="comments"
    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]=mapped_column(nullable=False)
