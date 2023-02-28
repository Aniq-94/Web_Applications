supported_languages = list[str] = ['en','es']

class UnsupportedLanguageException(Exception):
    def __init__(self, lang: str) -> None:
        super().__init__(*args)