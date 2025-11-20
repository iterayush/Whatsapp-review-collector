import os
from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.responses import Response
from sqlalchemy.orm import Session
from dotenv import load_dotenv
from .database import SessionLocal, engine, Base
from . import models, crud, schemas, twilio_handler

# load backend/.env if present
env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path=env_path)

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="WhatsApp Product Review Collector")

# CORS
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/webhook")
async def whatsapp_webhook(request: Request, db: Session = Depends(get_db)):
    form = await request.form()
    from_number = form.get('From')
    body = form.get('Body')
    if not from_number:
        raise HTTPException(status_code=400, detail="Missing From field")
    reply_text = twilio_handler.handle_whatsapp_message(db, from_number, body)
    xml = twilio_handler.twiml_message(reply_text)
    return Response(content=xml, media_type="application/xml")

from typing import List
@app.get("/api/reviews", response_model=List[schemas.ReviewOut])
def get_reviews(db: Session = Depends(get_db)):
    reviews = crud.get_reviews(db)
    return reviews

@app.get("/")
def root():
    return {"message": "WhatsApp Review Collector backend running."}
