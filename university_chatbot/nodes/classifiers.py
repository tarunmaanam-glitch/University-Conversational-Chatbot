from utilities.llm import llm
 
def classify_query(state):
    query = state["messages"][-1].content.lower()
 
    if "what is my name" in query:
        state["query_category"] = "memory"
        return state
 
    elif any(word in query for word in [
        "fee", "fees", "admission", "course",
        "eligibility", "application", "entrance",
        "b.tech", "m.tech"
    ]):
        state["query_category"] = "admission"
 
    elif any(word in query for word in [
        "hostel", "room", "mess",
        "wifi", "curfew", "facility"
    ]):
        state["query_category"] = "hostel"
 
    elif any(word in query for word in [
        "placement", "package", "salary",
        "company", "companies", "internship"
    ]):
        state["query_category"] = "placement"
 
    elif any(word in query for word in [
        "attendance", "gpa", "grade",
        "semester", "credit", "backlog"
    ]):
        state["query_category"] = "academic"
 
    else:
        state["query_category"] = "academic"
 
    print(f"\n[ROUTED TO] {state['query_category'].upper()}")
 
    return state

    