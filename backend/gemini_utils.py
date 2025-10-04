import google.generativeai as genai
import os, json

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_quiz(text):
    prompt = f"""
    Create a 10-question multiple choice quiz based on these notes.
    Each question should have 4 options and 1 correct answer.
    Format as JSON:
    {{ "quiz": [{{"question": "...", "options": [...], "answer": "..."}}] }}
    Notes: {text}
    """
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return json.loads(response.text)
