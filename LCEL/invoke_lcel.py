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
model = ChatOpenAI(model="gpt-3.5-turbo")
chain = (
    {"topic": RunnablePassthrough()} 
    | prompt
    | model
    | output_parser
)

# response = chain.invoke("ice cream")
# print('response >> ', response)

# for chunk in chain.stream("ice cream"):
#     print(chunk, end="", flush=True)

# response = chain.batch(["ice cream", "spaghetti", "dumplings"])
# print('response >> ', response)

from langchain.globals import set_debug

set_debug(True)

async def main():
    await chain.ainvoke("ice cream")

import asyncio
asyncio.run(main())




