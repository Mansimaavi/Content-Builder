import wikipedia

def search_wikipedia(query: str) -> str:
    try:
        return wikipedia.summary(query, sentences=3)
    except Exception:
        return "No relevant information found."
