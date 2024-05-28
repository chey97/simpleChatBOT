from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

# Get the API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")
print("API Key:", api_key)

# Initialize the OpenAI client with the API key
client = OpenAI(api_key=api_key)

def chat_with_gpt(prompt):
    # Use the provided prompt for the completion
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,  # Use the provided prompt
            }
        ],
        model="gpt-3.5-turbo",
    )
    return chat_completion.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("Enter a prompt: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break
    
        response = chat_with_gpt(user_input)
        print("Chatbot: ", response)
