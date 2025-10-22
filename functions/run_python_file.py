import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    try:
        full_path = os.path.join(working_directory, file_path)
        if os.path.commonpath([os.path.abspath(working_directory)]) != os.path.commonpath([os.path.abspath(working_directory), os.path.abspath(full_path)]):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.exists(full_path):
            return f'Error: File "{file_path}" not found.'
        if full_path[-3:] != ".py":
            return f'Error: "{file_path}" is not a Python file.'
    except Exception as e:
        return f'Error: {str(e)}'
    try:
        run = ["uv", "run", file_path]
        if len(args) > 0:
            run += args
        process = subprocess.run(run, timeout=30, capture_output=True, cwd=working_directory, text=True)
        result = ""
        if process.stdout != "":
            result += f"STDOUT: {process.stdout}\n"
        else:
            return f"No output produced."
        if process.stderr != "":
            result += f"STDERR: {process.stderr}\n"
        if process.returncode != 0:
            result += f"Process exited with code {process.returncode}"
        return result
    except Exception as e:
        return f"Error: executing Python file: {e}"
