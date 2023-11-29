# 导入 Langchain 库的 ChatOpenAI 类，用于与 OpenAI 聊天模型进行交互。
from langchain.chat_models import ChatOpenAI  

# 导入 PromptTemplate 模块，用于创建和管理提示模板。
from langchain.prompts import PromptTemplate  


from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableBranch
from typing import Literal
from langchain.output_parsers.openai_functions import PydanticAttrOutputFunctionsParser
from langchain.utils.openai_functions import convert_pydantic_to_openai_function
from langchain.utils.openai_functions import convert_pydantic_to_openai_function


# 导入 dotenv 库，用于从 .env 文件加载环境变量，管理敏感数据如 API 密钥。
from dotenv import load_dotenv  

# 调用 load_dotenv 函数来加载 .env 文件中的环境变量。
load_dotenv()  

# 定义物理问题的提示模板
physics_template = """
你是一位非常聪明的物理教授。你擅长以简明易懂的方式回答物理问题。当你不知道某个问题的答案时，你会承认自己不知道。

以下是一个问题：
{input}
"""
physics_prompt = PromptTemplate.from_template(physics_template)

# 定义数学问题的提示模板
math_template = """
你是一个非常优秀的数学家。你擅长回答数学问题。你之所以这么厉害，是因为你能够把难题分解成组成部分，回答这些部分，然后把它们放在一起回答更广泛的问题。

这里有一个问题：
{input}
"""
math_prompt = PromptTemplate.from_template(math_template)

# 定义通用问题的提示模板
general_prompt = PromptTemplate.from_template(
    "您是一个很有帮助的助手。尽可能准确地回答问题。"
)

# 创建基于条件的提示分支
prompt_branch = RunnableBranch(
    (lambda x: x["topic"] == "物理", physics_prompt),
    (lambda x: x["topic"] == "数学", math_prompt),
    general_prompt
)

# 定义主题分类器模型
from langchain.pydantic_v1 import BaseModel
from typing import Literal

class TopicClassifier(BaseModel):
    "分类用户问题的主题"

    topic: Literal["物理", "数学", "通用"]
    "用户问题的主题。其中之一是'数学'，'物理'或'通用'。"


# 创建主题分类器函数
from langchain.utils.openai_functions import convert_pydantic_to_openai_function
classifier_function = convert_pydantic_to_openai_function(TopicClassifier)

print("classifier_function")
print(classifier_function)


# 创建 ChatOpenAI 实例并绑定主题分类器函数
llm = ChatOpenAI().bind(
    functions=[classifier_function], function_call={"name": "TopicClassifier"}
)

# 创建解析器
from langchain.output_parsers.openai_functions import PydanticAttrOutputFunctionsParser
parser = PydanticAttrOutputFunctionsParser(
    pydantic_schema=TopicClassifier, attr_name="topic"
)

# 创建分类链
classifier_chain = llm | parser

# 创建最终的处理链
from operator import itemgetter
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough

final_chain = (
    RunnablePassthrough.assign(topic=itemgetter("input") | classifier_chain)
    | prompt_branch
    | ChatOpenAI()
    | StrOutputParser()
)

# 使用处理链生成响应
response = final_chain.invoke({"input": "第一个大于 40 的质数是多少，且该质数的 1 加上能被 3 整除？"})
print(response)

response1 = final_chain.invoke({"input": "请解释什么是相对论。"})
print(response1)
