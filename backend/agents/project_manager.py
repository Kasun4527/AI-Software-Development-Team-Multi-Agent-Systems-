from langchain_core.messages import HumanMessage
from services.llm import llm

def project_manager_agent(state: dict) -> dict:
    requirements = state["requirements"]

    prompt = f"""
You are a senior Project Manager at a software company.

User Requirements:
{requirements}

Your tasks:
1. Analyze the requirements
2. Break down into clear development tasks
3. Decide the tech stack (use Python FastAPI for backend, React for frontend)
4. Create a development plan with phases
5. Define clear deliverables for each agent:
   - Backend Developer tasks
   - Frontend Developer tasks
   - What APIs need to be built
   - What UI components need to be built

Return a detailed, structured project plan.
"""
    response = llm.invoke([HumanMessage(content=prompt)])
    print("\n✅ Project Manager done")
    return {**state, "project_plan": response.content}