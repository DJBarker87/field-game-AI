
# Ask Ralph – Eton Field Game Assistant (OpenAI Assistant API)

This project creates a website where users can ask questions about the Eton Field Game and receive clear, polite, and accurate answers from "Ralph", the Master in charge.

## 🧠 Powered By:
- OpenAI's Assistant API
- gpt-4-turbo
- Field Game Laws 2025 and Ralph's email archive

---

## 🚀 Quick Start

### 1. Clone this repo

```bash
git clone https://github.com/yourusername/ask-ralph.git
cd ask-ralph
```

### 2. Install dependencies

Make sure you have Python 3.9+ and pip installed.

```bash
pip install -r requirements.txt
```

### 3. Set your OpenAI API Key

Create a `.env` file and paste:

```
OPENAI_API_KEY=sk-...
```

### 4. Run the Assistant Setup

This will upload the Field Game Laws and email archive and create your Assistant:

```bash
python backend/setup_assistant.py
```

### 5. Start the Backend Server

```bash
python backend/app.py
```

### 6. Open the Website

Coming soon – or use any frontend connected to `http://localhost:5000/ask-ralph`.

---

## 📁 Contents

- `/backend`: Python Flask server using OpenAI Assistant API
- `/data`: Source files (laws + emails)
- `/frontend`: (Optional) React UI or connect via any client
- `/docs`: Notes, changelogs, API guides

---

## 🧵 Threaded Memory

This version supports conversation memory – Ralph will remember follow-up questions in context!

---

## 🛠 Requirements

- Python 3.9+
- OpenAI API key
- Internet connection

---

Made with a lot of care and tradition.
