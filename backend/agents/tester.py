from langchain_core.messages import HumanMessage
from services.llm import llm

def tester_agent(state: dict) -> dict:
    backend_code = state["backend_code"]
    frontend_code = state["frontend_code"]
    requirements_spec = state["requirements_spec"]
    review_report = state["review_report"]

    prompt = f"""
You are a senior QA Engineer. Write comprehensive tests for the following code.

Requirements Specification:
{requirements_spec}

Backend Code:
{backend_code}

Code Review Report:
{review_report}

Your tasks:
1. Write Python pytest test cases for all API endpoints
2. Include happy path tests
3. Include edge case tests
4. Include error handling tests
5. Write a test plan document
6. List all test scenarios covered
7. Identify any untestable areas and why

Return:
### test_main.py
<pytest code here>

### Test Plan
<test plan document>
"""
    response = llm.invoke([HumanMessage(content=prompt)])
    print("\n✅ Tester done")
    return {**state, "test_code": response.content}