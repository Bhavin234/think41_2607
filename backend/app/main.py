from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from . import database, crud, models

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Request model
class ChatRequest(BaseModel):
    user_id: str
    message: str
    conversation_id: int = None

# Response model
class ChatResponse(BaseModel):
    conversation_id: int
    user_message: str
    ai_response: str

@app.post("/api/chat", response_model=ChatResponse)
def chat(request: ChatRequest, db: Session = Depends(get_db)):
    if request.conversation_id:
        # Use existing conversation
        convo = db.query(models.Conversation).filter(models.Conversation.id == request.conversation_id).first()
        if not convo:
            raise HTTPException(status_code=404, detail="Conversation not found")
    else:
        # Start new conversation
        convo = crud.create_conversation(db, user_id=request.user_id)

    # Save user message
    crud.add_message(db, conversation_id=convo.id, sender="user", message=request.message)

    # Mock AI response
    ai_reply = f"I'm just a bot! You said: {request.message}"

    # Save AI reply
    crud.add_message(db, conversation_id=convo.id, sender="ai", message=ai_reply)

    return ChatResponse(
        conversation_id=convo.id,
        user_message=request.message,
        ai_response=ai_reply
    )
