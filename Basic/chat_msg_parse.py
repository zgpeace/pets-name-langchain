from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.schema import BaseOutputParser

from dotenv import load_dotenv  
load_dotenv()  

llm = OpenAI(model_name="gpt-3.5-turbo", temperature=0)
chat_model = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

from langchain.schema import HumanMessage

text = "制造彩色袜子的公司取什么好名字呢？"
messages = [HumanMessage(content=text)]

response = llm.invoke(text)
print("string >>", response)
# >> Feetful of Fun

response =  chat_model.invoke(messages)
print("message >>", response)

class NextLineSeparatedListOutputParser(BaseOutputParser):
    """Parse the output of an LLM call to a comma-separated list."""


    def parse(self, text: str):
        """Parse the output of an LLM call."""
        return text.strip().split("\n")

result = NextLineSeparatedListOutputParser().parse(response.content)
print('next line result >> ', result)
# >> ['hi', 'bye']
# >> AIMessage(content="Socks O'Color")
