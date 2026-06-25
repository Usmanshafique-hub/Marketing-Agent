from fastapi import FastAPI
from pydantic import BaseModel
from app.agent import generate_marketing_content

app = FastAPI()

class MarketingRequest(BaseModel):
    business_name: str
    audience: str
    goal: str
    platform: str


@app.post("/generate")
def generate(request: MarketingRequest):
    result = generate_marketing_content(
        request.business_name,
        request.audience,
        request.goal,
        request.platform
    )

    return {"result": result}