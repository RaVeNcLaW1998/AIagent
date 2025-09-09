import os
from dotenv import load_dotenv
from google import genai
import sys


def main():
    # get api key from .evn file
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    for arg in sys.argv:
        # send prompt
        response = client.models.generate_content(
            model="gemini-2.0-flash-001",
            contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.",
        )

        # print response
        if response is None or response.usage_metadata is None:
            print("response is malformed")
            return
        print(response.text)
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


main()
