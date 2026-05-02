from .. import models, hash
from fastapi import HTTPException, status
from .. import jwt_handler

def authentication(request, db):
    user = db.query(models.User).filter(
        models.User.email == request.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="user doesn't exist")
    if not hash.Hash.rehash(request.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Email or password is wrong")
    access_token = jwt_handler.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
