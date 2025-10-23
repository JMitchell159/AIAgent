import os
from config import CHARACTER_LIMIT
from google import genai
from google.genai import types

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

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Retrieves the content of a file, up to a max character limit, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to retrieve content from, relative to the working directory. If an empty string is provided, an error is thrown.",
            ),
        },
    ),
)
