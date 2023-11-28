# 导入 ChatOpenAI 类，用于与 OpenAI 聊天模型进行交互。
from langchain.chat_models import ChatOpenAI  

# 导入 PromptTemplate 模块，用于创建和管理提示模板。
from langchain.prompts import PromptTemplate  

# 导入 PydanticOutputParser，用于将输出解析为 Pydantic 模型。
from langchain.output_parsers import PydanticOutputParser

# 导入 Pydantic 的 BaseModel 类和 Field 函数，用于定义数据模型。
from langchain.pydantic_v1 import BaseModel, Field
from typing import List

# 导入 dotenv 库，用于从 .env 文件加载环境变量，管理敏感数据如 API 密钥。
from dotenv import load_dotenv  

# 调用 load_dotenv 函数来加载 .env 文件中的环境变量。
load_dotenv()  

# 创建剧本梗概的提示模板。
synopsis_prompt = PromptTemplate.from_template(
    """你是一位剧作家。根据剧名，你的工作是为该剧写一个梗概。
剧名：{title}
剧作家：这是上面剧的一个梗概：
"""
)

# 创建剧评的提示模板。
review_prompt = PromptTemplate.from_template(
    """您是《纽约时报》的一位戏剧评论家。根据该剧的剧情简介，您的工作是为该剧撰写评论。
剧情简介：
{synopsis}
来自纽约时报戏剧评论家的评论：
"""
)

# 导入 StrOutputParser，用于解析字符串输出。
from langchain.schema import StrOutputParser

# 创建一个 ChatOpenAI 实例。
llm = ChatOpenAI()

# 创建处理链的两个部分：一个生成剧本梗概，另一个生成剧评。
# 使用 `|` 运算符将提示、模型和输出解析器连接起来。
from langchain.schema.runnable import RunnablePassthrough

# 创建生成剧本梗概的处理链。
synopsis_chain = synopsis_prompt | llm | StrOutputParser()

# 创建生成剧评的处理链。
review_chain = review_prompt | llm | StrOutputParser()

# 将两个处理链组合起来。
chain = {"synopsis": synopsis_chain} | RunnablePassthrough.assign(review=review_chain)

# 使用处理链生成对特定剧本标题的梗概和评论。
response = chain.invoke({"title": "海滩上日落时的悲剧"})

# 打印出生成的响应。
print(response)
