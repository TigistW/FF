import openai
from dotenv import load_dotenv
import os
def chat():
    load_dotenv()
    
    openai.api_key = os.getenv("OPENAI_KEY")
    conversation = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What's the weather like in africa?"},
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use the appropriate model name
        messages=conversation
    )
    assistant_reply = response['choices'][0]['message']['content']
    # print(assistant_reply)
    return assistant_reply