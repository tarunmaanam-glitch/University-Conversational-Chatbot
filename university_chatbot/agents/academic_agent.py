from langchain_core.messages import AIMessage
from utilities.llm import llm
from knoledge_base.academic_kb import ACADEMIC_KB
def academic_agent(state):
    question=state["messages"][-1].content
    context = "\n".join(ACADEMIC_KB.values())

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
