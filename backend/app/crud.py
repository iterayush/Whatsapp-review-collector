from sqlalchemy.orm import Session
from . import models

# Reviews
def create_review(db: Session, contact_number: str, user_name: str, product_name: str, product_review: str):
    review = models.Review(
        contact_number=contact_number,
        user_name=user_name,
        product_name=product_name,
        product_review=product_review
    )
    db.add(review)
    db.commit()
    db.refresh(review)
    return review

def get_reviews(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Review).order_by(models.Review.created_at.desc()).offset(skip).limit(limit).all()

# Session state
def get_session(db: Session, phone_number: str):
    return db.query(models.ConversationState).filter(models.ConversationState.phone_number == phone_number).first()

def create_or_update_session(db: Session, phone_number: str, state: str, temp_product=None, temp_name=None):
    sess = get_session(db, phone_number)
    if not sess:
        sess = models.ConversationState(
            phone_number=phone_number,
            state=state,
            temp_product=temp_product,
            temp_name=temp_name
        )
        db.add(sess)
    else:
        sess.state = state
        sess.temp_product = temp_product
        sess.temp_name = temp_name
    db.commit()
    db.refresh(sess)
    return sess

def delete_session(db: Session, phone_number: str):
    sess = get_session(db, phone_number)
    if sess:
        db.delete(sess)
        db.commit()
