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
    max_tokens=60
)

# 导入langchain.schema模块中的HumanMessage和SystemMessage类。
# 这些类用于创建符合特定格式的消息，以便ChatOpenAI类能正确处理。
from langchain.schema import (
    HumanMessage,
    SystemMessage
)

# 创建一个包含两条消息的列表：一条系统消息和一条人类消息。
# 系统消息定义了AI的角色（创意AI），而人类消息包含了用户的请求（为公司起名）。
messages = [
    SystemMessage(content="You are a creative AI."),
    HumanMessage(content="请给我的硅谷AI科技公司起个有创新的名字，可以参考OpenAI，DeepMind，Google，Facebook等等")
]

# 使用chat实例处理这些消息，并将结果存储在response变量中。
response = chat(messages)

# 打印响应内容。
print(response)

