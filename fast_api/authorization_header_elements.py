from typing import NamedTuple
from starlette.requests import Request as StarletteRequest
from verify_token import UnauthorizedException, UnauthenticatedExcepton

class AuthorizationHeaderElements(NamedTuple):
    authorization_scheme: str
    bearer_token: str
    are_valid: bool

def get_authorization_header_elements(
        authorization_header: str,
) -> AuthorizationHeaderElements: 
    try:
        authorization_scheme, bearer_token = authorization_header.split()
    except ValueError:
        raise UnauthorizedException
    else:
        valid = authorization_scheme.lower() == "bearer" and bool(bearer_token.strip())
        return AuthorizationHeaderElements(authorization_scheme, bearer_token, valid)

def get_bearer_token(request: StarletteRequest) -> str:
    authorization_header = request.headers.get("Authorization")
    if authorization_header:
        authorization_header_elements = get_authorization_header_elements(
            authorization_header
        )
        if authorization_header_elements.are_valid:
            return authorization_header_elements.bearer_token
        else:
            raise UnauthorizedException
    else:
        raise UnauthenticatedExcepton
