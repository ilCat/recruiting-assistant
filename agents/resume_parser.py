from schemas.graph_state import State
from .llms import GoogleLLM, llm


def parse_resume(state: State):
    text = state["candidate_resume"]
    prompt = f"""Extract structured resume data: Education, Work Experience, Skills, Certifications, Publications, Projects.

    Resume:
    {text}
    """
    resume = llm.predict(prompt)
    return {"candidate_data_parsed": resume}
