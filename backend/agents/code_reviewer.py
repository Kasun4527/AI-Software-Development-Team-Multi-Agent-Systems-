from langchain_core.messages import HumanMessage
from services.llm import llm

def code_reviewer_agent(state: dict) -> dict:
    backend_code = state["backend_code"][:3000]
    frontend_code = state["frontend_code"][:3000]
    requirements_spec = state["requirements_spec"][:1500]

    prompt = f"""
You are a senior Code Reviewer. Review the following code.

Requirements (summary):
{requirements_spec}

Backend Code (truncated):
{backend_code}

Frontend Code (truncated):
{frontend_code}

Review for:
1. Bugs and logical errors
2. Security vulnerabilities
3. API contract mismatches
4. Missing error handling

For each issue: Severity (HIGH/MEDIUM/LOW), Location, Issue, Fix.
Give an overall score out of 10 and summary.
"""
    response = llm.invoke([HumanMessage(content=prompt)])
    print("\n✅ Code Reviewer done")
    return {**state, "review_report": response.content}