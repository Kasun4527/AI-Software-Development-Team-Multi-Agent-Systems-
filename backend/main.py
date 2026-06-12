from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agents.supervisor import pipeline

app = FastAPI(title="AI Software Development Team")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ProjectRequest(BaseModel):
    requirements: str

@app.post("/generate")
async def generate_project(request: ProjectRequest):
    result = pipeline.invoke({
        "requirements": request.requirements,
        "project_plan": "",
        "requirements_spec": "",
        "backend_code": "",
        "frontend_code": "",
        "review_report": "",
        "test_code": ""
    })
    return {
        "project_plan": result["project_plan"],
        "requirements_spec": result["requirements_spec"],
        "backend_code": result["backend_code"],
        "frontend_code": result["frontend_code"],
        "review_report": result["review_report"],
        "test_code": result["test_code"]
    }

@app.get("/")
def root():
    return {"message": "AI Dev Team API running"}