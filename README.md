# 🤖 Autonomous AI Recruiting Assistant with LangGraph

This project implements an **autonomous AI recruiting assistant** using LangGraph. Given a candidate’s name, resume (PDF or DOCX), and a job description(String or DOCX), the assistant gathers public web data, parses and analyzes the resume, compares qualifications to the job requirements, and outputs a structured fit assessment with reasoning.

---

## Features

- **Autonomous Web Search** for candidate’s public data (GitHub, blogs, StackOverflow, etc.)
- **Resume Parsing** (education, experience, skills, certifications)
- **Job Description Parsing** (required skills, experience, qualifications)
- **Fit Evaluation Engine** with structured comparison matrix
- **LangGraph Orchestration** for modular and scalable architecture

###
- **Inputs** The agent accept:
* candidate_name: (string)

* resume_file: (PDF or DOCX)

* job_description: (string or DOCX)

---

## Steps to use

1. Load CV file and JD file to colab

2. Set env variable 'GOOGLE_API_KEY' in the compose.yaml

3. Build and run container 
    ```bash
    docker-compose up --build 
    ```
4. Go to 

        http://0.0.0.0:8000/docs

5. You can test the aplication on 2 ways:

* Test the aplication with the example files(Alexis_Silva_Resume_SD.pdf, JD.docx) in the content folder using the endpoints '/test' or '/test-all-info' with no arguments

* Test the aplication adding the name, CV and JD manually using the endpoint  '/evaluate-candidate'



