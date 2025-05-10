from schemas.graph_state import State
from .llms import GoogleLLM, llm


def parse_job_description(state: State):
    jd_text = state["job_desc"]
    prompt = f"""Parse this job description and extract:
    - Core Skills
    - Required Experience
    - Preferred Qualifications
    - Domain/Industry

    Job Description:
    {jd_text}
    """
    jd = llm.predict(prompt)
    return {"job_description_parsed": jd}
