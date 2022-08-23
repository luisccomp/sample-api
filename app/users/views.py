from flask import Blueprint, request

from ..exceptions import BadRequest
from ..extensions.database import db
from ..response import response
from .dto import UserCreateDTO, UserResponseDTO
from .models import User


users_blueprint = Blueprint("users", __name__)


@users_blueprint.post("")
def register_user():
    user_data = UserCreateDTO.from_request(request)
    
    if User.query.filter(User.username == user_data.username).first():
        raise BadRequest("Choose a different username")
    
    elif User.query.filter(User.email == user_data.email).first():
        raise BadRequest("Choose a different email")
    
    user = User(email=user_data.email)
    user.set_password(user_data.password)
    
    db.session.add(user)
    db.session.commit()
    
    user_response = UserResponseDTO.from_object(user)
    
    return response(user_response.asdict(), status=201)
