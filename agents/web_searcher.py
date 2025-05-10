from langchain_community.tools import DuckDuckGoSearchRun
from schemas.graph_state import State
from .llms import GoogleLLM, llm

search = DuckDuckGoSearchRun()


def search_candidate(state: State):
    candidate = state["candidate_name"]

    queries = {
        "github": f'"{candidate}" site:github.com -gist.github.com',
        "blog": f'"{candidate}" blog OR article OR post site:medium.com OR site:dev.to OR site:hashnode.dev',
        "conference": f'"{candidate}" conference OR speaker OR talk OR keynote OR presentation',
        "news": f'"{candidate}" interview OR quoted OR profile OR feature site:bbc.com OR site:cnn.com OR site:reuters.com OR site:nytimes.com',
        "social": f'"{candidate}" site:twitter.com OR site:stackoverflow.com',
    }

    try:
        results = {key + "_results": search.run(q) for key, q in queries.items()}

        prompt = f"Act as a technical recruiter evaluating a candidate for a job position. Use the following search results to create a breaf resume of the relevant info about the candidate. Here you are the search results: {results}"
        resume = llm.predict(prompt)
        return {"web_search": resume}
    except:
        print("Request rate limit rised")
        return {"web_search": "No data found."}
