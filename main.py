from typing import TypedDict
from langgraph.graph import StateGraph


class AgentState(TypedDict):
    name: str
    age: int
    message: str


def first_node(state: AgentState) -> AgentState:
    state["message"] = f"Hi, {state['name']}!"
    return state


def second_node(state: AgentState) -> AgentState:
    state["message"] = state["message"] + f" You are {state['age']} years old."
    return state


graph = StateGraph(AgentState)

graph.add_node("first_node", first_node)
graph.add_node("second_node", second_node)
graph.set_entry_point("first_node")
graph.add_edge("first_node", "second_node")
graph.set_finish_point("second_node")

app = graph.compile()

result = app.invoke({"name": "Jonah", "age": 20})

print("Result:", result["message"])

# Result: Hi, Jonah! You are 20 years old.
