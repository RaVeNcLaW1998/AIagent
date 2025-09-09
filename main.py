import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types


def main():
    # get api key from .evn file
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    if len(sys.argv) < 2:
        print("we need a prompt")
        sys.exit(1)
    user_prompt = sys.argv[1]

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    # send prompt
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
    )

    # print response
    if response is None or response.usage_metadata is None:
        print("response is malformed")
        return
    print(response.text)
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


main()
