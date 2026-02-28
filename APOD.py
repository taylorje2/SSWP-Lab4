from pydantic import BaseModel

# class for the APOD results
class nasa_apod(BaseModel):
    # birthdate for the APOD
    date: str
    # explanation of the APOD
    explanation: str
    # title of the APOD
    title: str
    # standard resolution image URL of the APOD
    url: str
    # high res version image URL of the APOD
    hdurl: str

    # results layout of the APOD
    def __str__(self):
        return f"Title: {self.title}\nDate: {self.date}\nExplanation: {self.explanation}\nURL: {self.url}\nHD URL: {self.hdurl}"