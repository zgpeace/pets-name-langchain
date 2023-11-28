# 导入 Langchain 库中的 ChatOpenAI 类，用于与 OpenAI 聊天模型进行交互。
from langchain.chat_models import ChatOpenAI  

# 导入 PydanticOutputParser，用于将输出解析为 Pydantic 模型。
from langchain.output_parsers import PydanticOutputParser

# 导入 Pydantic BaseModel 类和 Field 函数，用于定义数据模型。
from langchain.pydantic_v1 import BaseModel, Field
from typing import List

# 导入 dotenv 库，用于从 .env 文件加载环境变量，管理敏感数据，如 API 密钥。
from dotenv import load_dotenv  

# 调用 load_dotenv 函数来加载 .env 文件中的环境变量。
load_dotenv()  

# 定义一个 Pydantic 数据模型，表示演员和他们参演的电影名称列表。
class Actor(BaseModel):
    name: str = Field(description="The name of the actor")
    film_names: List[str] = Field(description="list of names of films they starred in")

# 定义一个查询字符串，用于生成随机演员的电影作品列表。
actor_query = "Generate the filmography for a random actor."

# 创建一个 PydanticOutputParser 实例，用于解析 Pydantic 模型。
parser = PydanticOutputParser(pydantic_object=Actor)

# 定义一个格式不正确的字符串。
misformatted = "{'name': 'Tom Hanks', 'film_names': ['Forrest Gump']}"

# 打开注释则格式化报错： Expecting property name enclosed in double quotes: line 1 column 2
# parser.parse(misformatted)

# 导入 OutputFixingParser，用于修正输出格式错误。
from langchain.output_parsers import OutputFixingParser

# 创建一个 OutputFixingParser 实例，结合 Pydantic 解析器和 ChatOpenAI 模型。
new_parser = OutputFixingParser.from_llm(parser=parser, llm=ChatOpenAI())

# 使用新解析器解析格式不正确的字符串，并打印结果。
response = new_parser.parse(misformatted)
print(response)

