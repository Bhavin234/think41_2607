from sqlalchemy.orm import Session
from . import models

def create_conversation(db: Session, user_id: str):
    convo = models.Conversation(user_id=user_id)
    db.add(convo)
    db.commit()
    db.refresh(convo)
    return convo

def add_message(db: Session, conversation_id: int, sender: str, message: str):
    msg = models.Message(
        conversation_id=conversation_id,
        sender=sender,
        message=message
    )
    db.add(msg)
    db.commit()
    db.refresh(msg)
    return msg
