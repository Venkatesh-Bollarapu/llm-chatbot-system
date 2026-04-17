# 🤖 LLM Chatbot System (Stateless Version)

A simple chatbot built using **Streamlit + LangGraph + Google Gemini LLM**.

This is the **initial version** of the project, demonstrating a stateless chatbot where each query is processed independently.

---

## 🚀 Features

* 💬 Chat interface using Streamlit
* ⚡ Fast responses using Gemini LLM
* 🧠 LangGraph workflow integration
* 🔁 Clean and minimal architecture

---

## 🧱 Tech Stack

* **Frontend:** Streamlit
* **LLM:** Google Gemini (`gemini-2.5-flash`)
* **Framework:** LangGraph + LangChain

---

## 📁 Project Structure

```
.
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/your-username/llm-chatbot-system.git
cd llm-chatbot-system
```

---

### 2. Create virtual environment

```
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

### 4. Add API Key

Create a `.env` file:

```
GOOGLE_API_KEY=your_api_key_here
```

---

### 5. Run the app

```
streamlit run app.py
```

---

## 🧠 How It Works

1. User enters input
2. Input is sent to Gemini LLM
3. Response is generated and displayed
4. Chat UI maintains history (UI only)

---

## ⚠️ Note

* This is a **stateless chatbot**
* LLM does NOT remember previous messages
* Chat history is only stored in UI (`session_state`)

---

## 🔮 Upcoming Improvements

* Add conversation memory (stateful chatbot)
* Add persistent storage
* Add RAG (Retrieval-Augmented Generation)

---

## 👨‍💻 Author

Venkatesh Bollarapu

