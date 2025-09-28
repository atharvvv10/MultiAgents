from src.api_client import ask_gemini

def handle_command(command: str):
    if command.lower().startswith("summarize "):
        text = command.replace("summarize ", "")
        return ask_gemini(f"Summarize this text: {text}")

    if command.lower().startswith("question "):
        question = command.replace("question ", "")
        return ask_gemini(f"Answer this: {question}")

    return ask_gemini(command)  # fallback → general chat
 
