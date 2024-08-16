from fastapi import Depends, HTTPException, status
import jwt
from verify_token import VerifyToken
from authorization_header_elements import get_bearer_token

def validate_token(token: str = Depends(get_bearer_token)):
    return VerifyToken(token).verify()

class PermissionDeniedException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN, detail="Permission denied"
        )

class PermissionsValidator:
    def __init__(self, required_permissions: list[str]):
        self.required_permissions = required_permissions
    
    def __call__(self, token: str = Depends(validate_token)):
        token_permissions = token.get("permissions")
        token_permissions_set = set(token_permissions)
        required_permissions_set = set(self.required_permissions)

        if not required_permissions_set.issubset(token_permissions_set):
            raise PermissionDeniedException
                 