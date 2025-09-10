import os
import subprocess


def run_python_file(working_directory, file_path, args=[]):
    file_path = os.path.abspath(os.path.join(working_directory, file_path))
    abs_working_dir = os.path.abspath(working_directory)
    if not file_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(file_path):
        return f'Error: File "{file_path}" not found.'
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        final_args = ["python3", file_path]
        final_args.extend(args)
        completed_process = subprocess.run(
            final_args, cwd=abs_working_dir, timeout=30, capture_output=True
        )
        if completed_process.stdout or completed_process.stderr:
            final_string = f"STDOUT: {completed_process.stdout} STDERR:{completed_process.stderr} "
        else:
            final_string = "No output produced." 
        if completed_process.returncode != 0:
            final_string += f"Process exited with code {completed_process.returncode}"
        return final_string

    except Exception as e:
        return f"Error: executing Python file: {e}"
    
    