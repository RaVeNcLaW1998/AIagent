import os
from google.genai import types

def get_files_info(working_directory, directory="."):
    try:
        full_path = os.path.abspath(os.path.join(working_directory, directory))

        if not full_path.startswith(os.path.abspath(working_directory)):
            return f'Error: "{directory}" is not a directory in our working directory'

        # list the contents
        final_response = ""
        for content in os.listdir(full_path):
            content_path = os.path.join(full_path, content)
            size = os.path.getsize(content_path)
            is_dir = os.path.isdir(content_path)
            final_response += f"{content}: file_size={size} bytes, is_dir={is_dir}\n"
        return final_response

    except Exception as e:
        print(f"Error: {e}")

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)