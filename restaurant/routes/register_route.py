from flask import Blueprint, request, jsonify
from services.register_service import UserService
import logging

logger = logging.getLogger(__name__)
user_controller = Blueprint('user_controller', __name__)

@user_controller.route('/api/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        logger.info(f"Received registration request for email: {data.get('email')}")

        # Call the service to handle registration logic
        result, status_code = UserService.register_user(data)

        return jsonify(result), status_code

    except Exception as e:
        logger.exception("Registration error")
        return jsonify({'error': 'Registration failed. Please try again.'}), 500
