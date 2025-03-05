from pydantic_settings import BaseSettings


class JobConfig(BaseSettings):
    MODEL_NAME: str = "ollama/deepseek-r1:7b"


job_config = JobConfig()
