from utilities.llm import llm
import json
 
def extractor_profile(state):
    last_msg=state["messages"][-1].content.lower()
 
    #Simple rule based
    if "my name is" in last_msg:
        try:
            name = last_msg.split("my name is")[1].strip().split()[0]
            state["student_name"] = name.title()
        except:
            pass
    prompt = f"""
Extract student information.
 
Message:
{last_msg}
 
Rules:
- If information is missing return null
- Never return 'unknown'
- Return only JSON
 
Format:
 
{{
  "name": null,
  "register_no": null,
  "department": null
}}
"""
    result = llm.invoke(prompt)
 
    try:
        raw = result.content.strip()
 
        start = raw.find("{")
        end = raw.rfind("}") + 1
 
        data = json.loads(raw[start:end])
 
        if data.get("name") and data["name"] != "unknown":
            state["student_name"] = data["name"]
 
        if data.get("register_no") and data["register_no"] != "unknown":
            state["register_no"] = data["register_no"]
 
        if data.get("department") and data["department"] != "unknown":
            state["department"] = data["department"]
 
    except:
        pass
 
    return state