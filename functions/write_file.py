import os


def write_file(working_directory, file_path, content):
    try:
        file_path = os.path.abspath(os.path.join(working_directory, file_path))
        if not file_path.startswith(os.path.abspath(working_directory)):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        # create file path if it doesnt exist
        parent_dir = os.path.dirname(file_path)
        print(parent_dir)
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
