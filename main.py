import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file
import sys
from config import SYSTEM_PROMPT

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

available_functions = types.Tool(function_declarations=[schema_get_files_info, schema_get_file_content, schema_run_python_file, schema_write_file,])

verbose = False

args = sys.argv
if len(args) < 2:
    sys.exit("Error: A prompt must be provided")

if "--verbose" in args:
    verbose = True
    args.remove("--verbose")

messages = [types.Content(role="user", parts=[types.Part(text=args[1])]),]

response = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages, config=types.GenerateContentConfig(tools=[available_functions], system_instruction=SYSTEM_PROMPT))

if verbose:
    print(f"User prompt: {args[1]}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

print(response.text)
for call in response.function_calls:
    print(f"Calling function: {call.name}({call.args})")
