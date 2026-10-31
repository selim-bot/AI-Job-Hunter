from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "AI Job Hunter"
    app_env: str = "development"
    database_url: str = "postgresql+psycopg://jobhunter:local_password@localhost:5432/jobhunter"
    llm_api_key: str = ""
    llm_model: str = ""
    backend_url: str = "http://localhost:8000"
    max_jobs_per_search: int = 50
    minimum_match_score: int = 60

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
