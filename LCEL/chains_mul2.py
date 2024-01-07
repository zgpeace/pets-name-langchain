from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatOpenAI
from langchain_core.runnables import ConfigurableField
# We add in a string output parser here so the outputs between the two are the same type
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import ChatPromptTemplate
# Now lets create a chain with the normal OpenAI model
from langchain_community.llms import OpenAI
from operator import itemgetter

from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain_community.chat_models import ChatOpenAI

from dotenv import load_dotenv  # 导入从 .env 文件加载环境变量的函数
load_dotenv()  # 调用函数实际加载环境变量

from langchain.globals import set_debug  # 导入在 langchain 中设置调试模式的函数
set_debug(True)  # 启用 langchain 的调试模式

from langchain_core.runnables import RunnablePassthrough

prompt1 = ChatPromptTemplate.from_template(
    "generate a {attribute} color. Return the name of the color and nothing else:"
)
prompt2 = ChatPromptTemplate.from_template(
    "what is a fruit of color: {color}. Return the name of the fruit and nothing else:"
)
prompt3 = ChatPromptTemplate.from_template(
    "what is a country with a flag that has the color: {color}. Return the name of the country and nothing else:"
)
prompt4 = ChatPromptTemplate.from_template(
    "What is the color of {fruit} and the flag of {country}?"
)
model = ChatOpenAI()
model_parser = model | StrOutputParser()

color_generator = (
    {"attribute": RunnablePassthrough()} | prompt1 | {"color": model_parser}
)
color_to_fruit = prompt2 | model_parser
color_to_country = prompt3 | model_parser
question_generator = (
    color_generator | {"fruit": color_to_fruit, "country": color_to_country} | prompt4
)
prompt = question_generator.invoke("warm")
print('prompt >> ', prompt)
response = model.invoke(prompt)
print('response >> ', response)