import os
from google import genai
from google.genai import types

def write_file(working_directory, file_path, content):
    try:
        full_path = os.path.join(working_directory, file_path)
        if os.path.commonpath([os.path.abspath(working_directory)]) != os.path.commonpath([os.path.abspath(working_directory), os.path.abspath(full_path)]):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        path_split = full_path.split("/")
        str_path = path_split[0]
        for path in path_split[1:-1]:
            if not os.path.exists(str_path):
                os.mkdir(str_path)
            str_path += "/" + path
        with open(full_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: {str(e)}'

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to write content to, relative to the working directory. The file will be created if it does not exist, and it will overwrite the content in existing files. If an empty string is provided, an error is thrown.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file. If an empty string is provided, it will create a blank file or delete the contents of an existing file.",
            )
        }
    )
)
        