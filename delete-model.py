import json
import sys
import openai
import os
from dotenv import load_dotenv
import openai

load_dotenv()
OPENAI_API_KEY = os.getenv("API_KEY")

openai.api_key = OPENAI_API_KEY

openai.models.delete("ft:gpt-3.5-turbo-0613:personal:tlc-ft:8iI8DX4v")
openai.models.delete("ft:gpt-3.5-turbo-0613:personal:tlc-ft:8iGRxihU")
openai.models.delete("ft:gpt-3.5-turbo-0613:personal:tlc-ft:8iGRtr5p")
openai.models.delete("ft:gpt-3.5-turbo-0613:personal:tlc-ft:8iGO6xFl")