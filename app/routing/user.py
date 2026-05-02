from fastapi import APIRouter, Depends, status, HTTPException
import bcrypt
from .. import database, schemas, models, oauth2
from sqlalchemy.orm import Session

from ..repository import user

router = APIRouter(tags=["user"], prefix="/user")

get_db = database.get_db

@router.post("/createUser", response_model = schemas.ShowUser)
def createUser(request:schemas.User, db:Session = Depends(get_db)):
    return user.userCreate(request, db)


@router.get("/{user_id}", response_model=schemas.ShowUser)
def showUser(user_id: int, db: Session = Depends(get_db), current_user=Depends(oauth2.get_current_user)):
    return user.showUser(user_id, db)
