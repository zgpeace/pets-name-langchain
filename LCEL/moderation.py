from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatOpenAI
from langchain_core.runnables import ConfigurableField
# We add in a string output parser here so the outputs between the two are the same type
from langchain_core.output_parsers import StrOutputParser
from langchain.chains import OpenAIModerationChain
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms import OpenAI

from dotenv import load_dotenv  # 导入从 .env 文件加载环境变量的函数
load_dotenv()  # 调用函数实际加载环境变量

from langchain.globals import set_debug  # 导入在 langchain 中设置调试模式的函数
set_debug(True)  # 启用 langchain 的调试模式

moderate = OpenAIModerationChain()
model = OpenAI()
prompt = ChatPromptTemplate.from_messages([("system", "repeat after me: {input}")])
chain = prompt | model
normal_response = chain.invoke({"input": "you are stupid"})
print('normal_response >> ', normal_response)

moderated_chain = chain | moderate
moderated_response = moderated_chain.invoke({"input": "you are stupid"})
print('moderated_response >> ', moderated_response)

