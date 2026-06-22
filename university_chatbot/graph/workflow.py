# workflow.py
from langgraph.graph import StateGraph, END
from graph.state import UniversityState
from graph.router import agent_router

from nodes.extractor_profile import extractor_profile
from nodes.classifiers import classify_query

from agents.academic_agent import academic_agent
from agents.admission_agent import admission_agent
from agents.placement_agent import placement_agent
from agents.hostel_agent import hostel_agent
from agents.memory_agent import memory_agent

from memory.checkpoint import memory
def build_graph():
    builder = StateGraph(UniversityState)
    builder.add_node("extract_profile", extractor_profile)
    builder.add_node("classify_query", classify_query)
 
    builder.add_node("admission", admission_agent)
    builder.add_node("hostel", hostel_agent)
    builder.add_node("placement", placement_agent)
    builder.add_node("academic", academic_agent)
    builder.add_node("memory", memory_agent)
 
    builder.set_entry_point("extract_profile")
    builder.add_edge(
        "extract_profile",
        "classify_query"
    )
 
    builder.add_conditional_edges(
        "classify_query",
        agent_router,
        {
            "admission": "admission",
            "hostel": "hostel",
            "placement": "placement",
            "academic": "academic",
            "memory": "memory"
        }
    )
 
    builder.add_edge("admission", END)
    builder.add_edge("hostel", END)
    builder.add_edge("placement", END)
    builder.add_edge("academic", END)
    builder.add_edge("memory", END)
 
    return builder.compile(
        checkpointer=memory
    )
