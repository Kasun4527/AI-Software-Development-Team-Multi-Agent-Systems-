from langchain_core.messages import HumanMessage
from services.llm import llm

def code_reviewer_agent(state: dict) -> dict:
    backend_code = state["backend_code"]
    frontend_code = state["frontend_code"]
    requirements_spec = state["requirements_spec"]

    prompt = f"""
You are a senior Code Reviewer. Review the following code thoroughly.

Requirements Specification:
{requirements_spec}

Backend Code:
{backend_code}

Frontend Code:
{frontend_code}

Review for:
1. Bugs and logical errors
2. Security vulnerabilities
3. Missing requirements from the spec
4. Code quality and best practices
5. API contract mismatches between frontend and backend
6. Performance issues
7. Missing error handling

For each issue found:
- Severity: HIGH / MEDIUM / LOW
- Location: which file and what part
- Issue: description
- Fix: how to fix it

Also give an overall score out of 10 and summary.
"""
    response = llm.invoke([HumanMessage(content=prompt)])
    print("\n✅ Code Reviewer done")
    return {**state, "review_report": response.content}