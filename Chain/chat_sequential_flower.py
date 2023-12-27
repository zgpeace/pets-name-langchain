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

# 导入所需要的库
from langchain.llms import OpenAI
from langchain.chains import LLMChain, SequentialChain
from langchain.prompts import PromptTemplate

from langchain.globals import set_debug

set_debug(True)

# 第一个LLMChain：生成鲜花的介绍
llm = OpenAI(temperature=.7)
template = """
你是一个植物学家。给定花的名称和类型，你需要为这种花写一个300字左右的介绍。
花名: {name}
颜色: {color}
植物学家: 这是关于上述花的介绍:"""
prompt_template = PromptTemplate(
    input_variables=["name", "color"],
    template=template
)
introduction_chain = LLMChain(
    llm=llm,
    prompt=prompt_template,
    output_key="introduction"
)

# 第二个LLMChain：根据鲜花的介绍写出鲜花的评论
template = """
你是一位鲜花评论家。给定一种花的介绍，你需要为这种花写一篇200字左右的评论。
鲜花介绍:
{introduction}
花评人对上述花的评论:"""
prompt_template = PromptTemplate(
    input_variables=["introduction"],
    template=template
)
review_chain = LLMChain(
    llm=llm,
    prompt=prompt_template,
    output_key="review"
)

# 第三个LLMChain：根据鲜花的介绍和评论写出一篇自媒体的文案
template = """
你是一家花店的社交媒体经理。给定一种花的介绍和评论，你需要为这种花写一篇社交媒体的帖子，300字左右。
鲜花介绍:
{introduction}
花评人对上述花的评论:
{review}
社交媒体帖子:
"""
prompt_template = PromptTemplate(
    input_variables=["introduction", "review"],
    template=template
)
social_post_chain = LLMChain(
    llm=llm,
    prompt=prompt_template,
    output_key="social_post_text"
)

# 总的链：按顺序运行三个链
overall_chain = SequentialChain(
    chains=[introduction_chain, review_chain, social_post_chain],
    input_variables=["name", "color"],
    output_variables=["introduction", "review", "social_post_text"],
    verbose=True
)

# 运行链并打印结果
result = overall_chain({
    "name": "玫瑰",
    "color": "红色"
})
print(result)
