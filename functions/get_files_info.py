import os

def get_files_info(working_directory, directory="."):
    full_path = os.path.join(working_directory, directory)
    result = ""
    if directory == ".":
        result = "Result for current directory:\n"
    else:
        result = f"Result for '{directory}' directory:\n"
    try:
        if os.path.commonpath([os.path.abspath(working_directory)]) != os.path.commonpath([os.path.abspath(working_directory), os.path.abspath(full_path)]):
            return result + f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if os.path.isfile(full_path):
            return result + f'Error: "{directory}" is not a directory'
        files = os.listdir(full_path)
        for f in files:
            result += f"- {f}: file_size={os.path.getsize(full_path + "/" + f)} bytes, is_dir={os.path.isdir(full_path + "/" + f)}\n"
        return result
    except Exception as e:
        return f'Error: {str(e)}'
