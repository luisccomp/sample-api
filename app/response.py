from json import dumps
from typing import Any, Mapping

from flask import Response


def response(
        data: Mapping[str, Any], 
        status: int = 200, 
        headers: Mapping[str, Any] | None = None
) -> Response:
    if not headers:
        headers = {}
    
    if not headers.get("Content-Type"):
        headers["Content-Type"] = "application/json"
        
    return Response(dumps(data), status, headers)
