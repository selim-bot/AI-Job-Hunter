# AI Job Hunter

AI-powered job discovery, matching and application assistant.
Stack: Python, FastAPI, LangGraph, Playwright, PostgreSQL, Streamlit, Docker, Render.

## Quick start (Windows PowerShell)

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r backend/requirements.txt
python -m playwright install chromium
copy .env.example .env   # then edit values
uvicorn app.main:app --reload --app-dir backend
streamlit run frontend/dashboard.py   # in a second terminal
```

- API docs: http://127.0.0.1:8000/docs
- Dashboard: http://localhost:8501
- Tests: `pytest`

Applications must never be submitted without explicit user approval.
Respect job-site terms; never bypass CAPTCHA/MFA/anti-bot protections.
