from langchain_google_genai import ChatGoogleGenerativeAI
import os

# os.environ["GOOGLE_API_KEY"] = "AIzaSyDzXfFOES7LPfJR1JOt_exPXg20uYLK_Cw"

# googllm = ChatGoogleGenerativeAI(
#     model="gemini-2.0-flash",
#     temperature=0,
#     max_tokens=None,
#     timeout=None,
#     max_retries=2,
# )


class GoogleLLM(ChatGoogleGenerativeAI):
    pass
    # def __init__(self, model="gemini-2.0-flash", temperature=0):

    #     super().__init__(
    #         self,
    #         model=model,
    #         temperature=temperature,
    #         max_retries=2,
    #     )


llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)
