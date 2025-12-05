import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("AIzaSyAR8RNXS6MBbGhEAOrGmptcKkCXoQF7mmw"))
model = genai.GenerativeModel("gemini-2.0-flash-lite")

def answer(question, context):
    prompt = f"Context:\n{context}\n\nQuestion: {question}\n\nAnswer:"
    response = model.generate_content(prompt)
    return response.text
