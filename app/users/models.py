from ..extensions.bcrypt import bcrypt
from ..extensions.database import IntegerPKMixin, db


class User(db.Model, IntegerPKMixin):
    __tablename__ = "users"
    
    username = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(250), unique=True, index=True)
    password = db.Column(db.String(250))
    
    def check_password(self, password: str) -> bool:
        return bcrypt.check_password_hash(self.password, password)
    
    def set_password(self, password: str):
        self.password = str(bcrypt.generate_password_hash(password), "utf-8")
