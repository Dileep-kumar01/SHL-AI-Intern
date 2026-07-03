# SHL AI Assessment Recommender

## Project Overview

The SHL AI Assessment Recommender is a web application developed using FastAPI and Google's Gemini AI. It helps users find the most suitable SHL assessments based on a job role, skill, or technology.

The application searches the SHL assessment catalog and uses Gemini AI to generate concise, relevant, and user-friendly recommendations.

---

## Features

- AI-powered SHL assessment recommendations
- FastAPI backend
- Modern HTML, CSS, and JavaScript frontend
- Gemini AI integration
- SHL catalog search
- Health check API
- Responsive user interface
- Input validation for unrelated queries

---

## Technologies Used

- Python 3
- FastAPI
- HTML
- CSS
- JavaScript
- Gemini API
- Jinja2
- Python-dotenv

---

## Project Structure

```
SHL-AI-Intern/
│
├── app/
│   ├── api.py
│   ├── chatbot.py
│   ├── catalog.py
│   ├── gemini.py
│   ├── models.py
│
├── data/
│   └── shl_catalog.json
│
├── prompts/
│
├── static/
│   └── shl_style.css
│
├── templates/
│   └── index.html
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

Clone the repository.

```bash
git clone <repository-url>
```

Move into the project directory.

```bash
cd SHL-AI-Intern
```

Create a virtual environment.

```bash
python -m venv .venv
```

Activate the virtual environment.

Windows:

```bash
.venv\Scripts\activate
```

Install the required packages.

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Run the application.

```bash
uvicorn main:app --reload
```

Open your browser.

```
http://127.0.0.1:8000
```

---

## API Endpoints

### Home

```
GET /
```

Returns the web application.

### Health Check

```
GET /health
```

Returns the application status.

### Chat

```
POST /chat
```

Request

```json
{
    "message":"Python Developer"
}
```

Response

```json
{
    "user_message":"Python Developer",
    "reply":"Recommended SHL assessment..."
}
```

---

## Example Queries

- Java Developer
- Python Developer
- Software Engineer
- SQL Developer
- Data Analyst
- Sales Manager
- Leadership Assessment
- Personality Assessment

---

## Author

Dileep Kumar

B.Tech - Artificial Intelligence & Machine Learning

Vel Tech Rangarajan Dr. Sagunthala R&D Institute of Science and Technology

---

## License

This project was developed for the SHL AI Internship Assignment.
