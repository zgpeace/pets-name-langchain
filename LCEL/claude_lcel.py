from langchain.llms import OpenAI
from langchain_core.runnables import RunnablePassthrough
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain.chat_models import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

prompt = ChatPromptTemplate.from_template(
    "Tell me a short joke about {topic}"
)
output_parser = StrOutputParser()

anthropic = ChatAnthropic(model="claude-2")
anthropic_chain = (
    {"topic": RunnablePassthrough()} 
    | prompt 
    | anthropic
    | output_parser
)

anthropic_chain.invoke("ice cream")