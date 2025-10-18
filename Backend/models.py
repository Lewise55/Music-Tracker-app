from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

class User(db.model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    user_name: Mapped[str] = mapped_column(String(120), nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)

    def sterialize(self):
        return{
            "id": self.id,
            "email": self.email,
            "user_name": self.user_name,
            # password should never be sterialized for security
        }

class Song(db.model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(120), nullable=False)
    artist: Mapped[str] = mapped_column(String(120), nullable=False)
    album: Mapped[str] = mapped_column(String(120), nullable=False)

    def sterialize(self):
        return{
            "id": self.id,
            "title": self.title,
            "artist": self.artist,
            "album": self.album,
        }