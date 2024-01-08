# !pip install langchain duckduckgo-search
from langchain.prompts import ChatPromptTemplate
from langchain.tools import DuckDuckGoSearchRun
from langchain_community.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv  # 导入从 .env 文件加载环境变量的函数
load_dotenv()  # 调用函数实际加载环境变量

from langchain.globals import set_debug  # 导入在 langchain 中设置调试模式的函数
set_debug(True)  # 启用 langchain 的调试模式

search = DuckDuckGoSearchRun()

template = """将以下用户输入转换为搜索引擎的搜索查询：:

{input}"""
prompt = ChatPromptTemplate.from_template(template)

model = ChatOpenAI()
chain = prompt | model | StrOutputParser() | search
response = chain.invoke({"input": "我想弄清楚今晚有什么体育运动可以看"})
print('response >> ', response)