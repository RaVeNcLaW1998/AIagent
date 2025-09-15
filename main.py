import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types
from config import MODEL
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.write_file import schema_write_file
from functions.run_python_file import schema_run_python_file
from functions.call_function import call_function


def main():
    # get api key from .evn file
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)
   
    # check for prompt
    if len(sys.argv) < 2:
        print("we need a prompt")
        sys.exit(1)
    user_prompt = sys.argv[1]

    # flag to show the token details of the prompt
    verbose_flag = False
    if len(sys.argv) == 3 and sys.argv[2] == "--verbose":
        verbose_flag = True

    
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    
    #list of available functions
    available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_write_file,
        schema_run_python_file,
    ]
    )
    
    system_prompt = """
    You are a helpful AI coding agent.

    When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

    - List files and directories
    - Get contents of the file
    - Write to the python file(create or update)
    - Run the python file with optional arguements

    All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """
    
    # send prompt
    response = client.models.generate_content(
        model= MODEL,
        contents=messages,
        config=types.GenerateContentConfig(tools=[available_functions],system_instruction=system_prompt),
    )

    # print response
    if response is None or response.usage_metadata is None:
        print("response is malformed")
        return
    
    if response.function_calls:
        for function_call_part in response.function_calls:
            function_call_result = call_function(function_call_part,verbose_flag)
            if not function_call_result.parts[0].function_response.response:
                raise Exception("No response form the function call")
            else:
                if verbose_flag:
                    print(f"-> {function_call_result.parts[0].function_response.response}")
                
    else:
        print(response.text)
        
    #print the prompt details
    if verbose_flag:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


main()
