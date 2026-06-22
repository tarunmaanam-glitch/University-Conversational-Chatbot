from contextlib import ExitStack
from langgraph.checkpoint.sqlite import SqliteSaver
 
DB_PATH = "university_memory.db"
 
_stack = ExitStack()
 
memory = _stack.enter_context(
    SqliteSaver.from_conn_string(DB_PATH)
)
