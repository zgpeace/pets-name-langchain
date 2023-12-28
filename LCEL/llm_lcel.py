from langchain.llms import OpenAI
from langchain_core.runnables import RunnablePassthrough
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

prompt = ChatPromptTemplate.from_template(
    "Tell me a short joke about {topic}"
)
output_parser = StrOutputParser()

llm = OpenAI(model="gpt-3.5-turbo-instruct")
llm_chain = (
    {"topic": RunnablePassthrough()} 
    | prompt
    | llm
    | output_parser
)

response = llm_chain.invoke("ice cream")
print('response >> ', response)