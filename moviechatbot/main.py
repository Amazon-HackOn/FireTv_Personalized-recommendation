import textbase
from textbase.message import Message
from textbase import models
import os
from typing import List

# Load your OpenAI API key
models.OpenAI.api_key = "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"

# Prompt for movie recommendation conversations
MOVIE_PROMPT = """You are chatting with a movie recommendation bot. Please provide me with your preferences, such as your favorite genres, actors, or any specific movie you liked."""

@textbase.chatbot("movie-bot")
def on_message(message_history: List[Message], state: dict = None):
    """Chatbot logic for generating movie recommendation responses"""

    # Extract user messages and concatenate for conversation history
    user_messages = [message.content for message in message_history if message.role == "user"]
    conversation_history = "\n".join(user_messages)

    # Generate GPT-3.5 Turbo response with movie prompt
    bot_response = models.OpenAI.generate(
        system_prompt=MOVIE_PROMPT,
        message_history=message_history,
        model="gpt-3.5-turbo",
    )

    return bot_response, state

# Entry point of the script
if __name__ == "__main__":
    try:
        cli()  # Call the command line interface function
    except KeyboardInterrupt:
        # Handle keyboard interrupt (Ctrl+C)
        print("Keyboard interrupt received. Terminating the server...")
        sys.exit(1)
