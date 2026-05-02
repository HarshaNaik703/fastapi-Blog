from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from .. import database, jwt_handler, schemas, models, hash
from sqlalchemy.orm import Session
from ..repository import authentication

router = APIRouter(
    tags=["authentication"],
    prefix="/auth"
)


@router.post("/login")
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    return authentication.authentication(request, db)
