from typing import List

from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.schema import BaseOutputParser
from langserve import add_routes
from dotenv import load_dotenv  

load_dotenv()  

# 1. Chain definition
class CommaSeparatedListOutputParser(BaseOutputParser[List[str]]):
    """Parse the output of an LLM call to a comma-separated list."""


    def parse(self, text: str) -> List[str]:
        """Parse the output of an LLM call."""
        return text.strip().split(", ")

template = """你是一个有帮助的助手，可以生成逗号分隔的列表。
用户将传入一个类别，你应该生成该类别中的5个对象的逗号分隔列表。
只返回逗号分隔的列表，不要其他内容。"""
human_template = "{text}"

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", template),
    ("human", human_template),
])
category_chain = chat_prompt | ChatOpenAI() | CommaSeparatedListOutputParser()
# response = category_chain.invoke({"text": "颜色"})
# print('colors >> ', response)
# >> ['red', 'blue', 'green', 'yellow', 'orange']

# 2. App definition
app = FastAPI(
  title="LangChain Server",
  version="1.0",
  description="A simple API server using LangChain's Runnable interfaces",
)

# 3. Adding chain route
add_routes(
    app,
    category_chain,
    path="/category_chain",
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)