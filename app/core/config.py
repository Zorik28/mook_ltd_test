from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Instant messaging service'
    database_url: str

    class Config:
        env_file = '.env'


settings = Settings()
