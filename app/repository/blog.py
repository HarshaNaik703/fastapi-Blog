from .. import models, schemas, database
from fastapi import HTTPException, status


def create_blog(request, db, current_user):
    new_blog = models.Blog(title=request.title,
                           body=request.body,
                           user_id=current_user.user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def show_blog(db):
    blogs = db.query(models.Blog).all()
    return blogs

def delete_blog(db, blog_id):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Blog not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return f"Blog successfuclly deleted"

def show_specifif(db, blog_id):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()

    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")

    return blog

def update(request, db):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Blog not found")
    blog.update(request)
    db.commit()
    return f"blog updated"

