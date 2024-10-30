from restaurant import db, bcrypt
from flask_login import UserMixin
from datetime import datetime

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.Text, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    role = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    __table_args__ = (
        db.CheckConstraint("role IN ('customer', 'owner')", name='check_role'),
    )

    def __repr__(self):
        return f'<User {self.email}>'

    # def __init__(self, **kwargs):
    #     super(User, self).__init__(**kwargs)
    #     if 'password' in kwargs:
    #         self.password = kwargs['password']

    # @property
    # def password(self):
    #     raise AttributeError('Password is not readable')

    # @password.setter
    # def password(self, plain_text_password):
    #     if plain_text_password:
    #         self.password_hash = bcrypt.generate_password_hash(
    #             plain_text_password
    #         ).decode('utf-8')

    # def check_password_correction(self, attempted_password):
    #     return bcrypt.check_password_hash(self.password_hash, attempted_password)

    # def update_last_login(self):
    #     """Update the last login timestamp"""
    #     self.last_login = datetime.utcnow()
    #     db.session.commit()

    # @property
    # def full_name(self):
    #     """Return the user's full name"""
    #     return f"{self.first_name} {self.last_name}"

    # def to_dict(self):
    #     """Convert user object to dictionary for API responses"""
    #     return {
    #         'id': self.id,
    #         'firstName': self.firstName,
    #         'lastName': self.lastName,
    #         'email': self.email,
    #         'phoneNumber': self.phoneNumber,
    #         'role': self.role
    #     }

    # def __repr__(self):
    #     return f'<User {self.email}>'
