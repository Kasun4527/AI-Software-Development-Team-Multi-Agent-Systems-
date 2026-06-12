from langchain_core.messages import HumanMessage
from services.llm import llm

def backend_developer_agent(state: dict) -> dict:
    requirements_spec = state["requirements_spec"]
    project_plan = state["project_plan"]

    prompt = f"""
You are a senior Backend Developer. Write production-ready Python FastAPI code.

Project Plan:
{project_plan}

Requirements Specification:
{requirements_spec}

Your tasks:
1. Write complete FastAPI application code
2. Include all API endpoints defined in the spec
3. Include proper data models using Pydantic
4. Include error handling
5. Include CORS middleware
6. Add comments to explain the code
7. Structure the code properly with routers if needed

Return the COMPLETE backend code with filename headers like:
### main.py
<code here>

### models.py
<code here>

Make sure the code is complete and runnable.
"""
    response = llm.invoke([HumanMessage(content=prompt)])
    print("\n✅ Backend Developer done")
    return {**state, "backend_code": response.content}