from langchain_core.runnables import ConfigurableField
from langchain_core.runnables import RunnablePassthrough
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

from langchain.globals import set_debug

set_debug(True)

prompt = ChatPromptTemplate.from_template(
    "Tell me a short joke about {topic}"
)
output_parser = StrOutputParser()
model = ChatOpenAI(model="gpt-3.5-turbo")
llm = OpenAI(model="gpt-3.5-turbo-instruct")

configurable_model = model.configurable_alternatives(
    ConfigurableField(id="model"), 
    default_key="chat_openai", 
    openai=llm,
)
configurable_chain = (
    {"topic": RunnablePassthrough()} 
    | prompt 
    | configurable_model 
    | output_parser
)

ice_response = configurable_chain.invoke(
    "ice cream", 
    config={"model": "openai"}
)
print('ice_response >> ', ice_response)

stream = configurable_chain.stream(
    "spaghetti", 
    config={"model": "chat_openai"}
)
for chunk in stream:
    print(chunk, end="", flush=True)

# response = configurable_chain.batch(["ice cream", "spaghetti", "dumplings"])
# response = configurable_chain.batch(["ice cream", "spaghetti"])
# print('ice cream, spaghetti, dumplings, response >> ', response)

# await configurable_chain.ainvoke("ice cream")


# async def main():
#     await configurable_chain.ainvoke("ice cream")

# import asyncio
# asyncio.run(main())