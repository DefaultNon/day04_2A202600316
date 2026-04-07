import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(
    model="qwen/qwen3.6-plus:free",
    openai_api_key=os.getenv("OPENROUTER_API_KEY"),
    openai_api_base="https://openrouter.ai/api/v1"
)

try:
    print("Sending message to OpenRouter...")
    response = llm.invoke([HumanMessage(content="Xin chào, bạn là ai?")])
    print(f"Response: {response.content}")
except Exception as e:
    print(f"Error: {str(e)}")
