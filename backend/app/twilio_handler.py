from sqlalchemy.orm import Session
from . import crud

def twiml_message(text: str):
    # Return TwiML XML string
    return f"<Response><Message>{text}</Message></Response>"

def handle_whatsapp_message(db: Session, from_number: str, body: str):
    contact = from_number
    body_text = (body or "").strip()

    sess = crud.get_session(db, contact)
    # No session -> ask product
    if not sess:
        crud.create_or_update_session(db, contact, state='ASK_PRODUCT')
        return "Welcome! Which product is this review for?"

    # ASK_PRODUCT -> store product, ask name
    if sess.state == 'ASK_PRODUCT':
        product = body_text or "Unknown Product"
        crud.create_or_update_session(db, contact, state='ASK_NAME', temp_product=product)
        return "What's your name?"

    # ASK_NAME -> store name, ask review
    if sess.state == 'ASK_NAME':
        name = body_text or "Anonymous"
        crud.create_or_update_session(db, contact, state='ASK_REVIEW', temp_name=name, temp_product=sess.temp_product)
        return f"Please send your review for {sess.temp_product}."

    # ASK_REVIEW -> create review, delete session
    if sess.state == 'ASK_REVIEW':
        review_text = body_text or ""
        user_name = sess.temp_name or "Anonymous"
        product_name = sess.temp_product or "Unknown Product"
        crud.create_review(db, contact, user_name=user_name, product_name=product_name, product_review=review_text)
        crud.delete_session(db, contact)
        return f"Thanks {user_name} — your review for {product_name} has been recorded. 🙏"

    # fallback
    crud.create_or_update_session(db, contact, state='ASK_PRODUCT')
    return "Which product is this review for?"
