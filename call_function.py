from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.run_python_file import run_python_file
from functions.write_file import write_file
from google import genai
from google.genai import types

call_dict = {"get_file_content": get_file_content, "get_files_info": get_files_info, "run_python_file": run_python_file, "write_file": write_file}

def call_function(call, verbose=False):
    if verbose:
        print(f"Calling function: {call.name}({call.args})")
    else:
        print(f" - Calling function: {call.name}")
    if call.name in call_dict:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=call.name,
                    response={"result": call_dict[call.name](working_directory="./calculator", **call.args)},
                )
            ],
        )
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=call.name,
                response={"error": f"Unknown function: {call.name}"},
            )
        ],
    )
