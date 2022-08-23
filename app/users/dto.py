from dataclasses import dataclass

from ..base.dto import RequestDTO, ResponseDTO
from .schemas import UserCreateSchema, UserResponseSchema


@dataclass(frozen=True)
class UserCreateDTO(RequestDTO):
    schema_class = UserCreateSchema
    
    username: str
    email: str
    password: str


@dataclass(frozen=True)
class UserResponseDTO(ResponseDTO):
    schema_class = UserResponseSchema
    
    id: str
    username: str
    email: str
