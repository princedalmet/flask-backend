from werkzeug.security import generate_password_hash
from database.user_database import UserDatabase
import logging

logger = logging.getLogger(__name__)

class UserService:
    @staticmethod
    def register_user(data):
        # Validate required fields
        required_fields = ['first_name', 'last_name', 'email', 'password']
        for field in required_fields:
            if not data.get(field):
                return {'error': f'{field.replace("_", " ").title()} is required'}, 400

        # Validate the role field
        role = data.get('role', 'customer')  # Default role to 'customer' if not provided
        if role not in ['customer', 'owner']:
            return {'error': 'Invalid role. Allowed values are "customer" or "owner".'}, 400

        # Check if user already exists
        if UserDatabase.get_user_by_email(data['email']):
            return {'error': 'Email already registered'}, 409

        # Hash the password
        password_hash = generate_password_hash(data['password'])

        # Create new user record
        user_data = {
            'email': data.get('email'),
            'password_hash': password_hash,
            'first_name': data.get('first_name'),
            'last_name': data.get('last_name'),
            'role': role
        }

        # Attempt to add the user to the database
        try:
            UserDatabase.add_user(user_data)
            return {'message': 'Registration successful'}, 201
        except Exception as e:
            logger.error(f"Error during registration: {e}")
            return {'error': 'Registration failed. Please try again.'}, 500
