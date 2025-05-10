from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

# Hardcoded token (in a real app, never do this!)
HARDCODED_TOKEN = "supersecrettoken123"

# Use HTTPBearer for token extraction
security = Annotated[HTTPAuthorizationCredentials, Depends(HTTPBearer())]


def _verify_token(credentials: security):
    if credentials.credentials != HARDCODED_TOKEN:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing token",
            headers={"WWW-Authenticate": "Bearer"},
        )


validate_token = Annotated[None, Depends(_verify_token)]
