from typing import List, Annotated, Union
from fastapi import FastAPI, HTTPException, status, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import asyncio
from utils.starting_point import starting_point
from graphs.graph_builder import graph_app
import json
import fitz
from schemas.graph_state import fileClass

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def read_root():
    return {"Hi: Welcome to recruiting-assistant Server"}


@app.get(
    "/test",
)
async def get_results_test():
    response = graph_app.invoke(
        starting_point(
            "Alexis Silva", "./content/Alexis_Silva_Resume_SD.pdf", "./content/JD.docx"
        )
    )

    return response["result"]


@app.get(
    "/test-all-info",
)
async def test_all_info():
    response = graph_app.invoke(
        starting_point(
            "Alexis Silva", "./content/Alexis_Silva_Resume_SD.pdf", "./content/JD.docx"
        )
    )

    return response


@app.post(
    "/evaluate-candidate",
)
async def evaluate_candidate(
    name: str,
    CV_file: UploadFile = File(...),
    JD_file: Union[str, UploadFile] = "",
):
    CV_file_content = await CV_file.read()
    JD_file_content = None
    if type(JD_file) == str:
        JD_file = fileClass("NA")
        JD_file.filename = "NA"
        JD_file_content = JD_file
    else:
        JD_file_content = await JD_file.read()

    response = graph_app.invoke(
        starting_point(
            name,
            {"filename": CV_file.filename, "content": CV_file_content},
            {"filename": JD_file.filename, "content": JD_file_content},
        )
    )

    # return {
    #     "candidate_name": response["candidate_name"],
    #     "candidate_data_parsed": response["candidate_data_parsed"],
    #     "job_description_parsed": response["job_description_parsed"],
    #     "result": response["result"],
    # }
    return response["result"]
