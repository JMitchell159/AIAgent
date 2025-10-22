import os
from config import CHARACTER_LIMIT

def get_file_content(working_directory, file_path):
    result = ""
    try:
        full_path = os.path.join(working_directory, file_path)
        if os.path.commonpath([os.path.abspath(working_directory)]) != os.path.commonpath([os.path.abspath(working_directory), os.path.abspath(full_path)]):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(full_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        large = os.path.getsize(full_path) > CHARACTER_LIMIT
        with open(full_path, "r") as f:
            result += f.read(CHARACTER_LIMIT)
        if large:
            result += f'[...File "{file_path}" truncated at {CHARACTER_LIMIT} characters]'
        return result
    except Exception as e:
        return f'Error: {str(e)}'
