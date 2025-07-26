from sqlalchemy import Column, Integer, String, Text, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base

class Conversation(Base):
    __tablename__ = 'conversations'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(50))
    created_at = Column(DateTime, default=func.now())

    messages = relationship("Message", back_populates="conversation")

class Message(Base):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True, index=True)
    conversation_id = Column(Integer, ForeignKey('conversations.id'), ondelete='CASCADE')
    sender = Column(Enum("user", "ai"), nullable=False)  # 'user' or 'bot'
    message = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=func.now())
    conversation = relationship("Conversation", back_populates="messages")
    