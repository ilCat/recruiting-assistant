from schemas.graph_state import State
from .llms import llm


def evaluate_fit(state: State):
    candidate_data = state["candidate_data_parsed"]
    job_data = state["job_description_parsed"]
    web_search = state["web_search"]
    prompt = f"""Compare candidate profile against job description with the following criteria, andd parse the output:
    - Core skills
    - Relevant experience
    - Industry/domain relevance
    - Preferred qualifications

    Candidate:
    {candidate_data}
    Relevant public information about the candidate:
    {web_search}

    Job:
    {job_data}

    Deliver de Output in JSON format
    Output:
    - Fit Score: 'Strong Fit', 'Moderate Fit', or 'Not a Fit'
    - Comparison Matrix
    - Justification
    """

    result = llm.predict(prompt)
    return {"result": result}
