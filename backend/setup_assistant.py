import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

file = openai.files.create(
    file=open("data/combined_emails.txt", "rb"),
    purpose='assistants'
)

assistant = openai.beta.assistants.create(
    name="Ralph",
    instructions="You are Ralph, the Field Game master at Eton...",
    tools=[{"type": "retrieval"}],
    model="gpt-4-1106-preview",
    file_ids=[file.id]
)

print("✅ Assistant created. ID:", assistant.id)
