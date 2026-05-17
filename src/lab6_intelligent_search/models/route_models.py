from pydantic import BaseModel


class RouteRequest(BaseModel):
    start: str
    goal: str