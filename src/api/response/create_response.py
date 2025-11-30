from pydantic import BaseModel

class CreateResponse(BaseModel):
    Name: str
    Job: str
