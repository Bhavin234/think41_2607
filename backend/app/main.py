from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from . import database, crud, models
from .llm import get_llm_response

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Request model for incoming chat messages
class ChatRequest(BaseModel):
    user_id: str
    message: str
    conversation_id: int = None

# Response model for the chat response
class ChatResponse(BaseModel):
    conversation_id: int
    user_message: str
    ai_response: str

@app.get("/")
def root():
    return {"message": "Chatbot backend is running!"}

@app.post("/api/chat", response_model=ChatResponse)
def chat(request: ChatRequest, db: Session = Depends(get_db)):
    # Get or create conversation
    if request.conversation_id:
        convo = db.query(models.Conversation).filter(
            models.Conversation.id == request.conversation_id
        ).first()
        if not convo:
            raise HTTPException(status_code=404, detail="Conversation not found")
    else:
        convo = crud.create_conversation(db, user_id=request.user_id)

    # Save user message
    crud.add_message(
        db,
        conversation_id=convo.id,
        sender="user",
        message=request.message
    )

    # Fetch all previous messages for context
    previous_msgs = db.query(models.Message).filter(
        models.Message.conversation_id == convo.id
    ).order_by(models.Message.timestamp).all()

    # Format for Groq
    chat_history = [{"role": "system", "content": "You are a helpful support chatbot for an e-commerce clothing site."}]
    for msg in previous_msgs:
        chat_history.append({
            "role": msg.sender,
            "content": msg.message
        })

    # Get AI response from Groq LLM
    try:
        ai_reply = get_llm_response(chat_history)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"LLM error: {e}")

    # Save AI response to DB
    crud.add_message(
        db,
        conversation_id=convo.id,
        sender="ai",
        message=ai_reply
    )

    return ChatResponse(
        conversation_id=convo.id,
        user_message=request.message,
        ai_response=ai_reply
    )
