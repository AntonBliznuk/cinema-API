from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "cinema-API"
    API_V1_STR: str = "/api/v1"

    # Database
    SQLALCHEMY_DATABASE_URI: str = "sqlite:///./test.db"

    class Config:
        case_sensitive = True


settings = Settings()
