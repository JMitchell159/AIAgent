import os

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
        