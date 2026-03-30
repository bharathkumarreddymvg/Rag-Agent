from duckduckgo_search import DDGS

def web_search(query: str):
    results = []

    try:
        with DDGS() as ddgs:
            search_results = ddgs.text(query, max_results=5)

            for r in search_results:
                results.append({
                    "content": r.get("body", ""),
                    "source": r.get("href", "")
                })

    except Exception as e:
        print("Web search failed:", e)

    return results