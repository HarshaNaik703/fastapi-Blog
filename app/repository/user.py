from fastapi import APIRouter, Depends, status, HTTPException
import bcrypt
from .. import database, schemas, models, hash, oauth2
from sqlalchemy.orm import Session

def userCreate(request, db):
    newUser = models.User(name=request.name, email=request.email,
                          password=hash.Hash.hash(request.password))
    db.add(newUser)
    db.commit()
    db.refresh(newUser)
    return newUser


def showUser(user_id, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.user_id == user_id).first()

    if user:
        return user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User associated with {user_id} not found"
    )
