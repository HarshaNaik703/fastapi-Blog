from fastapi import APIRouter, HTTPException, status, dependencies, Depends
from typing import List
from ..database import get_db
from .. import schemas, models
from sqlalchemy.orm import Session
from .. import oauth2

from ..repository import blog


router = APIRouter(
    prefix="/blogs",
    dependencies=[Depends(oauth2.get_current_user)],
    tags=["blogs"],
)

@router.get("/", response_model=List[schemas.ShowBlog])
def all(db : Session = Depends(get_db)):
    return blog.show_blog(db)


@router.get("/{blog_id}", response_model=schemas.ShowBlog)
def showBlog(
    blog_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(oauth2.get_current_user)
):
    return blog.show_specifif(db, blog_id)

@router.post("/create_blog")
def create_blog(request : schemas.Blog, db : Session = Depends(get_db),
                current_user: models.User = Depends(oauth2.get_current_user)):
    return blog.create_blog(request, db, current_user)

@router.delete("/delete_post/{blog_id}")
def delete_post(blog_id: int, db: Session = Depends(get_db)):
    return blog.delete_blog(db, blog_id)


@router.put("/update/{blog_id}")
def update_post(request: schemas.Blog,blog_id: int, db: Session = Depends(get_db)):
    return blog.update(request, db)    
    
    
