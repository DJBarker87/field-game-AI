from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
CORS(app)

ASSISTANT_ID = os.getenv("ASSISTANT_ID")

@app.route("/ask-ralph", methods=["POST"])
def ask_ralph():
    data = request.get_json()
    thread = openai.beta.threads.create()
    openai.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=data.get("question", "")
    )
    response = openai.beta.threads.runs.create_and_poll(
        thread_id=thread.id,
        assistant_id=ASSISTANT_ID
    )
    answer = response.latest_message().content[0].text.value
    return jsonify({"answer": answer})

if __name__ == "__main__":
    print("✅ Ralph is awake and listening on port 5000...")
    app.run(debug=True)
