def greet(firstname: str, lastname: str, lang: str = 'en') -> str:
    if lang == 'en':
        return f'Hello, {firstname} {lastname}'
    elif lang =='es':
        return f'Hola, {firstname} {lastname}'
    else:
        raise UnsupportedLanguageExceptions