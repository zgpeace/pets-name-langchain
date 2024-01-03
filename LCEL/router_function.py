from langchain_core.runnables import RunnablePassthrough
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_core.runnables import RunnableBranch

from dotenv import load_dotenv
load_dotenv()

from langchain.globals import set_debug
set_debug(True)

chain = (
    PromptTemplate.from_template(
        """Given the user question below, classify it as either being about `LangChain`, `ChatGPT`, or `Other`.

Do not respond with more than one word.

<question>
{question}
</question>

Classification:"""
    )
    | ChatOpenAI()
    | StrOutputParser()
)

# response = chain.invoke({"question": "how do I call ChatGPT ?"})
# print('response >> ', response)

langchain_chain = (
    PromptTemplate.from_template(
        """You are an expert in langchain. \
Always answer questions starting with "As Harrison Chase told me". \
Respond to the following question:

Question: {question}
Answer:"""
    )
    | ChatOpenAI()
)
chatgpt_chain = (
    PromptTemplate.from_template(
        """You are an expert in ChatGPT. \
Always answer questions starting with "As Sam Altman told me". \
Respond to the following question:

Question: {question}
Answer:"""
    )
    | ChatOpenAI()
)
general_chain = (
    PromptTemplate.from_template(
        """Respond to the following question:

Question: {question}
Answer:"""
    )
    | ChatOpenAI()
)

def route(info):
    if "chatgpt" in info["topic"].lower():
        return chatgpt_chain
    elif "langchain" in info["topic"].lower():
        return langchain_chain
    else:
        return general_chain

full_chain = {"topic": chain, "question": lambda x: x["question"]} | RunnableLambda(
    route
)

response = full_chain.invoke({"question": "how do I use chatgpt?"})
print('response >> ', response)
