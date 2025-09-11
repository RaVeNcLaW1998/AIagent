import os
from google.genai import types

def write_file(working_directory, file_path, content):
    try:
        file_path = os.path.abspath(os.path.join(working_directory, file_path))
        if not file_path.startswith(os.path.abspath(working_directory)):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        # create file path if it doesnt exist
        parent_dir = os.path.dirname(file_path)
        if not os.path.isdir(parent_dir):
            try:
                os.makedirs(parent_dir)
            except Exception as e:
                return f"Error : Could not create parent directory :{parent_dir} = {e}"

        # writing contents into the file
        with open(file_path, "w") as f:
            f.write(content)
        return (
            f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        )
    except Exception as e:
        return f"Failed to write to file: {file_path} {e}"
    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Overwrites an existing file or writes to a new file if it doesn't exist (and creates required parent directory safely), constrainted to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path of the file to write, relative to the working directory",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The contents as a string to write to the file.",
            ),
        },
    ),
)
