from langgraph.graph import StateGraph
from schemas.graph_state import State
from agents.evaluator import evaluate_fit
from agents.input_handler import read_file
from agents.jd_parser import parse_job_description
from agents.resume_parser import parse_resume
from agents.web_searcher import search_candidate


graph = StateGraph(State)
graph.add_node("InputHandler", read_file)
graph.add_node("WebSearch", search_candidate)
graph.add_node("ResumeParser", parse_resume)
graph.add_node("JDParser", parse_job_description)
graph.add_node("Evaluator", evaluate_fit)

graph.set_entry_point("InputHandler")
graph.add_edge("InputHandler", "ResumeParser")
graph.add_edge("InputHandler", "WebSearch")
graph.add_edge("InputHandler", "JDParser")
graph.add_edge("ResumeParser", "Evaluator")
graph.add_edge("JDParser", "Evaluator")
graph.add_edge("WebSearch", "Evaluator")
graph.set_finish_point("Evaluator")

graph_app = graph.compile()
