"""LangGraph workflow: search -> analyze -> match -> draft -> approval -> track."""
from typing import TypedDict

from langgraph.graph import END, START, StateGraph


class State(TypedDict, total=False):
    candidate: dict
    jobs: list
    shortlisted: list
    approved: bool


def search(state: State) -> State:
    return {"jobs": state.get("jobs", [])}


def analyze_and_match(state: State) -> State:
    return {"shortlisted": state.get("jobs", [])}


def prepare_draft(state: State) -> State:
    return state


def approval(state: State) -> State:
    # Wire up checkpointing / interrupt here so execution pauses for the user.
    return state


def track(state: State) -> State:
    return state


def route_after_approval(state: State) -> str:
    return "track" if state.get("approved") else END


def build_graph():
    g = StateGraph(State)
    g.add_node("search", search)
    g.add_node("match", analyze_and_match)
    g.add_node("draft", prepare_draft)
    g.add_node("approval", approval)
    g.add_node("track", track)
    g.add_edge(START, "search")
    g.add_edge("search", "match")
    g.add_edge("match", "draft")
    g.add_edge("draft", "approval")
    g.add_conditional_edges("approval", route_after_approval)
    g.add_edge("track", END)
    return g.compile()
