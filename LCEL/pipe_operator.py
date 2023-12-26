from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv  

load_dotenv()  

prompt = ChatPromptTemplate.from_template("给我讲个关于{topic}的短篇笑话。")
model = ChatOpenAI()
output_parser = StrOutputParser()

chain = prompt | model | output_parser

# respose = chain.invoke({"topic": "冰淇淋"})
# print('joke >> ', respose)

prompt_value = prompt.invoke({"topic": "ice cream"})
print('prompt_value >> ', prompt_value)

message = prompt_value.to_messages()
print('message >> ', message)

string = prompt_value.to_string()
print('string >> ', string)

model_message = model.invoke(prompt_value)
print('model_message >> ', model_message)

# from langchain.llms import OpenAI

# llm = OpenAI(model="gpt-3.5-turbo-instruct")
# llm_message = llm.invoke(prompt_value)
# print('llm_message >> ', llm_message)

output_parser_message = output_parser.invoke(model_message)
print('output_parser_message >> ', output_parser_message)