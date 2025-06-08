# 💬 ChatterBot Terminal Web App (Django)

This is a web-based chatbot application built using Django and [ChatterBot](https://github.com/gunthercox/ChatterBot), a conversational dialog engine for Python.

---

## 🚀 Features

- Django web app interface for chatting with a bot.
- ChatterBot integrated with English corpus training data.
- AJAX-based chat UI with real-time responses.
- Trained using built-in ChatterBot corpus.

---

## 📁 Project Structure

chatterbot_terminal_project/ ├── chat/ # Django app (views, urls, chatbot logic) ├── chatter/ # Django settings and main URLs ├── templates/ # HTML templates (index.html) ├── static/ # Optional static files (CSS/JS) ├── manage.py ├── requirements.txt ├── README.md └── .gitignor


---

## ⚙️ Installation & Setup

1. Clone the repository

```bash
git clone https://github.com/your-username/chatterbot-terminal-webapp.git
cd chatterbot-terminal-webapp

2. Create a virtual environment

python3 -m venv venv
source venv/bin/activate

3. Install dependencies

pip install -r requirements.txt


4. Download required SpaCy model and ChatterBot corpus

python -m spacy download en_core_web_sm


5. Run migrations

python manage.py migrate


6. Start the development server

python manage.py runserver

📦 Requirements

    Python 3.10+

    Django 5.x

    ChatterBot 1.2.7

    ChatterBot Corpus (optional but recommended)

    SpaCy with en_core_web_sm

