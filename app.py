# app.py

from fastapi import FastAPI
from pydantic import BaseModel
from services.auditor import SustainabilityAuditor
from utils.scraper import extract_text_from_url

app = FastAPI(title="Green-Truth Auditor 🌱")

auditor = SustainabilityAuditor()


class AuditRequest(BaseModel):
    text: str | None = None
    url: str | None = None


@app.get("/")
def home():
    return {"message": "Green-Truth Auditor is running 🚀"}


@app.post("/audit")
def audit(request: AuditRequest):

    if request.url:
        text = extract_text_from_url(request.url)
    else:
        text = request.text

    if not text:
        return {"error": "Provide either text or URL"}

    result = auditor.audit(text)

    return result