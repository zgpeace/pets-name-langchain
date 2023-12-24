from typing import List

from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import BaseOutputParser
from dotenv import load_dotenv  

load_dotenv()  

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
chain = chat_prompt | ChatOpenAI() | CommaSeparatedListOutputParser()
response = chain.invoke({"text": "颜色"})
print('colors >> ', response)
# >> ['red', 'blue', 'green', 'yellow', 'orange']