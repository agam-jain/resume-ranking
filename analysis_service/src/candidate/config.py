from pydantic_settings import BaseSettings


class CandidateConfig(BaseSettings):
    MODEL_NAME: str = "ollama/deepseek-r1:7b"

    CV_UPLOAD_DIR: str = "./candidate_cv/"


candidate_config = CandidateConfig()
