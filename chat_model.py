# 导入Langchain库中的OpenAI模块，该模块提供了与OpenAI语言模型交互的功能
from langchain.llms import OpenAI  

# 导入Langchain库中的PromptTemplate模块，用于创建和管理提示模板
from langchain.prompts import PromptTemplate  

# 导入Langchain库中的LLMChain模块，它允许构建基于大型语言模型的处理链
from langchain.chains import LLMChain  

# 导入dotenv库，用于从.env文件加载环境变量，这对于管理敏感数据如API密钥很有用
from dotenv import load_dotenv  

# 导入openai库，以便使用OpenAI提供的API
import openai

# 调用load_dotenv函数来加载.env文件中的环境变量
load_dotenv()  

# 使用OpenAI的ChatCompletion接口创建一个响应。这个接口特别适合生成对话式的内容。
# 模型使用的是"gpt-3.5-turbo"，一种适用于快速响应和对话生成的GPT-3.5模型。
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    # messages是一个列表，包含与AI进行交互的信息。
    # 第一条信息定义了AI的角色，这里它被指定为一个“创意AI”。
    # 第二条信息是用户输入，要求AI为一家硅谷AI科技公司起一个创新的名字，参考OpenAI, DeepMind等。
    messages=[
        {"role": "system", "content": "You are a creative AI."},
        {"role": "user", "content": "请给我的硅谷AI科技公司起个有创新的名字，可以参考OpenAI，DeepMind，Google，Facebook等等"},
    ],
    # 设置温度为0.7，控制生成内容的创造性。
    temperature=0.7,
    # 设置最大令牌数量为60，限制响应的长度。
    max_tokens=60
)

# 打印从响应中获取的文本内容，去除首尾的空格。
# response是一个字典，其中'choices'包含了生成的内容。
print(response['choices'][0]['message']['content'])

# 打印完整的response.choices，以查看所有生成的选项。
print(response.choices)
