import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

verbose = False

args = sys.argv
if len(args) < 2:
    sys.exit("Error: A prompt must be provided")

if "--verbose" in args:
    verbose = True
    args.remove("--verbose")

messages = [types.Content(role="user", parts=[types.Part(text=args[1])]),]

response = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages,)

if verbose:
    print(f"User prompt: {args[1]}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

print(response.text)
