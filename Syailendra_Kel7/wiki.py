import wikipedia
from colorama import Fore, Style

class WikipediaFetcher:
    def __init__(self):
        pass

    def get_wikipedia_page(self, page_title, language='id'):
        wikipedia.set_lang(language)
        try:
            page = wikipedia.page(page_title)
            page_info = {
                "title": page.title,
                "summary": page.summary,
                "full_url": page.url,
                "sections": [section for section in page.sections],
                "categories": page.categories
            }
            return page_info
        except wikipedia.exceptions.DisambiguationError as e:
            return f"Kesalahan disambiguasi: {e.options}"
        except wikipedia.exceptions.PageError:
            return f"Halaman '{page_title}' tidak ada di Wikipedia bahasa {language}."
        except Exception as e:
            return f"Terjadi kesalahan: {e}"
