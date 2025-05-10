from typing_extensions import TypedDict


class State(TypedDict):
    files: dict[str]
    candidate_name: str
    candidate_resume: str
    candidate_link: str
    candidate_data_parsed: str
    job_desc: str
    job_description_parsed: str
    web_search: str
    result: str


class fileClass:
    def __init__(self, filename: str):
        self.filename = filename
