import os
from config import MAX_CHARS


def get_file_content(working_directory, file_path):
    try:
        file_path = os.path.abspath(os.path.join(working_directory, file_path))
        if not file_path.startswith(os.path.abspath(working_directory)):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        file_content_string = ""
        with open(file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if len(file_content_string) >= MAX_CHARS:
                file_content_string += (
                    f'[...File "{file_path}" truncated at 10000 characters]'
                )
        return file_content_string
    except Exception as e:
        print(f"Error: {e}")
