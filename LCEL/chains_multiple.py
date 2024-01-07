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

prompt1 = ChatPromptTemplate.from_template("what is the city {person} is from?")
prompt2 = ChatPromptTemplate.from_template(
    "what country is the city {city} in? respond in {language}"
)

model = ChatOpenAI()

chain1 = prompt1 | model | StrOutputParser()

chain2 = (
    {"city": chain1, "language": itemgetter("language")}
    | prompt2
    | model
    | StrOutputParser()
)

respone = chain2.invoke({"person": "obama", "language": "Chinese"})
print('respone >> ', respone)