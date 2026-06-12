from langchain_core.messages import HumanMessage
from services.llm import llm

def frontend_developer_agent(state: dict) -> dict:
    requirements_spec = state["requirements_spec"]
    backend_code = state["backend_code"]

    prompt = f"""
You are a senior Frontend Developer. Write production-ready React + Tailwind CSS code.

Requirements Specification:
{requirements_spec}

Backend Code (for API reference):
{backend_code}

Your tasks:
1. Write complete React components
2. Connect to the FastAPI backend APIs
3. Use Tailwind CSS for styling
4. Include proper state management with useState/useEffect
5. Include loading states and error handling
6. Make the UI clean and professional

Return the COMPLETE frontend code with filename headers like:
### App.jsx
<code here>

### components/ComponentName.jsx
<code here>

Make sure all API calls match the backend endpoints exactly.
"""
    response = llm.invoke([HumanMessage(content=prompt)])
    print("\n✅ Frontend Developer done")
    return {**state, "frontend_code": response.content}