from pydantic import BaseModel


class AbstractModel(BaseModel):
    class Config:
        allow_mutation = False
