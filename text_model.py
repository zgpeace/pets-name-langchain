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

# 使用openai库中的Completion.create方法调用GPT-3模型
# 指定模型为text-davinci-003，温度设置为0.5以控制创造性，最大令牌数为100
# 提供的提示，用于生成公司名称
response = openai.Completion.create(
    model="text-davinci-003",
    temperature=0.5,
    max_tokens=100,
    prompt="请给我的硅谷AI科技公司起个有创新的名字，可以参考OpenAI，DeepMind，Google，Facebook等等")

# 打印响应中的文本，去除首尾的空格
print(response.choices[0].text.strip())