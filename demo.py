import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())
openai_api_key = os.environ["OPENAI_API_KEY"]


# Completion model

from langchain_openai import OpenAI

llmModel = OpenAI()


for chunk in llmModel.stream(
    "Tell me one fun fact about the Kennedy family.i need detail response"
):
    print(chunk, end="", flush= True)