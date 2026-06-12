from langchain_core.messages import HumanMessage
from services.llm import llm

def requirement_analyst_agent(state: dict) -> dict:
    requirements = state["requirements"]
    project_plan = state["project_plan"]

    prompt = f"""
You are a senior Requirement Analyst at a software company.

User Requirements:
{requirements}

Project Plan:
{project_plan}

Your tasks:
1. Define detailed functional requirements
2. Define non-functional requirements
3. Define API endpoints with request/response format
4. Define database schema if needed
5. Define UI/UX requirements for each page
6. Identify potential edge cases and risks

Return a detailed requirements specification document.
"""
    response = llm.invoke([HumanMessage(content=prompt)])
    print("\n✅ Requirement Analyst done")
    return {**state, "requirements_spec": response.content}