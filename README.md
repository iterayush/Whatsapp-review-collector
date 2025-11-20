# Whatsapp-review-collector

##Built with:

  FastAPI (Python backend)
  PostgreSQL (Database)
  React (Frontend UI)
  Twilio WhatsApp Sandbox (Messaging)
  Docker Compose (Easiest way to run everything)

##Install Docker Desktop

Download: https://www.docker.com/products/docker-desktop/

After installation, ensure you see:

Engine running

##Twilio WhatsApp Sandbox Setup
Step 1 — Create Twilio Account

https://www.twilio.com/try-twilio

Step 2 — Enable WhatsApp Sandbox

Open:
https://console.twilio.com/us1/develop/sms/try-it-out/whatsapp-learn

You will get:

Sandbox number (example: +14155238886)

Join code (example: join desk-blue)

Send the join code to the sandbox number via WhatsApp.

Step 3 — Get your credentials

Go to:

Console → Settings → API Keys / Account Info

Collect:

TWILIO_ACCOUNT_SID = ACxxxxxxxxxxxxxxxxxxxx
TWILIO_AUTH_TOKEN  = yyyyyyyyyyyyyyyyyyyyy
TWILIO_WHATSAPP_NUMBER = whatsapp:+1415xxxxxxx

##Create .env file

Inside backend/ create a file named .env:

DATABASE_URL=postgresql://postgres:postgres@db:5432/reviewsdb
TWILIO_ACCOUNT_SID=ACxxxx...
TWILIO_AUTH_TOKEN=yyyyyyy...
TWILIO_WHATSAPP_NUMBER=whatsapp:+1415xxxxxxx
HOST_URL=http://localhost:8000

##Start Backend + PostgreSQL using Docker

Open terminal in the project root:
docker compose up --build

This will:
  Build backend
  Start PostgreSQL

Create required tables

Start FastAPI server at:
http://localhost:8000

You will see:

Uvicorn running on http://0.0.0.0:8000


Do not close this terminal.

##Start React Frontend

Open a second terminal:

cd frontend
npm install
npm start


Frontend runs at:

👉 http://localhost:3000

##Connect Twilio Webhook

Go to:

Twilio Console → WhatsApp Sandbox Settings

Look for:

"When a message comes in"
Paste this:

http://localhost:8000/webhook


Click Save.

##Test Your WhatsApp Bot
<Send ("price-honor") to start Twilio Chat.>

In WhatsApp, send message to your sandbox number:

Hi
Bot conversation:
1️⃣ Bot → “Which product is this review for?”
2️⃣ You → Laptop
3️⃣ Bot → “What’s your name?”
4️⃣ You → Ayush
5️⃣ Bot → “Please send your review for Laptop.”
6️⃣ You → Battery life is amazing.
7️⃣ Bot → “Thanks Ayush — your review for Laptop has been recorded. 🙏”

Review saved!

##View Reviews in the Dashboard

Open:

http://localhost:3000

You will see a table:

User	Product	Review	Time
Ayush	Laptop	Battery life is amazing	2025-11-20 10:18 AM
##Stop All Services

Press CTRL + C in both terminals.


