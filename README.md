# 🛍️ E-Commerce Customer Support Chatbot

A full-stack conversational AI application designed for an e-commerce clothing website.  
This chatbot helps users interactively query order status, product availability, and popular items using natural language.

---

## 🧰 Tech Stack

| Layer        | Technology            |
|--------------|------------------------|
| Frontend     | React.js               |
| Backend      | FastAPI (Python)       |
| Database     | MySQL 8                |
| LLM API      | Groq ChatCompletion (Gemma-7B) |
| Containerization | Docker + Docker Compose |

---

## 🚀 Features (Milestone Summary)

### ✅ Milestone 1: Environment Setup
- Created project with `frontend/` and `backend/` directories.
- Imported sample CSV e-commerce dataset.

### ✅ Milestone 2: Database Setup & Data Ingestion
- Designed MySQL tables based on 6 CSVs.
- Added `load_data.py` script to parse and insert data into MySQL.

### ✅ Milestone 3: Data Schemas
- Created models for:
  - Users, Products, Orders, Inventory
  - Conversations, Messages
- Each user can have multiple chat sessions with message history.

### ✅ Milestone 4: Core Chat API
- Implemented `/api/chat` endpoint.
- Accepts user queries and stores AI responses chronologically.

### ✅ Milestone 5: LLM Integration
- Integrated Groq API (free API key).
- Chatbot asks clarifying questions before replying with accurate data.
- Uses SQL and business logic to generate intelligent responses.

### ✅ Milestone 6–8: Frontend Chat UI & State
- Built React components: `ChatWindow`, `MessageList`, `UserInput`, `HistoryPanel`
- State managed with React Context API.
- Users can view, resume, and switch between sessions.

### ✅ Milestone 9: Full-Stack Integration
- Enabled CORS in backend.
- Connected frontend to FastAPI backend with message streaming.

### ✅ Milestone 10: Dockerization
- Dockerized backend, frontend, and MySQL.
- `docker-compose up` brings up full stack locally.

---

---

## ⚙️ Setup & Running Instructions

### 🧪 Local (Manual)

1. **MySQL DB**
   - Create a MySQL 8 DB:
     ```bash
     mysql -u root -p
     CREATE DATABASE chatbot_db;
     ```
   - Run `load_data.py` from `backend/` to insert CSVs.

2. **Backend**
   ```bash
   cd backend
   pip install -r requirements.txt
   uvicorn app.main:app --reload

3. **Frontend**
   ```bash
    cd frontend
    npm install
    npm start

4. **Docker**
    ```bash
    docker-compose up --build

Access:
Frontend: http://localhost:3000
Backend (docs): http://localhost:8000/docs


## 👨‍💻Author
Bhavin Sharma
GitHub: @bhavin234
