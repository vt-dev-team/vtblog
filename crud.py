from sqlalchemy.orm import Session
import time
from . import models, schemas

def get_post(db: Session, post_id: int):
    return db.query(models.Post).filter(models.Post.id == post_id).first()

def get_posts(db: Session, skip: int = 0, limit: int = 20):
    return db.query(models.Post).offset(skip).limit(limit).all()

def create_user(db: Session, post: schemas.PostCreate):
    db_post = models.Post(title=post.title, content=post.content, tags=post.tags, toplevel=post.toplevel, date=(int)(time.time()), defunct=post.defunct)