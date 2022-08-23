from abc import ABC, abstractmethod
from typing import List, Optional

from flask import Flask, Response
from marshmallow import ValidationError
from werkzeug.exceptions import HTTPException

from ..response import response


class BaseHTTPException(ABC, HTTPException):
    
    @abstractmethod
    def __init__(
            self, 
            status: int, 
            message: str, 
            details: Optional[List[str]]
    ):
        super().__init__(message, error_response(message, details, status))


class BadRequest(BaseHTTPException):
    
    def __init__(
            self,
            message: str = "Bad request", 
            details: Optional[List[str]] = None
    ):
        super().__init__(400, message, details)


def error_response(
        message: str, 
        details: list[str] | None = None, 
        status: int = 500
) -> Response:
    return response({"message": message, "details": details}, status)


def handle_internal_server_error(_):
    return error_response("Internal server error")


def handle_validation_error(error: ValidationError) -> Response:
    details = []
    
    for field, error_messages in error.messages.items():
        for error_message in error_messages:
            details.append(f"{field}: {error_message}")
    
    return error_response("Validation error", details, 400)


def register_error_handlers(app: Flask):
    app.register_error_handler(ValidationError, handle_validation_error)
    
    if app.env == "production":
        app.register_error_handler(500, handle_internal_server_error)
