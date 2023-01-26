import os
import openai
from dotenv import load_dotenv

class ChatGPT:
    def get_response(prompt) -> str:
        load_dotenv()
        openai.api_key = os.getenv("OPENAI_API_KEY")
        get = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=0.9, max_tokens=3000, n=1, presence_penalty=0.1, frequency_penalty=0.1)
        response = get.choices[0].text
        return response