from pydantic_settings import BaseSettings


class MachingConfig(BaseSettings):
    MODEL_NAME: str = "ollama/deepseek-r1:7b"


matching_config = MachingConfig()
