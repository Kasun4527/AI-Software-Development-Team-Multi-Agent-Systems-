from langgraph.graph import StateGraph, END
from typing import TypedDict
from agents.project_manager import project_manager_agent
from agents.requirement_analyst import requirement_analyst_agent
from agents.backend_developer import backend_developer_agent
from agents.frontend_developer import frontend_developer_agent
from agents.code_reviewer import code_reviewer_agent
from agents.tester import tester_agent

class DevTeamState(TypedDict):
    requirements: str
    project_plan: str
    requirements_spec: str
    backend_code: str
    frontend_code: str
    review_report: str
    test_code: str

def build_graph():
    graph = StateGraph(DevTeamState)

    graph.add_node("project_manager", project_manager_agent)
    graph.add_node("requirement_analyst", requirement_analyst_agent)
    graph.add_node("backend_developer", backend_developer_agent)
    graph.add_node("frontend_developer", frontend_developer_agent)
    graph.add_node("code_reviewer", code_reviewer_agent)
    graph.add_node("tester", tester_agent)

    graph.set_entry_point("project_manager")
    graph.add_edge("project_manager", "requirement_analyst")
    graph.add_edge("requirement_analyst", "backend_developer")
    graph.add_edge("backend_developer", "frontend_developer")
    graph.add_edge("frontend_developer", "code_reviewer")
    graph.add_edge("code_reviewer", "tester")
    graph.add_edge("tester", END)

    return graph.compile()

pipeline = build_graph()