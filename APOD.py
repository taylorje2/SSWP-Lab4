from pydantic import BaseModel

class nasa_apod(BaseModel):
    date: str
    explanation: str
    title: str
    hdurl: str


