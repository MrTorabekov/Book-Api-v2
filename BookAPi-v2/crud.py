from sqlalchemy.orm import Session
from models import User, Book
import schemas


def create_user(db: Session, user: schemas.UserCreate):
    db_user = User(
        username=user.username,
        email=user.email,
        password=user.password,
        is_active=user.is_active
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# Create a new book
def create_book(db: Session, book: schemas.BookCreate, user_id: int):
    db_book = Book(
        title=book.title,
        language=book.language,
        isbn=book.isbn,
        pages=book.pages,
        user_id=user_id
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book
