import fitz
def extract_text_from_pdf(path:str):
    docs = fitz.open(path)
    full_text = ""
    for page in docs:
        full_text += page.get_text() + "\n"
    return full_text