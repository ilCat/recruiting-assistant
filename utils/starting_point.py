def starting_point(candidate_name, resume_file, job_description):
    """
    candidate_name : str - name of the candidate
    resume_file : str - path to resume file
    job_description: str - path to resume file or sting of job description
    """

    return {
        "candidate_name": candidate_name,
        "files": {"candidate_resume": resume_file, "job_desc": job_description},
    }
