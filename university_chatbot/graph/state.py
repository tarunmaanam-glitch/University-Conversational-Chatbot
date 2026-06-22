from typing import TypedDict,Optional,List,Annotated
from langgraph.graph.message import add_messages


class UniversityState(TypedDict,total=False):
    messages:Annotated[List,add_messages]
    student_name:Optional[str]
    register_no:Optional[str]
    department:Optional[str]


    query_category:str
    kb_context:str