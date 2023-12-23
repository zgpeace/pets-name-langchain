# 导入Langchain库中的OpenAI模块，该模块提供了与OpenAI语言模型交互的功能
from langchain.llms import OpenAI  

# 导入Langchain库中的PromptTemplate模块，用于创建和管理提示模板
from langchain.prompts import PromptTemplate  

# 导入Langchain库中的LLMChain模块，它允许构建基于大型语言模型的处理链
from langchain.chains import LLMChain  

# 导入dotenv库，用于从.env文件加载环境变量，这对于管理敏感数据如API密钥很有用
from dotenv import load_dotenv  

# 导入Langchain库中的ChatOpenAI类，用于创建和管理OpenAI聊天模型的实例。
from langchain.chat_models import ChatOpenAI

# 调用dotenv库的load_dotenv函数来加载.env文件中的环境变量。
# 这通常用于管理敏感数据，如API密钥。
load_dotenv()  

# 创建一个ChatOpenAI实例，配置它使用gpt-3.5-turbo模型，
# 设定温度参数为0.7（控制创造性的随机性）和最大令牌数为60（限制响应长度）。
chat = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.7,
    max_tokens=120
)
# 导入Langchain库中的模板类，用于创建聊天式的提示。
from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
)

template = "你是一个很有帮助的助手，可以进行翻译语言从 {input_language} 到 {output_language}."
human_template = "{text}"

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", template),
    ("human", human_template),
])

prompt = chat_prompt.format_messages(input_language="English", output_language="Chinese", text="I love programming.")
print('prompt >>> ', prompt)

# 使用chat函数（需要事先定义）发送生成的提示，获取结果。
result = chat(prompt)

# 打印聊天结果。
print('result >>> ', result)