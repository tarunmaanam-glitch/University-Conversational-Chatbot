from langchain_core.messages import AIMessage
from utilities.llm import llm
from knoledge_base.hostel_kb import HOSTEL_KB
def hostel_agent(state):
    question=state["messages"][-1].content
    context = "\n".join(HOSTEL_KB.values())

    result = llm.invoke(
        f"""
        Context:
        {context}

        Question:
        {question}
        """
    )
    return {
        **state,
        "messages": [
            AIMessage(content=result.content)
        ]
    }