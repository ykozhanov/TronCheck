from pydantic import BaseModel


class ResponseSchema(BaseModel):
    message: str


class ExceptionSchema(ResponseSchema):
    details: dict
