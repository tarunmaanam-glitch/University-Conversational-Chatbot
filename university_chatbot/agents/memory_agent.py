from langchain_core.messages import AIMessage
 
def memory_agent(state):
 
    name = state.get("student_name")
 
    if name:
        answer = f"Your name is {name.title()}."
    else:
        answer = "I don't know your name yet."
 
    return {
        **state,
        "messages": [
            AIMessage(content=answer)
        ]
    }