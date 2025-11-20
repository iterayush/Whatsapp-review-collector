from sqlalchemy import Column, Integer, String, Text, DateTime, func
from .database import Base

class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True, index=True)
    contact_number = Column(String, index=True)
    user_name = Column(String, nullable=True)
    product_name = Column(String, nullable=True)
    product_review = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class ConversationState(Base):
    __tablename__ = "conversation_state"
    id = Column(Integer, primary_key=True, index=True)
    phone_number = Column(String, unique=True, index=True)
    state = Column(String)           # ASK_PRODUCT, ASK_NAME, ASK_REVIEW
    temp_product = Column(String, nullable=True)
    temp_name = Column(String, nullable=True)
