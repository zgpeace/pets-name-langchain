from langchain.llms import OpenAI
from langchain_core.runnables import RunnablePassthrough
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()
prompt = ChatPromptTemplate.from_template("tell me a joke about {topic}")
chain = prompt | model

# The input schema of the chain is the input schema of its first part, the prompt.
chain_iput = chain.input_schema.schema()
print('chain_iput >> ', chain_iput)

prompt_input = prompt.input_schema.schema()
print('prompt_input >> ', prompt_input)

model_input = model.input_schema.schema()
print('model_input >> ', model_input)

# The output schema of the chain is the output schema of its last part, in this case a ChatModel, which outputs a ChatMessage
chain_output = chain.output_schema.schema()
print('chain_output >> ', chain_output)

response = chain.invoke({"topic": "bears"})
print('response >> ', response)
