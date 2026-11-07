import wikipedia

wikipedia.set_lang("en")


def search_wiki(query: str):
  try:
    search_results = wikipedia.search(query, results=3)

    if not search_results:
      return "No results found on Wikipedia."

    page_title = search_results[0]

    summary = wikipedia.summary(page_title, sentences=3)

    return summary

  except wikipedia.exceptions.DisambiguationError as e:
    return f"Multiple results found. Be more specific: {e.options[:5]}"
  except wikipedia.exceptions.PageError:
    return "The page could not be found."
  except Exception as e:
    return f"An error occurred: {e}"