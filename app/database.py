from sqlalchemy import create_engine, String
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, sessionmaker
import bcrypt

engine = create_engine("sqlite:///spaniv_db.db")
SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(128), nullable=False)

    def set_password(self, pw: str) -> None:
        pw_bytes = pw.encode()
        hash_bytes = bcrypt.hashpw(pw_bytes, bcrypt.gensalt())
        self.password_hash = hash_bytes.decode("utf-8")

    def check_password(self, pw: str) -> bool:
        pw_bytes = pw.encode("utf-8")
        return bcrypt.checkpw(pw_bytes, self.password_hash.encode("utf-8"))
    

Base.metadata.create_all(engine)
user_1 = User(email="testmail@gmail.com")
user_1.set_password("MyTestPassword")

with SessionLocal() as session:
    session.add(user_1)
    session.commit()