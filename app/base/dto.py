from abc import ABC, abstractmethod
from dataclasses import asdict, fields
from typing import Any, Type

from flask import Request
from marshmallow import EXCLUDE, Schema


class DTO(ABC):
    
    schema_class: Type[Schema]
    
    @classmethod
    def schema(cls):
        return cls.schema_class(
            only=[f.name for f in fields(cls)], unknown=EXCLUDE)
    
    @abstractmethod
    def __init__(self): ...
    
    def asdict(self):
        return asdict(self)


class RequestDTO(DTO):
    
    @classmethod
    def from_request(cls, request: Request):
        return cls(**cls.schema().load(request.json))


class ResponseDTO(DTO):
    
    @classmethod
    def from_object(cls, o: Any, many: bool = False):
        schema = cls.schema()
        serialized_data = schema.dump(o, many=many)
        
        if many:
            return [cls(**params) for params in serialized_data]
        
        return cls(**serialized_data)
