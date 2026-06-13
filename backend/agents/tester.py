from langchain_core.messages import HumanMessage
from services.llm import llm

def tester_agent(state: dict) -> dict:
    backend_code = state["backend_code"][:3500]
    requirements_spec = state["requirements_spec"][:1000]
    review_report = state["review_report"][:1500]

    prompt = f"""
You are a senior QA Engineer. Write tests for this code.

Requirements (summary):
{requirements_spec}

Backend Code (truncated):
{backend_code}

Review Report:
{review_report}

Write:
### test_main.py
<pytest code for API endpoints, happy path + edge cases + error handling>

### Test Plan
<list of test scenarios>
"""
    response = llm.invoke([HumanMessage(content=prompt)])
    print("\n✅ Tester done")
    return {**state, "test_code": response.content}