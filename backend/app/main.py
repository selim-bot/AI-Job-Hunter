from fastapi import FastAPI

from app.routes import jobs, resume, applications

app = FastAPI(
    title="AI Job Hunter",
    description="AI-powered job discovery and application assistant",
    version="1.0",
)

app.include_router(resume.router)
app.include_router(jobs.router)
app.include_router(applications.router)


@app.get("/")
def home():
    return {"message": "AI Job Hunter API is running", "status": "success"}


@app.get("/health")
def health():
    return {"status": "healthy"}
