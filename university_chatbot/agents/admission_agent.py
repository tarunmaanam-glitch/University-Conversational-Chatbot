from langchain_core.messages import AIMessage
from utilities.llm import llm
from knoledge_base.admission import ADMISSION_KB
 
def admission_agent(state):
 
    question = state["messages"][-1].content
 
    context = "\n".join(ADMISSION_KB.values())
 
    prompt = f"""
You are a university admission officer.
 
Use ONLY the information below.
 
Information:
{context}
 
Question:
{question}
 
Answer clearly and accurately.
"""
 
    result = llm.invoke(prompt)
 
    return {
        **state,
        "messages": [
            AIMessage(content=result.content)
        ]
    }