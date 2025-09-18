def preprocess_text(text: str) -> str:
    return text.strip().lower()

def postprocess_text(text: str) -> str:
    return text.capitalize()
